# TapXWorld/ChinaTextbook 网络分析报告

## 仓库基本数据
- Star / Fork / Watcher: 66,002 / 14,719 / 559
- 语言: Roff (100%) — 实质为 PDF 文件存储仓库，GitHub 将 PDF 中的排版标记语言识别为 Roff
- License: 无（未声明开源许可证）
- 创建时间: 2020-01-05 | 最近推送: 2025-10-18 | 最近更新: 2026-03-21
- 话题标签: 无（作者未设置 topic 标签）
- 已归档: 否 | 是Fork: 否
- 磁盘占用: 约 42.5 GB（GitHub API 报告 43,543,927 KB）
- 主页: 无
- Open Issues: 98 | Open PRs: 11
- 社区健康度: 28%（无 License、无 Contributing 指南、无 Code of Conduct）

## 作者画像
- 姓名/ID: TapXWorld | 公司: 未披露 | 位置: Tokyo（东京）
- 粉丝: 1,327 | 公开仓库: 15 | 账号年龄: 约 13 年（2013-01-23 注册）
- Bio: "We can rule the world"
- 此 repo 投入权重: **中**（在最近活跃仓库中排第 6，近期更多在维护 tapxworld.github.io、jizhangben 等项目；但 ChinaTextbook 是其绝对代表作，star 数量碾压其他所有项目）
- 作者类型: **独立开发者**（无公司信息，个人项目为主，仓库涵盖安全工具 osep_tools/oswe_tools、区块链 blocksec-lab、快速部署环境 fastDeployEnvirment 等，暗示具备安全工程 / DevOps 背景）
- 贡献集中度: **双人主导**（TESTPERSONAL 贡献 76 次 commits 占 86%，TapXWorld 本人 11 次占 12.5%，keminshu 1 次占 1%。TESTPERSONAL 是一个无公开仓库的神秘账号，极可能是作者的小号或密切合作者）
- 背景推断: 作者为居住在东京的华人开发者，具备安全工程和 DevOps 背景（oswe/osep 工具），ChinaTextbook 项目初衷是为海外华人子女提供教育资源。配套开发了 Go 语言文件合并工具（ChinaTextbook-tools，348 star），展现了工程化能力。

## 社区热度
- 热度级别: **大众热门**（66,000+ star，在 GitHub 全站排名极高）
- 增长模式: **爆发型**
  - 2020-01 至 2025-04：长期低调维护，star 缓慢积累（约 5 年内数千 star）
  - 2025-05：突然爆火，单日最高 6,000+ star，被 Trending Repos 多次推荐
  - 2025-05-19 推文记录：总 star 25,334，24h 增长 2,027
  - 2025-05-21 推文记录：总 star 已达约 13,381 后迅速升至 31,248（周增 6,990）
  - 2025-06 至 2025-11：持续每日 300+ star 增长
  - 截至 2026-03-22：66,002 star，增长仍在持续
- 近期趋势: 最近 10 个月从约 30,000 增长到 66,000，增长约 36,000 star，月均约 3,600 star
- 套利判断: **否，已被充分发现**。项目已经处于高度曝光状态，不属于被低估资源。但其资源价值本身（完整的中国 K-12+大学教材库）具备长尾使用价值。

## 生态网络
- 上游依赖/数据来源:
  - [国家中小学智慧教育平台](https://basic.smartedu.cn/) — 教材 PDF 的原始来源
  - 各出版社（人教版、苏教版、北师大版、北京版等 8 种版本）
- 配套工具:
  - [TapXWorld/ChinaTextbook-tools](https://github.com/TapXWorld/ChinaTextbook-tools)（348 star）— 作者自建的文件合并/分割工具（Go 语言）
  - [happycola233/tchMaterial-parser](https://github.com/happycola233/tchMaterial-parser)（4,748 star）— 从智慧教育平台直接下载电子课本的工具，README 中推荐
  - [hantang/smartedu-dl-go](https://github.com/hantang/smartedu-dl-go)（22 star）— 多平台智慧教育平台资源下载工具
  - [amakerlife/tchMaterial-downloader](https://github.com/amakerlife/tchMaterial-downloader) — 免登录下载正版电子教材
- 同类项目:
  - [zgc/TapXWorld-ChinaTextbook](https://github.com/zgc/TapXWorld-ChinaTextbook) — 镜像/Fork 副本
  - [jiang97h/Chinese-textbooks](https://github.com/jiang97h/Chinese-textbooks) — 另一个电子教材集合
  - SourceForge 上存在镜像: [ChinaTextbook on SourceForge](https://sourceforge.net/projects/chinatextbook.mirror/)
- 社区:
  - Telegram 群组: https://t.me/+1V6WjEq8WEM4MDM1

## 官方文档洞察
- 项目无独立官网（homepageUrl 为空）
- README 即为全部文档，结构清晰：按学段（小学/初中/高中/大学）和学科（数学为主）组织 PDF 链接目录
- 项目声明: "资源来自国家中小学智慧教育平台，仅限个人学习与研究，版权归属官方出版社"
- 项目初衷有两个: (1) 对抗某些平台将免费资源加水印付费售卖的行为；(2) 让海外华人的孩子继续了解国内教育
- 外部深度报道:
  - [CSDN 博客详细分析](https://blog.csdn.net/horses/article/details/149750457): 介绍了项目覆盖范围（小初高大全学段、8 种出版社版本）、高清无水印特点、增长数据
  - [小众软件论坛讨论](https://meta.appinn.net/t/topic/71341): 用户认可资源覆盖面，但对 mergePDFs.exe 存在安全疑虑（VirusTotal 11/73 引擎报毒，社区认为大概率是误报）
  - [搜狐报道](https://www.sohu.com/a/894790256_122354589): 标题强调 "41.53 GB 中国中小学大学 PDF 教材免费获取"
  - [博客园"GitHub 热点速览"收录](https://www.cnblogs.com/xueweihan/p/18921524)

## 竞品清单
| 项目 | Star | 定位 | 差异 |
|------|------|------|------|
| [国家中小学智慧教育平台](https://basic.smartedu.cn/) | 官方 | 官方在线平台，需登录，在线浏览 | 官方源头，但不提供直接 PDF 下载 |
| [happycola233/tchMaterial-parser](https://github.com/happycola233/tchMaterial-parser) | 4,748 | 从官方平台下载 PDF 的工具 | 工具而非资源库，需自行下载 |
| [hantang/smartedu-dl-go](https://github.com/hantang/smartedu-dl-go) | 22 | 多平台下载工具（支持 PDF/课件/音视频） | 功能更全但用户量小 |
| 各网盘搬运 | N/A | 百度网盘/阿里云盘上的教材合集 | 可能带水印、可能收费、随时失效 |

ChinaTextbook 的核心竞争力在于: **一站式、Git 版本管理、无水印、免费、长期可用**。它不是工具，而是已经整理好的资源库，降低了用户门槛。

## 关键 Issue 信号
| # | 标题 | 评论数 | 状态 | 信号 |
|---|------|--------|------|------|
| [#35](https://github.com/TapXWorld/ChinaTextbook/issues/35) | 请求安全工程师关于 mergePDFs.exe 的审计报告 | 18 | closed | **安全信任危机**：社区对二进制合并工具的安全性提出质疑 |
| [#3](https://github.com/TapXWorld/ChinaTextbook/issues/3) | 提供国家中小学智慧平台地址 | 10 | closed | 社区互助，指向官方源 |
| [#42](https://github.com/TapXWorld/ChinaTextbook/issues/42) | 国家中小学智慧教育平台提供了全部教材 | 9 | open | 有人质疑项目必要性（官方已有免费渠道） |
| [#38](https://github.com/TapXWorld/ChinaTextbook/issues/38) | 建议增加收录旧版人教版高中数学选修 | 9 | open | 社区需求：旧版教材有怀旧/对比价值 |
| [#194](https://github.com/TapXWorld/ChinaTextbook/issues/194) | 2024版新课本[无广] | 8 | closed | 社区期待及时更新最新版教材 |
| [#4](https://github.com/TapXWorld/ChinaTextbook/issues/4) | 人教社毒教材 | 8 | closed | 项目与"毒教材"舆论事件关联，推动了早期关注 |
| [#64](https://github.com/TapXWorld/ChinaTextbook/issues/64) | 版权不会有问题吗 | 6 | closed | **版权风险**：社区对项目合法性的持续担忧 |
| [#149](https://github.com/TapXWorld/ChinaTextbook/issues/149) | 不是眼热别人卖得钱吧 | 6 | closed | 有人质疑项目动机 |

**Issue 信号总结**: 项目面临两大核心争议 — (1) 版权合法性风险；(2) 合并工具的安全信任问题。社区需求集中在旧版教材收录和及时更新新版教材。

## 知识入口
- DeepWiki: [https://deepwiki.com/TapXWorld/ChinaTextbook](https://deepwiki.com/TapXWorld/ChinaTextbook) — **已收录**
- Zread.ai: **未收录**（页面返回 "We couldn't find a repo match"）
- 关联论文: 无（这是资源型仓库，非研究项目）
- 在线 Demo: 无（纯 PDF 文件存储，无交互式应用）
- Telegram 社区: https://t.me/+1V6WjEq8WEM4MDM1

## 项目展示素材
README 中的展示性素材较少，项目本身为纯 PDF 资源库：

- **Star History 图表**: `https://api.star-history.com/svg?repos=TapXWorld/ChinaTextbook&type=Date` — 展示了经典的"爆发式增长"曲线
- **支付宝捐赠二维码**: `https://raw.githubusercontent.com/TapXWorld/ChinaTextbook/master/.cache/support-alipay.png` — 作者的捐赠收款码

README 主体内容为各学段教材的 PDF 链接目录（小学数学、初中数学、高中数学、大学数学），无其他展示性截图或视频。

## 快速判断
- **是否值得深入**: **有条件** — 作为教育资源库具有极高实用价值（完整的中国 K-12+大学教材 PDF），但存在版权风险且技术含量较低（本质是 PDF 文件的 Git 托管）。适合作为"资源发现"类推荐，不适合作为技术项目深入分析。
- **初步定位**: 中国教育资源数字化存档项目，面向海外华人家庭和教育资源匮乏地区，提供免费无水印的全学段 PDF 教材。属于"资源型仓库"而非"代码型仓库"。
- **作者可信度**: **中等** — 账号年龄 13 年，有安全工程背景（oswe/osep 工具），项目初衷合理（反对付费倒卖免费资源、服务海外华人）。但主要贡献者使用疑似小号（TESTPERSONAL），且合并工具引发过安全争议。无 License 声明是一个明显疏漏。
- **竞品格局**: **事实上的垄断** — 在"已整理好的中国教材 PDF 资源库"这一细分领域，ChinaTextbook 以 66,000 star 远超一切替代品。竞品主要是下载工具（需用户自行操作），而非现成的资源库。官方智慧教育平台虽免费但需登录且不便于批量获取。
