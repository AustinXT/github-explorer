#!/usr/bin/env bash
# reconcile-from-runner.sh —— 部署在 ali-demo（微信白名单机）上的 forced-command 接收脚本。
#
# 作用：GitHub Actions runner 连不上微信反代——不是 IP 白名单问题，而是阿里云对 Azure/GitHub
# runner 出口 IP 段在网络层对 :443 做 TCP RESET（见 commit a73d635，nginx 一条日志都没有）。
# 22/SSH 存活，故 reconcile-wechat.yml 把「报告标题字典 + publish_history.jsonl + reconcile
# 三件套 .py」打成 tar 包经 SSH stdin 送到本机，由本脚本解包后在白名单网络里跑核对。
# 与 publish-from-runner.sh 同构：stderr=诊断日志，stdout=回传给 runner 的 publish_history.jsonl。
#
# 契约（与发布链路一致）：
#   stdin : tar.gz，含 reconcile_wechat_publish.py / sync_wechat_status.py / _wechat_api.py /
#           publish_history.jsonl / h1.json
#   argv  : 经 $SSH_ORIGINAL_COMMAND 传入，仅白名单解析
#           --min-confidence / --include-drafts / --apply / --ci-run-id <digits>
#   stderr: 核对差异 / 进度日志（runner 落 reconcile.log）
#   stdout: （可能被 --apply 翻正过的）publish_history.jsonl 全文 —— runner 据此 git diff/commit。
#           dry-run（无 --apply）时内容不变 → runner 无 diff → 不 commit。
#
# ── 一次性部署（在 ali-demo 上，已采用「复用发布 key + dispatch」方案）─────────
# 复用现有发布链路，无需新 key / 新 GitHub secret（reconcile-wechat.yml 用 ALI_DEMO_SSH_KEY）：
# 1) 放置脚本：本文件 scp 到 /opt/wx-publish/reconcile-from-runner.sh（与 publish-from-runner.sh
#    同目录，独立于 git checkout，不受 publish 的 `git reset --hard` 影响）并 chmod +x。
# 2) 微信凭证：复用发布同一份 /root/.wx-publish.env（仅 WECHAT_APPID / WECHAT_APPSECRET；
#    本机直连 api.weixin.qq.com 即在白名单内，不设 WECHAT_API_BASE / WECHAT_PROXY_TOKEN）。
# 3) dispatch：在 /opt/wx-publish/publish-from-runner.sh 的 `set -euo pipefail` 之后插一段——
#    $SSH_ORIGINAL_COMMAND 以 "reconcile" 开头则 exec 本脚本，否则照走发布逻辑：
#       if [[ "${SSH_ORIGINAL_COMMAND:-}" == reconcile* ]]; then
#         exec env WECHAT_ENV_FILE=/root/.wx-publish.env /opt/wx-publish/reconcile-from-runner.sh
#       fi
#    发布步骤 ssh 不带远端命令 → SSH_ORIGINAL_COMMAND 为空 → 走发布，向后兼容。
# 备选（未采用）：独立 key — 私钥进 secret ALI_DEMO_RECONCILE_KEY、公钥单独锁 forced-command 到
#    本脚本；reconcile-wechat.yml 会优先用它。隔离更彻底，但要多管一把 key。
#
# 注：本脚本用 :?（必需变量）+ 参数白名单做显式校验，不依赖 set -u；且 set -u 在老 bash(3.2)
# 下对数组元素访问有误报，故只开 pipefail，保证跨 bash 版本稳健。
set -o pipefail

WECHAT_ENV_FILE="${WECHAT_ENV_FILE:-/root/.wx-publish.env}"
PY="${PYTHON_BIN:-python3}"

# ── 白名单解析远端传来的参数（forced-command 安全：绝不 eval 任意串）──────────
MIN_CONF="medium"
INCLUDE_DRAFTS=0
APPLY=0
CI_RUN_ID=""
# 优先用 SSH 注入的 SSH_ORIGINAL_COMMAND；本地直跑时退回 "$@"
read -r -a _args <<<"${SSH_ORIGINAL_COMMAND:-$*}"
i=0
while [[ $i -lt ${#_args[@]} ]]; do
  tok="${_args[$i]}"
  case "$tok" in
    reconcile) ;;  # 命令名占位，忽略
    --include-drafts) INCLUDE_DRAFTS=1 ;;
    --apply) APPLY=1 ;;
    --min-confidence)
      i=$((i+1)); v="${_args[$i]:-}"
      case "$v" in high|medium|low) MIN_CONF="$v" ;; *) echo "ERR: 非法 min-confidence: $v" >&2; exit 2 ;; esac
      ;;
    --min-confidence=*)
      v="${tok#*=}"
      case "$v" in high|medium|low) MIN_CONF="$v" ;; *) echo "ERR: 非法 min-confidence: $v" >&2; exit 2 ;; esac
      ;;
    --ci-run-id)
      i=$((i+1)); v="${_args[$i]:-}"
      case "$v" in ''|*[!0-9]*) echo "ERR: 非法 ci-run-id（仅数字）: $v" >&2; exit 2 ;; *) CI_RUN_ID="$v" ;; esac
      ;;
    --ci-run-id=*)
      v="${tok#*=}"
      case "$v" in ''|*[!0-9]*) echo "ERR: 非法 ci-run-id（仅数字）: $v" >&2; exit 2 ;; *) CI_RUN_ID="$v" ;; esac
      ;;
    *) echo "ERR: 不允许的参数: $tok（forced-command 仅接受 --min-confidence/--include-drafts/--apply/--ci-run-id）" >&2; exit 2 ;;
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

# ── 跑核对（诊断 → stderr）──────────────────────────────────────────────────
cd "$workdir"
extra=()
[[ $INCLUDE_DRAFTS -eq 1 ]] && extra+=(--include-drafts)
[[ $APPLY -eq 1 ]] && extra+=(--apply)
[[ -n "$CI_RUN_ID" ]] && extra+=(--ci-run-id "$CI_RUN_ID")

if ! "$PY" reconcile_wechat_publish.py \
    --min-confidence "$MIN_CONF" \
    --h1-json h1.json \
    --publish-jsonl publish_history.jsonl \
    ${extra[@]+"${extra[@]}"} >&2; then  # 空数组安全展开（兼容 bash 3.2 的 set -u）
  echo "ERR: reconcile_wechat_publish.py 执行失败" >&2
  exit 4
fi

# ── 回传（可能被 --apply 翻正过的）publish_history.jsonl → stdout ────────────
# dry-run 时内容与 runner 送来的一致 → runner git diff 为空 → 不 commit。
cat publish_history.jsonl
