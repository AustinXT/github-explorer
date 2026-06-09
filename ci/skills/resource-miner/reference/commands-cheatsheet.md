# 命令速查（资源类，无 tokei/onefetch）

确定性指标已由 `collect_resource_facts.py` 采好写进 FACTS_JSON。以下命令供 subagent
**补查细节 / 抽样验证**（如死链率、某目录条目数、某条目内容）。`$REPO` = LOCAL_PATH。

## 读 FACTS_JSON（先用这个，别重复跑）
```bash
jq '.detected_type, .content_scale.total_human, .update_rhythm.automation_signature' "$FACTS_JSON"
jq '.content_scale.top_dirs' "$FACTS_JSON"          # 顶层目录即分类
jq '.network.repo_basics' "$FACTS_JSON"             # stars/forks/topics/license/homepage
```

## 内容规模 / 结构
```bash
du -sh "$REPO" --exclude=.git                        # 仓库体积
find "$REPO" -type f -not -path '*/.git/*' | wc -l   # 文件数
find "$REPO" -type f -not -path '*/.git/*' | sed 's/.*\.//' | sort | uniq -c | sort -rn | head   # 文件类型直方图
ls -d "$REPO"/*/ | xargs -I{} sh -c 'echo "$(find "{}" -type f | wc -l) {}"'   # 各顶层目录文件数
```

## README / 链接（awesome）
```bash
wc -c "$REPO"/README*.md                              # README 体量
grep -cE '^\s*[-*+]\s+\[' "$REPO"/README.md           # 列表型链接条目数
grep -oE '\]\(https?://[^)]+\)' "$REPO"/README.md | wc -l   # 外链总数
# 死链抽样（取前 20 条外链测 HTTP 状态，估失效率）
grep -oE 'https?://[^) ]+' "$REPO"/README.md | head -20 | while read u; do
  echo "$(curl -s -o /dev/null -w '%{http_code}' --max-time 8 "$u") $u"; done
```

## 更新节奏 / 自动化签名（已在 FACTS，必要时复核）
```bash
git -C "$REPO" log --format='%ai' | awk '{print $2}' | cut -c1-5 | sort | uniq -c | sort -rn | head   # 提交时:分聚集
git -C "$REPO" log --format='%ai' -1                  # 最近一次提交
git -C "$REPO" shortlog -sn --all --no-merges | head  # 贡献者集中度
ls "$REPO"/.github/workflows/ 2>/dev/null             # 是否有 CI（自动查链/校验贡献）
```

## 学习资料（learning）
```bash
grep -cE '^#{1,3}\s' "$REPO"/README.md                # 章节数（学习路径粒度）
find "$REPO" -name '*.md' | wc -l                     # 内容文件数
ls "$REPO" | grep -iE 'translat|i18n|zh|en'           # 多语言/翻译同步
find "$REPO" -name '*.py' -o -name '*.ipynb' -o -name '*.js' | head  # 是否含可跑代码示例
```

## 抽样阅读内容（判断策展质量必做）
```bash
sed -n '1,80p' "$REPO"/README.md                      # README 头部（导航/收录标准）
# 抽读某顶层目录下一个条目，看有无点评/取舍
```

> WebFetch 失败可用 JINA reader 兜底：`https://r.jina.ai/<url>`。
> 死链抽样只为估失效率，不必全量；curl 超时设短（--max-time 8）避免拖慢。
