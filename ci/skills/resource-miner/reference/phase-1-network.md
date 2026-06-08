# Phase 1 — 网络分析（资源视角）

**目标**：作者画像、社区热度与增长、生态网络、同主题竞品、知识入口、展示素材。
与 repo-miner 的 Phase 1 高度一致，**去掉代码语言解读**，作者动机改从「策展人/运营者」角度切入。

**输入变量**：FULL_NAME / OWNER / REPO / GITHUB_URL / LOCAL_PATH / DEFAULT_BRANCH / FACTS_JSON（采集脚本输出的 JSON 路径）

**先做**：`Read FACTS_JSON`，重点读 `network` 块（`repo_basics` / `author` / `community` / `ecosystem` / `issues` / `media`）。
确定性数据已采好，本阶段只做**判断与外部情报补充**（WebSearch / WebFetch），不重复跑 gh。
若 `network` 为 null（无 gh/无网络），就只用离线信息 + WebSearch 补，标注数据受限。

## 1.1 基础数据（读 `network.repo_basics`）
stars / forks / 描述 / homepage / topics / license / `heat_level`（极小众/小众精品/中等热度/大众热门）。

## 1.2 作者画像（读 `network.author`，资源视角重写）
- 背景：login / name / bio / company / followers / public_repos / `top_repos`
- **关键判断（资源类特有）**：
  - **技术人 → 策展人/运营者的转型**？作者是否有工程背景却来做内容策展（往往更有工具化、自动化能力）
  - **是否系列化运营**：`top_repos` 里有没有同主题的姊妹资源仓库（如同时维护多个 awesome / 多本电子书库）→ 形成覆盖矩阵/双寡头
  - 动机推测：个人品牌 / 招聘名片 / 流量入口 / 商业导流 / 纯公益
- 贡献集中度：`network.author.contributors` + `top_contributor_share_pct`（多数资源仓库是单人或极少数主导）

## 1.3 社区热度与增长（读 `network.community`）
- `growth_pattern`（爆发型/高速增长/稳步增长/平稳放缓）+ 采样 stargazer 时间线
- 判断：是「现象级爆款」还是「长尾稳增」？热度与实际维护投入是否匹配（高 star + 零互动是资源仓库常见反差）

## 1.4 生态网络与竞品候选（读 `network.ecosystem` + WebSearch 精化）
- `competitor_candidates` 是同 topic+语言的机械候选，对资源类**需用 WebSearch 重判**：
  - awesome → 搜「同主题 awesome list」「awesome-X alternatives」
  - learning → 搜「同主题 教程/路线图/课程」「best X roadmap/tutorial」
  - atypical → 搜该资源细分的同类项目
- 产出 3-5 个**真实同主题竞品**（带 star/特点），供 Phase 3 竞品矩阵。无则标注「无明显竞品」。

## 1.5 官方文档 / 博客 / 外部评价（WebFetch + WebSearch）
- WebFetch homepage（若有）+ README 里的官网/App/导流链接（资源仓库常植入商业化入口，是「战略意图」的关键证据）
- WebSearch 外部评价：是否被知名清单/媒体/社区推荐、是否被 Internet Archive 等保存机构备份（资源价值的外部认可信号）

## 1.6 关键 Issue 信号（读 `network.issues`）
选 2-3 个能揭示**策展张力**的 issue：收录标准争议、失效链接投诉、版权/合规质疑、收录请求积压 → 反映治理质量与运营负担。

## 1.7 知识入口
DeepWiki（`deepwiki.com/<owner>/<repo>`）、Zread.ai（`zread.ai/<owner>/<repo>`）是否收录；关联论文/官网/在线 Demo。逐个给链接或标「未收录/无」。

## 1.8 展示素材（读 `network.media`）
- README 里 `verified=true` 的图片直接用；资源仓库常**无展示图**，此时可在 Phase 3 用「目录结构 code block」展示策展结构代替（见报告模板「项目展示」节）
- 最终 ≤5 个素材，过滤 badge/赞助/社交小图标

## 返回格式（结构化摘要，回主对话）

```
### Phase 1 网络分析摘要

**基础数据**: stars X / forks X / heat=... / topics=[...] / license=...
**作者画像**: [背景 + 技术人→策展人判断 + 是否系列化运营 + 动机推测]
**社区热度与增长**: [growth_pattern + 热度vs投入反差判断]
**同主题竞品**(供 Phase 3): 1) name(stars,特点) 2) ... | 或「无明显竞品」
**官方文档/导流/外部评价**: [官网/App 导流链接 + 外部认可信号] | 或「无」
**关键 Issue 信号**: [2-3 条策展张力] | 或「Issues 关闭/无」
**知识入口**: DeepWiki[..] Zread[..] 论文[..] Demo[..]
**展示素材**: [图片 markdown ≤5] | 或「无展示图，建议用目录结构展示」
```
