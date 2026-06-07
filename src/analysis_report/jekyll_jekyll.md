# 13 年 51K stars：Jekyll 为什么仍是 GitHub Pages 的默认引擎

> GitHub: https://github.com/jekyll/jekyll

## 一句话总结
Jekyll 选择「git push 即发布」的极简哲学——以一个线性 `Site#process` 管线、反射式插件发现、三维 Hooks 注册表、Regenerator 增量构建等朴素但长寿的设计，把「写博客/文档」从数据库+运行时压缩成静态 HTML，让一个 2008 年的 SSG 在 2026 年仍是 GitHub Pages 的官方引擎。

## 值得关注的理由
- **生态护城河几乎不可复制**：GitHub Pages 官方默认引擎 = `github.io` 用户零配置一键发布，13 年沉淀的官方/第三方插件矩阵（feed、seo、sitemap、paginate 等）形成正向飞轮。
- **「克制即胜利」的工程哲学样本**：放弃并行/异步换取心智模型清晰；放弃「多格式输出同源」留给插件；放弃内置评论/搜索/表单——明确的 NOT-done 让核心保持瘦。
- **长寿命开源项目治理范式**：1,245 名贡献者、Parker Moore 27.9% 主导、`master` 仍接收提交、`History.markdown` 13 年没断，160 个 tag 严格 SemVer，是「职业级开源」的标本。

## 项目展示

> README 媒体在本次采集中未抓到（README 实际存在但 collect 未覆盖），已用官网 hero 图替代。

| 资源 | 链接 | 类型 |
|---|---|---|
| Jekyll 品牌 logo | <https://jekyllrb.com/img/logo-2x.png> | hero |
| Octojekyll 宣传图 | <https://jekyllrb.com/img/octojekyll.png> | hero（首页 Octocat 风格） |

## 项目画像

| 维度 | 数据 |
|------|------|
| GitHub | <https://github.com/jekyll/jekyll> |
| Star / Fork | 51,475 / 10,283 |
| Watcher | 1,399 |
| 代码行数 | 28,103（不含空行/注释） |
| 语言分布 | Ruby 60% / Gherkin 16%（Cucumber BDD） / Sass 8% / YAML 6% / JavaScript 4% / HTML 3% |
| 项目年龄 | 211.8 个月（≈17.6 年，首次提交 2008-10-19） |
| 最近推送 | 2026-04-22 |
| 开发阶段 | 低维护（稳定末期；近 365 天 27 commit，但 160 个 tag 持续小修小补） |
| 贡献模式 | 社区协作（1,245 名贡献者，Top 1 @parkr 占 27.9%，@jekyllbot 占 22%） |
| 热度定位 | 大众热门（51K stars，SSG 品类事实标准之一） |
| 质量评级 | 代码[优秀] 文档[优秀] 测试[充分] CI/CD[完善] 错误处理[规范] |
| 话题标签 | ruby, jekyll, static-site-generator, blog-engine, markdown, liquid |
| License | MIT |
| Release | v4.4.1（共 160 个 tag，100 个 GitHub Release，SemVer 严格） |
| 依赖 | Ruby 2.7.0+，Liquid/Kramdown/Rouge/SafeYAML/Webrick（gem 体系） |

## 作者视角：为什么存在这个项目

### 创始人/作者背景
Jekyll 由 **Tom Preston-Werner（mojombo）**——GitHub 联合创始人——在 2008 年于 GitHub 内部孵化、用于支撑 GitHub Pages。早期核心团队后由社区接管，Parker Moore（@parkr）作为项目维护者占贡献量的 27.9%。@jekyll 组织化运营 13.5 年，54 个公开仓库里 jekyll/jekyll 以 51K stars 远超次席 jekyll-seo-tag 的 1,719，是组织绝对旗舰。Tom 在 GitHub 内部承担过「为每个 Repo 生成静态页面」的运维与一致性压力——他意识到「每次动态渲染」的成本可以前置到「提交时」消化，把构建从运行时搬到 build-time。

### 问题判断
2008 年时：WordPress/MovableType 等动态博客依赖数据库+运行时（PHP/MySQL），安装、备份、迁移、抗 DDoS 都有成本；安全补丁频发；评论/插件带来的复杂度超出「写文章」本身。真正的静态生成器仍非常小众（Nanoc 偏 Ruby 程序员、Blosxom 偏 Perl、Hugo 尚未诞生），没有面向「非程序员博主」的「开箱即用」工作流。Tom 写 Jekyll 既是解决 GitHub Pages 引擎的内部痛点，又同时把 GitHub Pages 绑定为一个零运维的「发布 SaaS」，形成正向飞轮。

### 解法哲学
- **极简 vs 功能完整**：Jekyll does what you tell it to do — no more, no less. Markdown + Liquid + Front Matter + Layouts 完成 80% 博客需求。
- **性能 vs 易用**：易用始终优先——`Site#process` 仍是 reset→read→generate→render→cleanup→write 的同步线性管线，无并行/异步；性能靠 LiquidRenderer 模板 parse 缓存、Regenerator 增量、Cache 落盘「打补丁」。
- **开放生态**：Converter/Generator/Command/Tag/Filter/Hook 五大插件入口，`Jekyll::Plugin.descendants` 反射发现，零样板。
- **标准化 vs 魔幻**：YAML + Markdown + Liquid 三件套都来自成熟生态，故意不发明模板 DSL，复用 Shopify/Liquid 生态。
- **明确的 NOT-done**：① 不做「多格式输出同源」（HTML/JSON/AMP/feed 共存留给插件，见 Issue #3041 长期开放讨论）② 不内置评论/搜索/表单 ③ 不替代数据库。

### 战略意图
Jekyll 是「瘦核心 + 胖插件」的开源模式，所有官方可选能力（feed、sitemap、SEO、paginate、redirect-from、coffeescript、gist）都以独立 gem（`jekyll-*`）发布，与核心解耦——这是 GitHub 在 Ruby 生态里典型的「中央仓 + 卫星包」治理模型。商业化**不在 Jekyll 本体**，而在 GitHub Pages（云端托管/构建）以及 Grav/CloudCannon/Siteleaf 等「编辑体验」第三方。Jekyll 维持 MIT + 完全开源，保护了「GitHub Pages 的引擎」这一定位，这是它能维持 13 年中立性的关键。

## 核心价值提炼

### 创新之处
1. **Plugin.descendants 反射式插件发现**（新颖度 4/5 / 实用性 5/5 / 可迁移性 5/5）：`Jekyll::Plugin.inherited` 在子类定义时自动登记到 `Set`，运行时无需注册表。Ruby/Rails 生态几乎人手一份。
2. **Hooks 三维注册表**（3/5 / 5/5 / 5/5）：用 `[-priority, load_order]` 作为排序键，让多个插件在同一阶段按优先级有序执行。调试极简——`Jekyll::Hooks.trigger` 是同步调用，stack trace 干净。
3. **Drops 模板沙箱**（3/5 / 4/5 / 4/5）：`Jekyll::Drops::Drop < Liquid::Drop` 包装内部对象，`delegate_method` / `data_delegator` DSL 显式声明「模板能访问哪些字段」，`SETTER_KEYS_STASH` + `NON_CONTENT_METHOD_NAMES` 压成本。
4. **Regenerator 增量构建**（4/5 / 5/5 / 5/5）：每个文档渲染结束记一份 `{mtime, deps: [layout_path, include_paths, ...]}` 落盘；下次构建按「源变了 OR 任一 dep 变了 OR 目标缺失」判定是否重渲。Issue #380 长期痛点最终靠这个解决。
5. **Theme = Gem「内容、设计、逻辑」三分离**（4/5 / 4/5 / 3/5）：把皮肤建模为普通 gem，`load_theme_configuration` 合并主题配置但禁止主题覆盖 Jekyll 默认值；symlink 直接 bail 防止恶意主题指向外部目录。
6. **parse / render 分阶段缓存**（3/5 / 4/5 / 4/5）：Liquid 模板拆成「parse（昂贵，只一次）+ render（廉价，可重入）」两阶段；`stats_table` 用 `terminal-table` 给出 TOP-N 慢模板。
7. **自指 dogfooding**（3/5 / 4/5 / 3/5）：`docs/` 目录是 Jekyll 站点的源，`docs/_config.yml` 用自己的 `_layouts`/`_includes`/`_data`——jekyllrb.com 的部署产物 = Jekyll 构建产物。

### 可复用的模式与技巧
1. **中央容器 + 显式线性管线（Site#process = reset→read→generate→render→cleanup→write）**——可迁移到任何批量文档生成、报告生成、ETL 流程。
2. **Plugin 抽象 + 反射发现 + 优先级**——可迁移到任何「用户放个文件就生效」的扩展框架。
3. **Hooks 三维注册表（owner × event × priority）**——可迁移到构建工具的扩展点、CI runner、IDE processor pipeline。
4. **配置三层合并（DEFAULTS < _config.yml < override）+ Hash 子类**——可迁移到任何 CLI 工具的配置加载。
5. **Drops 模板沙箱**——可迁移到 CMS 字段过滤、API 响应脱敏、模板注入防护。
6. **Regenerator 增量构建（mtime 摘要 + 依赖图）**——可迁移到文档站、报告生成、邮件模板预编译、ETL 增量同步。
7. **Render 三段式（Liquid → Converter Chain → Layout 俄罗斯套娃）**——可迁移到邮件、PDF、报表、Markdown 文档。
8. **Theme = Gem**——可迁移到可插拔皮肤系统（CMS 主题、IDE 主题、报表模板）。
9. **`benchmark/` 目录的 micro-bench 习惯**——`symbol-to-proc` / `schwartzian_transform` / `native-vs-pathutil-relative` 等独立脚本让 PR 评审可以「看到这个改动快了多少」。
10. **`rubocop/` 自定义风格规则**——避免用 `get_` 前缀等历史包袱污染主仓库。
11. **用框架构建框架的官网**——dogfooding 之王道；VitePress、Hexo、Astro 的官方站都是这个模式。

### 关键设计决策
1. **Site 是中央容器，构建流程是显式线性管线**（reset→read→generate→render→cleanup→write）：放弃「全自动黑盒」灵活性换心智模型清晰，代价是性能（无并行），但通过 Regenerator 增量与 Cache 落盘缓解。
2. **Plugin 抽象 + 反射式子类发现（`descendants`）**：不显式注册 → 加载顺序由 `Dir[].sort` 决定，调试「插件冲突」需要靠 `priority` 机制兜底。
3. **Hook 系统按「owner + event + priority」三维注册**：`@registry = { owner: { event: [block, ...] } }`，每个 block 进入时用 `[-priority, load_order]` 作为排序键。
4. **Render 阶段用三层流水线（Liquid → Converter Chain → Layout 俄罗斯套娃）**：默认关闭 Markdown 内的 Liquid（`render_with_liquid?` 默认 false），避免「`{{ something }}` 嵌在 Markdown 里没渲染」困扰。
5. **Configuration 三层合并（DEFAULTS < _config.yml < override）+ Hash 子类**：YAML 反序列化即配置，`Configuration#stringify_keys` 兜底用户配置里有 `clear` key 与 Hash#clear 冲突。
6. **Front Matter Defaults 按「路径 glob + 类型 + 优先级」合并**：声明式比命令式多一层「匹配规则心智」，但用户基本能「照抄示例」就懂。
7. **safe 模式 + 插件白名单**：`safe: true` 下 `instantiate_subclasses` 只保留 `klass.safe == true` 的插件；同时支持 `whitelist: ['my-trusted-plugin']`。
8. **液态模板解析缓存（LiquidRenderer::File）**：模板数量爆炸时是隐患——但博客场景的 layout/include 数量在百级以下，问题不大。

## 竞品格局与定位

### 竞品对比矩阵

| 维度 | Jekyll | Hugo | Eleventy (11ty) | Gatsby |
|------|--------|------|----------------|--------|
| 引擎语言 | Ruby | Go | Node.js | React + GraphQL |
| Stars | 51K | 78K | 30K | 55K |
| 构建速度（10K 页） | 分钟级 | 秒级 | 中等 | 慢 |
| 部署形式 | Ruby 运行时 + gem | 单二进制 | Node.js | Node.js + Webpack/Vite |
| 模板引擎 | Liquid（独家） | Go template | Nunjucks/Liquid/Handlebars/Mustache/Pug/EJS | React/JSX |
| 增量构建 | ✅ Regenerator（成熟） | ✅ 天然 | 早期需手写 | ✅ |
| GitHub Pages 原生 | ✅ 官方引擎 | ❌ | ❌ | ❌ |
| 冷启动成本 | 5 分钟 | 中 | 中 | 高（需懂 React + GraphQL） |
| 多语言 | 靠插件 | ✅ 原生 | 靠插件 | 靠插件 |
| 客户端交互 | 弱 | 弱 | 中 | 强（React 运行时） |
| 数据层 | `_data/*.yml` | 模板/数据 | `_data/*` | GraphQL 统一图 |
| 错误可调试性 | 优秀（Ruby stack） | 优秀 | 优秀 | 较差（GraphQL 错误栈劝退新人） |

### 差异化护城河
- **生态护城河（强）**：GitHub Pages 官方引擎 + 13 年沉淀的官方/第三方插件矩阵 + 大量「用 Jekyll 写」的教程与主题。
- **信任护城河（强）**：MIT 协议 + 透明治理（`team/` 公开 + 议程公开）+ 长期稳定的 API 兼容性。
- **技术护城河（中等）**：插件系统、Front Matter Defaults、Incremental build 都是行业早期创新；但 Hugo/11ty 都在这些点上迎头赶上。

### 竞争风险
- **被 Hugo 替代（高风险）**：性能敏感 / 大型文档（万页+）/ 多语言用户必然流向 Hugo。
- **被 11ty 替代（中风险）**：前端/JS 栈团队若不锁定 GitHub Pages，会选 11ty（更轻量、更多模板引擎）。
- **被 Gatsby/Astro 替代（中风险）**：需要客户端交互（登录、评论、表单 SPA）的项目会流向前两者。
- **被 Notion/Obsidian Publish/Substack 替代（中等 + 渐进）**：纯写作者越来越倾向「连 git 都不想用」的全托管平台。

### 生态定位
Jekyll 在静态站生成器生态中的位置是**「最朴素、最长寿、最被托管平台官方支持的内容站引擎」**——它不追求性能/能力极限，而是追求「git push 就能上线」的极简哲学。13 年后仍是 GitHub Pages 的默认引擎，足以说明这种定位的韧性。

## 套利机会分析
- **信息差**：Jekyll 不是「被低估」的项目——它的价值已充分定价（GitHub Pages 引擎、51K stars、SSG 品类事实标准）。但作为「老牌稳定」项目的代表，对追求极简部署与 Markdown 优先的工作流仍是首选。
- **技术借鉴**：`Site#process` 线性管线 + 反射式 Plugin 发现 + Hooks 三维注册表 + Drops 沙箱 + Regenerator 增量构建 + Theme = Gem，这一整套设计模式可以**整套迁移**到任何「批量文档生成 / 插件化 CLI / 静态站工具」的新项目，是「插件化框架」的标杆实现。
- **生态位**：Jekyll 填补了「零运行时 + 极简心智 + 官方托管」三位一体的空白，13 年未被取代。
- **趋势判断**：已进入维护期（近 365 天 27 commit，dev_stage 标记为「低维护」），新功能增长停滞；但增长主要来自存量用户的稳定使用而非爆发新增，GitHub Pages 的引擎定位短期不会变。趋势是「在 GitHub Pages 默认引擎这个生态位上保持稳定，被 Hugo/11ty 蚕食边缘用户」。

## 风险与不足
- **构建性能瓶颈**：10K 页以上站点分钟级等待；Regenerator 增量只是缓解，没有根本性解决（Issue #380 长期痛点）。
- **「单页单输出」模型限制**：同一页内容如何用不同 layout 输出多格式（HTML/JSON/AMP/feed）是长期 open 议题（Issue #3041），API/feed 等场景需要插件绕路。
- **Ruby 生态的版本升级成本**：每次 Ruby 主版本升级都带来 gem 兼容性问题，新人需要懂 Ruby 才能贡献。
- **Liquid 模板引擎的双刃剑**：对设计师友好但灵活性差（无法做复杂条件/循环），高端用户会撞墙。
- **插件质量参差**：第三方插件是 Jekyll 力量源泉但也是最大的安全/稳定性风险来源——`safe` 模式只能挡一部分。
- **维护期陷阱**：近 30 天 0 commit、近 90 天仅 9 commit，新功能响应慢，社区贡献者可能流失到 11ty/Astro 等更活跃的 SSG。

## 行动建议
- **如果你要用它**：
  - ✅ 选它的场景：博客 / 项目文档 / 营销页 / 中小型内容站（< 1K 页）/ 想 git push 零运维上线。
  - ❌ 别选它的场景：万页+ 文档站（用 Hugo）/ 需要登录态/评论/表单（用 Gatsby/Astro）/ JS 栈团队（用 11ty）。
- **如果你要学它**：
  - 重点读 `lib/jekyll/site.rb`（构建管线）、`lib/jekyll/plugin.rb`（反射发现）、`lib/jekyll/hooks.rb`（三维注册表）、`lib/jekyll/drops/drop.rb`（沙箱）。
  - 读 `lib/site_template/` 和 `docs/_docs/plugins.md` 看「插件作者怎么上手」。
  - 看 `History.markdown` 2,998 次修改的演变，理解「17 年如何保持 API 稳定」。
- **如果你要 fork 它**：
  - 可以改进的方向：① 内置 i18n（取代 jekyll-polyglot 插件）② 多格式输出同源（解决 Issue #3041）③ ESM/TypeScript front matter 支持 ④ Incremental 真正按 page 粒度并行。
  - 风险：13 年的 API 兼容性是 Jekyll 最大的资产，fork 改了 API 就丢了生态。

## 知识入口

| 资源 | 链接 |
|------|------|
| DeepWiki | <https://deepwiki.com/jekyll/jekyll>（已收录，架构与设计哲学解读完整） |
| Zread.ai | 未收录 |
| 关联论文 | 无（SSG 为工程类项目，学术文献稀少） |
| 在线 Demo | <https://jekyllrb.com/docs>（Quickstart 即可在 30 秒内 `bundle exec jekyll serve` 本地起站） |

---

## 附：分阶段分析原始摘要

### Phase 1 — 网络分析
- **仓库基本数据**：Star 51,475 / Fork 10,283 / Watcher 1,399；Ruby 70.6% / Gherkin 23.1% / JavaScript 3.8%；MIT License；创建 2008-10-20，最近推送 2026-04-22；话题标签 ruby, jekyll, static-site-generator, blog-engine, markdown, liquid。
- **作者画像**：@jekyll 组织账号（13.5 年，54 公开仓库，1,269 粉丝），此 repo 投入权重高（排第 1，远超次席）；核心团队 + 1,245 位贡献者社区维护；Top 1 @parkr 占 27.9%。
- **社区热度**：大众热门（51K stars，GitHub Pages 官方引擎）；早期高速增长（27 天 200 star ≈ 7.4 star/天）；近期进入维护期（30 天 0 commit、90 天 9 commit）；不算被低估——SSG 品类事实标准之一，价值已充分定价。
- **生态网络**：上游依赖 GitHub Pages（官方默认引擎）；同类项目 Hugo/Hexo/Eleventy/Gatsby/Pelican/Octopress/Next.js。
- **官方文档洞察**：「Transform your plain text into static websites and blogs」；目标用户：不想折腾数据库/CMS 的内容创作者与开发者；差异化叙事：「No more databases, comment moderation, or pesky updates to install—just your content.」（零运行时）；设计哲学：「just your content」；构建管线 `reset → read → generate → render → write`。
- **关键 Issue 信号**：
  1. [#6948 Jekyll 4.0 Ideas](https://github.com/jekyll/jekyll/issues/6948) — 揭示 Jekyll 从 3.x 跨向 4.0 的核心设计张力（要不要全面重写渲染管线、是否引入插件签名、kramdown 默认配置如何取舍）
  2. [#3041 multiple formats per page](https://github.com/jekyll/jekyll/issues/3041) — 长期 open 议题：同一页内容如何用不同 layout 输出多格式，反映 Jekyll「单页单输出」模型在 API/feed 等场景下的局限性
  3. [#380 Incremental regeneration](https://github.com/jekyll/jekyll/issues/380) — 大站点构建性能痛点，催生了 `--incremental` 与 4.x 的部分增量方案

### Phase 2 — 元分析
- **代码规模**：28,103 行（不含空行/注释），Ruby 59.9% / Gherkin 16.3% / Sass 7.6% / YAML 5.5% / JavaScript 3.8% / HTML 3.4%；代码/注释比 1:0.74（注释 20,920 行，比例 74.4%，体现项目对开发者文档化的重视）；698 文件；Ruby gem 项目（无 package.json）。
- **开发节奏**：211.8 个月（17.6 年）；总 commit 11,872；近 30 天 0 commit / 90 天 9 commit / 365 天 27 commit；周末占比 23.8%，深夜占比 21.1%；开发阶段「低维护」，开发模式「职业项目」（团队 + 社区双轨）。
- **演化轨迹核心文件**（Top 10）：
  1. `History.markdown` — 2,998 次修改（自动生成的版本变更日志，不算核心逻辑）
  2. `lib/jekyll/site.rb` — 361 次修改（核心 Site 编排类，最热的真实代码热点）
  3. `jekyll.gemspec` — 295 次修改（gem 元数据/依赖声明）
  4. `History.txt` — 255 次修改（旧版 changelog）
  5. `lib/jekyll.rb` — 246 次修改（顶层入口/自动加载，插件机制与配置默认值）
  6. `Gemfile` — 230 次修改（依赖锁文件）
  7. `lib/jekyll/post.rb` — 181 次修改（文章/文档模型）
  8. `lib/jekyll/convertible.rb` — 177 次修改（统一 Liquid/YAML/Markdown 内容转换）
  9. `test/test_site.rb` — 174 次修改（Site 类的单元测试）
  10. `test/test_filters.rb` — 157 次修改（Liquid 过滤器测试）
- **演化轨迹热点目录**：lib/jekyll 3,846 / docs/_docs 1,197 / site/_docs 744 / site/docs 469 / site/_posts 347 / lib/site_template 315（一等公民脚手架）。
- **Commit 类型分布**（近 200 次采样）：Feature/Add 24 (12.0%) / Fix/Bug 24 (12.0%) / Refactor 0 (0.0%) / Docs 12 (6.0%) / Test 3 (1.5%) / Other 137 (68.5%）。feature/fix 几乎 1:1，refactor 0% 佐证架构已稳定；other 68.5% 主要来自 History.markdown 自动 bump。
- **月度 commit 节奏亮点**：2013-05 达 306 commit / 2014-05 史上最高 348 commit（GitHub Pages 强整合期） / 2016-01 反弹至 281 commit（3.0 启动期） / 2018-12 ~ 2019-01 v4.0 前后小高峰 / 2022 起断崖式下跌 / 2025-2026 月均 2-6 commit。
- **版本发布**：v4.4.1（160 个 tag，100 个 GitHub Release）；SemVer 严格；主线 v2.x（2012-2014）→ v3.x（2015-2019，3.0 引入相对路径）→ v4.x（2019 至今，4.0 引入 GitHub Pages 兼容性、加速构建）；4.5 仍待发。

### Phase 3 — 内容分析（架构与设计）
- **目录结构**：`lib/jekyll.rb` 顶层用 `autoload` 按需加载；`site.rb` 是唯一「大对象」承担构建编排中央调度；`plugin.rb` 是插件抽象根，Converter/Generator/Command/Hook 派生；`drops/` 单独成层是给 Liquid 模板一个「安全、只读、防无限递归」的视图；`utils/` 拆出跨平台/IO/编码工具。
- **关键设计决策**（10 条详见上文「关键设计决策」节）：Site 中央容器 + 显式线性管线 / Plugin.descendants 反射发现 / Hooks 三维注册表 / Render 三段式 / Regenerator 增量构建 / Configuration 三层合并 / Drops 模板沙箱 / Front Matter Defaults 路径 glob + 优先级 / safe 模式 + 插件白名单 / LiquidRenderer 模板 parse 缓存 + 渲染 stats。
- **代码质量评级**：代码[优秀]（13 年演化 + 显式 YARD 注释 + 自定义 RuboCop 规则）/ 文档[优秀]（40+ 篇 + Jekyll 自指构建）/ 测试[充分]（55 个 Minitest + 20+ Cucumber + benchmark + Earthly）/ CI/CD[完善]（7+ workflow + Dependabot + CodeQL + release-please）/ 错误处理[规范]（Errors 模块 + FatalException + strict_* 开关）。
- **质量检查清单**：✅ 测试（unit + E2E + fixtures + benchmark）✅ CI/CD（GitHub Actions + Earthly + Dependabot + CodeQL）✅ 文档（40+ 篇 + 自指）✅ 错误处理 ✅ linter（rubocop/ 自定义规则）✅ CHANGELOG ✅ LICENSE ✅ examples（3 个新站模板）✅ 依赖锁定（Gemfile.lock）✅ 自指 dogfooding ✅ Earthly 多架构多 Ruby 矩阵。
- **哲学总结**：Jekyll 的护城河不在性能（输 Hugo）也不在能力（输 Gatsby），而在「零运行时 + 极简心智 + 官方托管」三位一体——**克制即胜利**的工程哲学。
