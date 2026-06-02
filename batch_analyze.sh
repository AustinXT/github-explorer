#!/usr/bin/env bash
#
# batch_analyze.sh - 批量并发调用 claude 分析 GitHub 仓库
#
# 用法: ./batch_analyze.sh [repos_file] [start_line] [end_line] [concurrency]
#   repos_file   - 仓库列表文件，默认 src/analysis_report/repos.md
#   start_line   - 起始行号（含），默认 1
#   end_line     - 结束行号（含），默认处理到文件末尾（0=不限）
#   concurrency  - 并发数，默认 5
#
# 示例:
#   ./batch_analyze.sh                              # 全部，5 并发
#   ./batch_analyze.sh repos.md 10 20               # 第 10-20 行，5 并发
#   ./batch_analyze.sh repos.md 1 0 8               # 全部，8 并发

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPOS_FILE="${1:-$SCRIPT_DIR/src/analysis_report/repos.md}"
START_LINE="${2:-1}"
END_LINE="${3:-0}"        # 0 表示不限制
MAX_JOBS="${4:-5}"

OUTPUT_DIR="$SCRIPT_DIR/src/analysis_report"
TMP_DIR="$SCRIPT_DIR/tmp"
LOG_DIR="$TMP_DIR/logs"
STAT_DIR="$TMP_DIR/.stats_$$"

mkdir -p "$OUTPUT_DIR" "$TMP_DIR" "$LOG_DIR" "$STAT_DIR"
trap 'rm -rf "$STAT_DIR"' EXIT

# ── 解析 URL 列表 ──────────────────────────────────────────────
urls=()
line_num=0
while IFS= read -r line || [[ -n "$line" ]]; do
    line_num=$((line_num + 1))
    [[ $line_num -lt $START_LINE ]] && continue
    [[ $END_LINE -gt 0 && $line_num -gt $END_LINE ]] && break

    line="$(echo "$line" | xargs)"  # trim
    if [[ "$line" =~ ^https://github\.com/[^/]+/[^/]+ ]]; then
        urls+=("$line")
    fi
done < "$REPOS_FILE"

TOTAL=${#urls[@]}
if [[ $TOTAL -eq 0 ]]; then
    echo "❌ 未从 $REPOS_FILE 中解析到任何 GitHub URL"
    exit 1
fi

echo "=========================================="
echo " 批量仓库分析"
echo " 仓库列表: $REPOS_FILE"
echo " 待处理数: $TOTAL"
echo " 并  发  数: $MAX_JOBS"
echo " 输出目录: $OUTPUT_DIR"
echo " 临时目录: $TMP_DIR"
echo "=========================================="
echo ""

# ── 原子计数器（基于文件，进程安全）─────────────────────────────
counter_file="$STAT_DIR/done"
echo "0" > "$counter_file"

inc_done() {
    local lockdir="$counter_file.lock"
    while ! mkdir "$lockdir" 2>/dev/null; do :; done
    echo $(( $(cat "$counter_file") + 1 )) > "$counter_file"
    rmdir "$lockdir"
}
get_done() {
    cat "$counter_file"
}

# ── 单个仓库处理函数 ────────────────────────────────────────────
analyze_one() {
    local idx="$1" url="$2"

    local path="${url#https://github.com/}"
    local username repo_name
    username="$(echo "$path" | cut -d'/' -f1)"
    repo_name="$(echo "$path" | cut -d'/' -f2)"

    local output_file="$OUTPUT_DIR/${username}_${repo_name}.md"
    local log_file="$LOG_DIR/${username}_${repo_name}.log"
    local status_file="$STAT_DIR/${idx}"

    # 跳过已存在的报告
    if [[ -f "$output_file" ]]; then
        echo "⏭  [$idx/$TOTAL] $username/$repo_name — 报告已存在，跳过"
        echo "skipped" > "$status_file"
        inc_done
        return 0
    fi

    echo "⏳ [$idx/$TOTAL] $username/$repo_name — 开始分析..."
    local start_time
    start_time=$(date +%s)

    local prompt="/repo-miner $url ，中间过程文件输出到 $TMP_DIR ，最终分析报告输出到 $output_file"

    if claude -p "$prompt" \
        --dangerously-skip-permissions \
        > "$log_file" 2>&1; then
        local end_time elapsed
        end_time=$(date +%s)
        elapsed=$((end_time - start_time))

        if [[ -f "$output_file" ]]; then
            echo "✅ [$idx/$TOTAL] $username/$repo_name — 完成 (${elapsed}s)"
            echo "success" > "$status_file"
        else
            echo "⚠️  [$idx/$TOTAL] $username/$repo_name — 无输出文件 (${elapsed}s) 日志: $log_file"
            echo "failed:$url (无输出文件)" > "$status_file"
        fi
    else
        local end_time elapsed
        end_time=$(date +%s)
        elapsed=$((end_time - start_time))
        echo "❌ [$idx/$TOTAL] $username/$repo_name — 失败 (${elapsed}s) 日志: $log_file"
        echo "failed:$url" > "$status_file"
    fi

    inc_done
}

# ── 并发调度 + 进度监控 ─────────────────────────────────────────

# 启动进度监控（后台）
(
    while true; do
        done_count=$(get_done)
        pct=$((done_count * 100 / TOTAL))
        bar_len=$((pct / 2))
        bar=""
        for ((b=0; b<bar_len; b++)); do bar+="█"; done
        printf "\r  📊 进度: [%-50s] %3d%% (%d/%d)  并发: %d" "$bar" "$pct" "$done_count" "$TOTAL" "$MAX_JOBS"
        [[ $done_count -ge $TOTAL ]] && break
        sleep 2
    done
    echo ""
) &
MONITOR_PID=$!

# 并发执行，使用 fd 作为信号量
FIFO="$STAT_DIR/fifo"
mkfifo "$FIFO"
exec 6<>"$FIFO"

# 预填充 MAX_JOBS 个令牌
for ((t=0; t<MAX_JOBS; t++)); do
    echo >&6
done

for i in "${!urls[@]}"; do
    idx=$((i + 1))
    url="${urls[$i]}"

    # 获取一个令牌（阻塞直到有空闲槽位）
    read -u 6

    # 后台执行，完成后归还令牌
    (
        analyze_one "$idx" "$url"
        echo >&6
    ) &
done

# 等待所有后台任务完成
wait

# 关闭信号量 fd
exec 6>&-
rm -f "$FIFO"

# 停止进度监控
kill "$MONITOR_PID" 2>/dev/null || true
wait "$MONITOR_PID" 2>/dev/null || true

# ── 汇总统计 ────────────────────────────────────────────────────
success=0
failed=0
skipped=0
failed_list=()

for sf in "$STAT_DIR"/*; do
    [[ "$(basename "$sf")" == "done" || "$(basename "$sf")" == "fifo" ]] && continue
    [[ ! -f "$sf" ]] && continue
    content="$(cat "$sf")"
    case "$content" in
        success)   success=$((success + 1)) ;;
        skipped)   skipped=$((skipped + 1)) ;;
        failed:*)  failed=$((failed + 1)); failed_list+=("${content#failed:}") ;;
    esac
done

echo ""
echo "=========================================="
echo " 执行完毕"
echo "  ✅ 成功: $success"
echo "  ⏭  跳过: $skipped"
echo "  ❌ 失败: $failed"
echo "  📊 合计: $TOTAL"
echo "=========================================="

if [[ ${#failed_list[@]} -gt 0 ]]; then
    echo ""
    echo "失败列表:"
    for item in "${failed_list[@]}"; do
        echo "  - $item"
    done
fi
