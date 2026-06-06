#!/usr/bin/env bash
# reconcile-from-runner.sh —— 部署在 ali-demo（微信白名单机）上的 forced-command 接收脚本。
#
# 作用：GitHub Actions runner 连不上微信反代（IP 不在白名单），故 reconcile-wechat.yml
# 把「报告标题字典 + publish_history.jsonl + reconcile 三件套 .py」打成 tar 包经 SSH stdin
# 送到本机，由本脚本解包后在白名单网络里跑只读核对，把差异结果从 stdout 回传给 runner。
# 完全照搬现有 publish-from-runner.sh 的「tar 走 stdin、forced-command」模式。纯只读，不发任何东西。
#
# ── 一次性部署（在 ali-demo 上）─────────────────────────────────────────────
# 1) 放置脚本：把本文件放到 /opt/github-explorer/reconcile-from-runner.sh 并 chmod +x
# 2) 微信凭证：本脚本会 source 一个 env 文件拿 WECHAT_*（与发布同一套）。默认路径
#    /opt/github-explorer/wechat.env，可用环境变量 WECHAT_ENV_FILE 覆盖。该文件至少含：
#       WECHAT_APPID=...
#       WECHAT_APPSECRET=...
#       # ali-demo 若直连微信被白名单则无需下面两行；若本机也走反代则按需设置：
#       # WECHAT_API_BASE=https://wx.nightvoyager.top
#       # WECHAT_PROXY_TOKEN=...
# 3) 授权 key（二选一）：
#    (a) 独立 key（推荐，隔离发布）：新生成一对 key，把私钥放进 GitHub secret
#        ALI_DEMO_RECONCILE_KEY，公钥加到 ~/.ssh/authorized_keys 并锁 forced-command：
#          command="/opt/github-explorer/reconcile-from-runner.sh",no-port-forwarding,no-agent-forwarding,no-X11-forwarding,no-pty ssh-ed25519 AAAA...
#        然后把 reconcile-wechat.yml 里的 secrets.ALI_DEMO_SSH_KEY 换成 ALI_DEMO_RECONCILE_KEY。
#    (b) 复用发布 key：在你现有 publish 的 forced-command 脚本开头按 $SSH_ORIGINAL_COMMAND 分流——
#          以 "reconcile" 开头就 exec 本脚本，否则走原 publish 逻辑（保持向后兼容）。
#
# stdin : tar.gz，含 reconcile_wechat_publish.py / sync_wechat_status.py / _wechat_api.py /
#         publish_history.jsonl / h1.json
# argv  : 经 $SSH_ORIGINAL_COMMAND 传入，仅白名单解析 --min-confidence / --include-drafts
# stdout: 核对差异文本（回传 runner）
set -euo pipefail

WECHAT_ENV_FILE="${WECHAT_ENV_FILE:-/opt/github-explorer/wechat.env}"
PY="${PYTHON_BIN:-python3}"

# ── 白名单解析远端传来的参数（forced-command 安全：绝不 eval 任意串）──────────
MIN_CONF="medium"
INCLUDE_DRAFTS=0
# 优先用 SSH 注入的 SSH_ORIGINAL_COMMAND；本地直跑时退回 "$@"
read -r -a _args <<<"${SSH_ORIGINAL_COMMAND:-$*}"
i=0
while [[ $i -lt ${#_args[@]} ]]; do
  tok="${_args[$i]}"
  case "$tok" in
    reconcile) ;;  # 命令名占位，忽略
    --include-drafts) INCLUDE_DRAFTS=1 ;;
    --min-confidence)
      i=$((i+1)); v="${_args[$i]:-}"
      case "$v" in high|medium|low) MIN_CONF="$v" ;; *) echo "ERR: 非法 min-confidence: $v" >&2; exit 2 ;; esac
      ;;
    --min-confidence=*)
      v="${tok#*=}"
      case "$v" in high|medium|low) MIN_CONF="$v" ;; *) echo "ERR: 非法 min-confidence: $v" >&2; exit 2 ;; esac
      ;;
    *) echo "ERR: 不允许的参数: $tok（forced-command 仅接受 --min-confidence/--include-drafts）" >&2; exit 2 ;;
  esac
  i=$((i+1))
done

# ── 凭证 ────────────────────────────────────────────────────────────────────
if [[ -f "$WECHAT_ENV_FILE" ]]; then
  set -a; # shellcheck disable=SC1090
  source "$WECHAT_ENV_FILE"; set +a
fi
: "${WECHAT_APPID:?缺 WECHAT_APPID（检查 $WECHAT_ENV_FILE 或 forced-command 环境）}"
: "${WECHAT_APPSECRET:?缺 WECHAT_APPSECRET}"

# ── 解包 stdin → 临时工作目录 ───────────────────────────────────────────────
workdir="$(mktemp -d)"
trap 'rm -rf "$workdir"' EXIT
tar xzf - -C "$workdir"

need() { [[ -f "$workdir/$1" ]] || { echo "ERR: payload 缺 $1" >&2; exit 3; }; }
need reconcile_wechat_publish.py
need sync_wechat_status.py
need _wechat_api.py
need publish_history.jsonl
need h1.json

# ── 跑只读核对 ──────────────────────────────────────────────────────────────
cd "$workdir"
extra=()
[[ $INCLUDE_DRAFTS -eq 1 ]] && extra+=(--include-drafts)
exec "$PY" reconcile_wechat_publish.py \
  --min-confidence "$MIN_CONF" \
  --h1-json h1.json \
  --publish-jsonl publish_history.jsonl \
  "${extra[@]}"
