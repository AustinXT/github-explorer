#!/usr/bin/env python3
"""阶段 1 数据库迁移的单元测试（stdlib unittest，不引入 pytest）。

运行方式：
    python3 -m unittest tests/test_db.py -v

测试用临时 sqlite 文件，与 src/data/db.sqlite 隔离。
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import init_db  # noqa: E402


class TempDBTest(unittest.TestCase):
    """共享一个临时 DB 文件，每个测试自动 fresh schema。"""

    def setUp(self) -> None:
        self.tmpfile = tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False)
        self.tmpfile.close()
        self.db_path = Path(self.tmpfile.name)
        # 替换全局路径以便 init_db 的辅助函数也指到临时文件
        self._orig_db = init_db.DB_PATH
        init_db.DB_PATH = self.db_path

    def tearDown(self) -> None:
        init_db.DB_PATH = self._orig_db
        try:
            os.unlink(self.db_path)
        except OSError:
            pass

    def conn(self) -> sqlite3.Connection:
        c = init_db.get_connection(self.db_path)
        init_db.ensure_schema(c)
        return c


class TestInitDB(TempDBTest):
    def test_idempotent(self):
        """ensure_schema 两次不重复应用同一 migration。"""
        c = self.conn()
        v1 = init_db.ensure_schema(c)
        v2 = init_db.ensure_schema(c)
        self.assertEqual(v1, v2)
        n = c.execute("SELECT COUNT(*) FROM schema_version").fetchone()[0]
        self.assertEqual(n, len(init_db.MIGRATIONS),
                         "schema_version 应只有 len(MIGRATIONS) 行，每次 migration 仅插入一次")
        c.close()


class TestSchemaConstraints(TempDBTest):
    def test_unique_slug(self):
        """重复 slug 应 raise IntegrityError。"""
        c = self.conn()
        c.execute("INSERT INTO reports (slug, title, mtime) VALUES ('foo', 'F', '2026-01-01')")
        with self.assertRaises(sqlite3.IntegrityError):
            c.execute("INSERT INTO reports (slug, title, mtime) VALUES ('foo', 'F2', '2026-01-02')")
        c.close()

    def test_unique_original_url(self):
        """重复 original_url 应 raise IntegrityError。"""
        c = self.conn()
        c.execute(
            "INSERT INTO reports (slug, title, mtime, original_url) VALUES (?, ?, ?, ?)",
            ("a", "A", "2026-01-01", "https://github.com/x/y"),
        )
        with self.assertRaises(sqlite3.IntegrityError):
            c.execute(
                "INSERT INTO reports (slug, title, mtime, original_url) VALUES (?, ?, ?, ?)",
                ("b", "B", "2026-01-02", "https://github.com/x/y"),
            )
        c.close()

    def test_published_state_check(self):
        """published_state 非枚举值应 fail。"""
        c = self.conn()
        with self.assertRaises(sqlite3.IntegrityError):
            c.execute(
                "INSERT INTO reports (slug, title, mtime, published_state) VALUES (?, ?, ?, ?)",
                ("x", "X", "2026-01-01", "wrong_state"),
            )
        c.close()

    def test_orphan_tag_fkey(self):
        """report_tags 引用不存在的 tag 应 fail。"""
        c = self.conn()
        c.execute("INSERT INTO reports (slug, title, mtime) VALUES ('foo', 'F', '2026-01-01')")
        with self.assertRaises(sqlite3.IntegrityError):
            c.execute("INSERT INTO report_tags (slug, tag) VALUES ('foo', 'nonexistent-tag')")
        c.close()

    def test_negative_stars(self):
        """stars < 0 应 fail。"""
        c = self.conn()
        with self.assertRaises(sqlite3.IntegrityError):
            c.execute(
                "INSERT INTO reports (slug, title, mtime, stars) VALUES (?, ?, ?, ?)",
                ("a", "A", "2026-01-01", -1),
            )
        c.close()


class TestUrlNormalization(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(init_db.normalize_url("https://github.com/Foo/Bar"), "https://github.com/foo/bar")

    def test_trailing_slash(self):
        self.assertEqual(init_db.normalize_url("https://github.com/foo/bar/"), "https://github.com/foo/bar")

    def test_preserves_double_slash(self):
        """rstrip('/') 不应剥掉 https:// 前的 // —— Python str.rstrip 是按字符剥两端。"""
        u = init_db.normalize_url("https://github.com/foo/bar")
        self.assertTrue(u.startswith("https://"))

    def test_none(self):
        self.assertIsNone(init_db.normalize_url(None))


class TestTagLockProtection(TempDBTest):
    def test_locked_slug_not_overwritten(self):
        """report_tag_locks 中的 slug 在 extract_tags 重跑时其 report_tags 不被覆盖。"""
        c = self.conn()
        # 准备：插入 1 个报告 + 2 个标签 + 1 个锁
        c.execute("INSERT INTO reports (slug, title, mtime) VALUES ('locked', 'L', '2026-01-01')")
        c.execute("INSERT INTO reports (slug, title, mtime) VALUES ('free', 'F', '2026-01-01')")
        c.execute("INSERT INTO tags (tag, label) VALUES ('manual-tag', 'Manual')")
        c.execute("INSERT INTO tags (tag, label) VALUES ('auto-tag', 'Auto')")
        c.execute("INSERT INTO report_tags (slug, tag) VALUES ('locked', 'manual-tag')")
        c.execute("INSERT INTO report_tag_locks (slug) VALUES ('locked')")
        c.commit()

        # 模拟 extract_tags 行为：对非锁定 slug 重写标签
        import extract_tags
        slug_to_tags = {"locked": ["auto-tag"], "free": ["auto-tag"]}
        extract_tags.write_report_tags(c, slug_to_tags)

        # 锁定 slug 保留 manual-tag；free 应被覆盖为 auto-tag
        locked_tags = [r[0] for r in c.execute("SELECT tag FROM report_tags WHERE slug='locked'")]
        free_tags = [r[0] for r in c.execute("SELECT tag FROM report_tags WHERE slug='free'")]
        self.assertEqual(locked_tags, ["manual-tag"], "锁定 slug 的标签应保留")
        self.assertEqual(free_tags, ["auto-tag"], "未锁定 slug 应被覆盖")
        c.close()


class TestExportJsonRoundtrip(TempDBTest):
    def test_published_roundtrip(self):
        """state=published + at=Y → compose 出 'published:Y'，与现有 reports.json 格式兼容。"""
        c = self.conn()
        c.execute(
            "INSERT INTO reports (slug, title, mtime, published_state, published_at) "
            "VALUES (?, ?, ?, ?, ?)",
            ("a", "A", "2026-01-01", "published", "2026-04-01"),
        )
        c.execute(
            "INSERT INTO reports (slug, title, mtime, published_state) VALUES (?, ?, ?, ?)",
            ("b", "B", "2026-01-01", "pending"),
        )
        c.execute(
            "INSERT INTO reports (slug, title, mtime, published_state, published_at) "
            "VALUES (?, ?, ?, ?, ?)",
            ("c", "C", "2026-01-01", "excluded", None),
        )
        c.commit()
        c.close()

        rows = init_db.dump_reports()
        by_slug = {r["slug"]: r for r in rows}
        self.assertEqual(by_slug["a"]["published"], "published:2026-04-01")
        self.assertEqual(by_slug["b"]["published"], "pending")
        self.assertEqual(by_slug["c"]["published"], "excluded")


class TestUserStarredView(TempDBTest):
    def test_join_to_reports(self):
        """v_user_starred 应能将 user_starred.url 与 reports.original_url 关联出 report_slug。"""
        c = self.conn()
        c.execute("INSERT INTO users (login, name) VALUES ('alice', 'Alice')")
        c.execute(
            "INSERT INTO reports (slug, title, mtime, original_url) VALUES (?, ?, ?, ?)",
            ("foo_bar", "Foo Bar", "2026-01-01", "https://github.com/foo/bar"),
        )
        c.execute(
            "INSERT INTO user_starred (login, url, name, stars, starred_at) "
            "VALUES (?, ?, ?, ?, ?)",
            ("alice", "https://github.com/foo/bar", "foo/bar", 100, "2026-01-02"),
        )
        c.execute(
            "INSERT INTO user_starred (login, url, name, stars, starred_at) "
            "VALUES (?, ?, ?, ?, ?)",
            ("alice", "https://github.com/x/y", "x/y", 50, "2026-01-03"),
        )
        c.commit()

        rows = dict(c.execute(
            "SELECT url, report_slug FROM v_user_starred WHERE login='alice'"
        ).fetchall())
        self.assertEqual(rows["https://github.com/foo/bar"], "foo_bar")
        self.assertIsNone(rows["https://github.com/x/y"])
        c.close()

    def test_user_starred_cascade_delete(self):
        """删除 users 行应级联清理 user_starred / user_tags / snapshot。"""
        c = self.conn()
        c.execute("INSERT INTO users (login, name) VALUES ('bob', 'Bob')")
        c.execute("INSERT INTO user_tags (login, tag) VALUES ('bob', 'devtools')")
        c.execute(
            "INSERT INTO user_starred_snapshot (login, fetched_at) VALUES ('bob', '2026-01-01')"
        )
        c.execute(
            "INSERT INTO user_starred (login, url, name, stars, starred_at) "
            "VALUES (?, ?, ?, ?, ?)",
            ("bob", "https://github.com/a/b", "a/b", 1, "2026-01-01"),
        )
        c.commit()
        c.execute("DELETE FROM users WHERE login='bob'")
        c.commit()

        self.assertEqual(c.execute("SELECT COUNT(*) FROM user_tags").fetchone()[0], 0)
        self.assertEqual(c.execute("SELECT COUNT(*) FROM user_starred").fetchone()[0], 0)
        self.assertEqual(c.execute("SELECT COUNT(*) FROM user_starred_snapshot").fetchone()[0], 0)
        c.close()


class TestStarredJsonRoundtrip(TempDBTest):
    def test_dump_preserves_user_order_and_tags(self):
        """dump_starred 应按 users.sort_order 输出 users；tags 按 position 输出（与 yaml 顺序一致）。"""
        c = self.conn()
        c.execute("INSERT INTO users (login, name, sort_order) VALUES ('u2', 'U2', 1)")
        c.execute("INSERT INTO users (login, name, sort_order) VALUES ('u1', 'U1', 0)")
        c.execute("INSERT INTO user_tags (login, tag, position) VALUES ('u1', 'b-tag', 0)")
        c.execute("INSERT INTO user_tags (login, tag, position) VALUES ('u1', 'a-tag', 1)")
        c.commit()
        c.close()

        data = init_db.dump_starred()
        self.assertEqual([u["login"] for u in data["users"]], ["u1", "u2"])
        self.assertEqual(data["users"][0]["tags"], ["b-tag", "a-tag"])


class TestPublishMdParsing(unittest.TestCase):
    """测试三种行格式都被正确解析（修复历史隐 bug）。"""

    def _parse(self, content: str) -> dict:
        import tempfile
        from pathlib import Path
        import build_reports_index as br
        old_file = br.PUBLISH_FILE
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write(content)
            br.PUBLISH_FILE = Path(f.name)
        try:
            return br.parse_publish_index()
        finally:
            br.PUBLISH_FILE = old_file
            os.unlink(f.name)

    def test_published_4col(self):
        idx = self._parse(
            "# 公众号发布记录\n\n"
            "| 文件 | 标题 | 发布日期 |\n"
            "|------|------|----------|\n"
            "| [a.md](analysis_report/a.md) | A 标题 | 2026-04-01 |\n"
        )
        self.assertIn("a", idx)
        self.assertEqual(idx["a"]["state"], "published")
        self.assertEqual(idx["a"]["at"], "2026-04-01")
        self.assertEqual(idx["a"]["title"], "A 标题")

    def test_excluded_2col(self):
        idx = self._parse(
            "## 不发布列表\n\n"
            "| 文件 | 原因 |\n|------|------|\n"
            "| [b.md](analysis_report/b.md) | 选题重复 |\n"
        )
        self.assertIn("b", idx)
        self.assertEqual(idx["b"]["state"], "excluded")
        self.assertEqual(idx["b"]["reason"], "选题重复")

    def test_draft_3col_bare(self):
        idx = self._parse(
            "## 不发布列表\n\n"
            "| c.md | 自动生成 | 2026-05-30 (已入草稿) |\n"
        )
        self.assertIn("c", idx)
        self.assertEqual(idx["c"]["state"], "pending")
        self.assertEqual(idx["c"]["at"], "2026-05-30")
        self.assertEqual(idx["c"]["reason"], "自动生成")

    def test_slug_lowercased(self):
        """Slug 必须 lowercase 与 Astro entry.id 对齐。"""
        idx = self._parse(
            "| [Aider-AI_Aider.md](analysis_report/Aider-AI_Aider.md) | T | 2026-04-01 |\n"
        )
        self.assertIn("aider-ai_aider", idx)


if __name__ == "__main__":
    unittest.main(verbosity=2)
