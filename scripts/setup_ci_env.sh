#!/usr/bin/env bash
# 在 GitHub Actions runner 上准备 repo-miner / md2wechat 跑得起来需要的全部依赖。
# 假定 runs-on: ubuntu-latest。
set -euo pipefail

log() { printf '\033[1;36m[setup]\033[0m %s\n' "$*"; }

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

log "1/5 安装 apt 依赖：gh, jq, tokei"
if ! command -v gh >/dev/null 2>&1; then
    # ubuntu-latest 已自带 gh，这里只是兜底
    sudo apt-get update -qq
    sudo apt-get install -y -qq gh jq
fi
command -v jq >/dev/null || sudo apt-get install -y -qq jq

if ! command -v tokei >/dev/null 2>&1; then
    log "  安装 tokei (cargo binstall)"
    if command -v cargo >/dev/null 2>&1; then
        cargo install tokei --quiet || true
    else
        # 用预编译包，避免编译耗时
        TOKEI_VER="12.1.2"
        curl -sSL "https://github.com/XAMPPRocky/tokei/releases/download/v${TOKEI_VER}/tokei-x86_64-unknown-linux-gnu.tar.gz" \
            | sudo tar -xz -C /usr/local/bin tokei
    fi
fi

log "2/5 安装 Node 和 Claude Code CLI"
if ! command -v claude >/dev/null 2>&1; then
    npm install -g @anthropic-ai/claude-code
fi
claude --version

log "3/5 注入 vendored skills 到 ~/.claude/skills/"
mkdir -p ~/.claude/skills
for skill in repo-miner md2wechat; do
    src="$REPO_ROOT/ci/skills/$skill"
    if [[ ! -d "$src" ]]; then
        echo "ERR: 缺少 vendor skill $src，请先 cp -RL .claude/skills/$skill ci/skills/" >&2
        exit 1
    fi
    rm -rf "$HOME/.claude/skills/$skill"
    cp -r "$src" "$HOME/.claude/skills/$skill"
    log "  ✓ $skill -> $HOME/.claude/skills/$skill"
done

log "4/5 校验 .env 必需变量"
# 推理后端默认走 Minimax，MINIMAX_API_KEY 必填
if [[ -z "${MINIMAX_API_KEY:-}" && -z "${ANTHROPIC_API_KEY:-}" ]]; then
    echo "ERR: MINIMAX_API_KEY 未设置（且无 ANTHROPIC_API_KEY 应急降级），无法跑 skill" >&2
    exit 1
fi
if [[ -z "${MINIMAX_API_KEY:-}" ]]; then
    echo "WARN: MINIMAX_API_KEY 未设置，将走 Anthropic 应急通道" >&2
fi

# 微信发布凭证
required=(WECHAT_APPID WECHAT_APPSECRET)
for var in "${required[@]}"; do
    if [[ -z "${!var:-}" ]]; then
        echo "WARN: $var 未设置，md2wechat 发布步骤将失败" >&2
    fi
done

log "5/5 准备运行时目录"
mkdir -p "$REPO_ROOT/notes" "$REPO_ROOT/tmp/logs" "$REPO_ROOT/src/analysis_report"

log "环境初始化完成"
