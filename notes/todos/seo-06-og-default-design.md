# TODO · 设计版 og-default.png

**当前状态**：`site/public/og-default.png` 是 ImageMagick 临时合成的占位卡 — 灰白渐变 + 黑色"GitHub Explorer"文字 + 红色副标题。能用，但不够品牌。

## 影响

- 首页 / 列表 / 标签等"无独立 OG 图"的页面分享到微信/Twitter/Slack 时显示这张卡 → 决定第一眼印象
- 报告详情页**不受影响** — 已经走 `getReportOgImage()` 借用 GitHub 仓库的 OG 图（每个仓库自带，自动好看）

## 替换要求

- 尺寸：1200×630（OG 标准 / Twitter summary_large_image）
- 格式：PNG（不要 SVG，Twitter Card 不支持）
- 文件大小 < 8MB（Facebook 上限），最好 < 300KB
- 中央留出文字安全区，左右各 100px 边距别放关键信息（小屏裁切）
- 文件名固定 `og-default.png`，覆盖即可，无需改代码

## 内容建议

主元素：
- "GitHub Explorer" 主标题
- "深度挖掘 GitHub 仓库价值" 副标
- 一个能传达"分析报告"的视觉符号（如：放大镜 + 代码片段 / 数据网络图 / 仓库图标矩阵）
- 数字背书："375+ 篇深度分析"

可选：
- 顶部一行小字 "AI Agent · LLM · DevTools" 体现内容范畴
- 二维码角标（公众号引流，可选）

## 自动化可能

如果以后要做"每篇报告生成专属 OG 卡"（替代当前借用 GitHub 的方案），可用：

- **构建期**：`satori` + `@vercel/og`（React JSX → PNG），Astro 5 有 [官方集成示例](https://docs.astro.build/en/recipes/og-images/)
- **运行期**：上线一个 `og.png?slug=...` endpoint，但 GitHub Pages 是静态托管，得搭配 Cloudflare Workers / Vercel

当前借用 GitHub OG 的方案 0 成本 0 维护，**除非有强需求，不必上**。
