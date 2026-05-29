# Vibe 网络分析笔记

## 仓库基本信息
- **仓库**: https://github.com/lynaghk/vibe
- **描述**: Easy Linux virtual machine on MacOS to sandbox LLM agents
- **Stars**: 833 | **Forks**: 44 | **Watchers**: 4
- **Issues**: 2 (open) | **PRs**: 0
- **License**: MIT
- **主语言**: Rust (45,857 bytes), Shell (2,496 bytes)
- **创建时间**: 2026-01-28
- **最后推送**: 2026-03-21
- **是否归档**: 否 | **是否 Fork**: 否
- **磁盘使用**: 115 KB

## 作者信息
- **用户名**: lynaghk (Kevin Lynagh)
- **公司**: Keming Labs
- **位置**: Amsterdam
- **博客**: https://kevinlynagh.com
- **公开仓库数**: 103
- **粉丝数**: 686
- **注册时间**: 2009-11-02 (16年+)

## 贡献者
| 用户 | 贡献数 |
|------|--------|
| lynaghk | 78 |
| mattiapv | 3 |
| artemy | 1 |
| ivarref | 1 |
| jtdowney | 1 |

## 热门 Issues
| # | 标题 | 评论 | 状态 |
|---|------|------|------|
| 23 | Doesn't launch | 8 | open |
| 5 | Unable to send prompt answer | 5 | closed |
| 15 | Prevent write to mounted .vibe folder | 4 | closed |
| 12 | Add --ca-cert flag for custom CA certificate support | 4 | closed |
| 8 | Resize disk on initial startup or when spinning up VM | 4 | closed |

## 社区讨论
- Lobsters: https://lobste.rs/s/6ifznf/vibe_easy_vm_sandboxes_for_llm_agents_on
- Hacker News: https://news.ycombinator.com/item?id=46852690
- 作者博客: https://kevinlynagh.com/newsletter/2026_02_01_vibe/

## 竞品/替代方案
- **VibeBox** (robcholz/vibebox): per-project micro-VM sandbox, Apple Virtualization Framework
- **Agent Safehouse**: macOS-native sandbox-exec policy generator
- **Era**: microVM-based sandboxing for AI code
- **Vibekit**: full-featured sandbox with LLM provider integration
- **Lima**: Linux VMs on Mac (作者尝试后因诸多问题放弃)
- **Tart**: macOS VM runner (构建失败)
- **OrbStack**: 容器为主，单VM，无法隔离整个磁盘
- **QEMU**: 作者最初原型，因 9p 性能问题放弃
- **Sandboxtron**: 作者自己的 sandbox-exec wrapper，因 sandbox 嵌套限制放弃
