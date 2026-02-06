#!/bin/bash
set -euo pipefail

echo "Currency Dashboard 已迁移到主博客仓库，不再单独部署。"
echo "请在仓库根目录执行："
echo "  hugo server -D    # 本地预览"
echo "  git add . && git commit -m \"...\" && git push"
echo "发布由主站 Cloudflare Pages 流程统一完成。"
