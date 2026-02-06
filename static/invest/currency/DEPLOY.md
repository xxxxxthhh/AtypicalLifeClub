# Currency Dashboard 发布说明

Currency Dashboard 现在作为博客子路径发布：

- 线上路径：`/invest/currency/`
- 源码路径：`static/invest/currency/`
- 发布方式：跟随主站 Hugo + Cloudflare Pages 构建

## 不再使用

- 独立 `currency-dashboard` 仓库
- 独立 GitHub Pages 发布流程
- 独立部署脚本创建新仓库

## 实际发布步骤

1. 修改 `static/invest/currency/*`
2. 本地运行 `hugo server -D` 预览
3. 检查 `http://localhost:1313/invest/currency/`
4. 提交并推送主仓库
5. 等待主站自动发布
