# Research Center 发布说明

Research Center 现在作为博客子路径发布：

- 线上路径：`/research/`
- 源码路径：`static/research/`
- 发布方式：跟随主站 Hugo + Cloudflare Pages 一起构建发布

## 不再使用

- 独立 `research-hub` 仓库
- 独立 GitHub Pages 部署
- 单独域名/子域名部署流程

## 实际发布步骤

1. 在主仓库修改 `static/research/*`
2. 本地预览：`hugo server -D`
3. 检查 `http://localhost:1313/research/`
4. 提交并推送主仓库
5. 等待主站发布完成

## 常见问题

- 页面 404：确认文件在 `static/research/` 下且路径以 `/research/` 开头。
- 首页没有新研报：确认 `static/research/data/reports.json` 已加入对应条目。
