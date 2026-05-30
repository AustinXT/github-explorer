#!/usr/bin/env python3
"""
解析 issue_comment 触发的 /analyze <github-url> 指令。

输入：comment body 从 stdin 读取（避免 shell 转义复杂度）
输出：
  - $GITHUB_OUTPUT: repo_url=<url>  matched=true|false
  - 匹配失败 exit 78（让 workflow 跳过，不算失败）
"""
from __future__ import annotations

import os
import re
import sys

PATTERN = re.compile(
    r"(?:^|\s)/analyze\s+(?:<)?(https?://github\.com/[\w.-]+/[\w.-]+)(?:>)?",
)


def emit(key: str, value: str) -> None:
    print(f"{key}={value}", file=sys.stderr)
    out_path = os.environ.get("GITHUB_OUTPUT")
    if out_path:
        with open(out_path, "a", encoding="utf-8") as f:
            f.write(f"{key}={value}\n")


def main() -> int:
    body = sys.stdin.read()
    m = PATTERN.search(body)
    if not m:
        emit("matched", "false")
        emit("repo_url", "")
        print("评论里没找到 /analyze <github-url>", file=sys.stderr)
        return 78
    url = m.group(1).rstrip("/")
    emit("matched", "true")
    emit("repo_url", url)
    print(url)
    return 0


if __name__ == "__main__":
    sys.exit(main())
