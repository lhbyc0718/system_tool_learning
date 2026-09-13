#!/usr/bin/env bash
set -e
URL="http://127.0.0.1:8000/packages.json"

# 获取数据并用 jq 筛选、排序，生成临时 JSON
curl -fsS "$URL" | jq '
  map(select(.status == "active" and .downloads >= 100))
  | sort_by(-.downloads, .name)
  | { title: "Active Packages Report",
      table: [.[] | {name, version, downloads}] }
' > summary.json

# 从 JSON 生成 Markdown 表格
jq -r '
  "## " + .title + "\n",
  "| Name | Version | Downloads |",
  "|------|---------|-----------|",
  (.table[] | "| " + .name + " | " + .version + " | " + (.downloads|tostring) + " |")
' summary.json > summary.md

# 清理临时文件
rm summary.json
