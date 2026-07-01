# Research Center 发布说明

Research Center 现在作为博客子路径发布：

- 线上路径：`/invest/research/`
- 源码路径：`static/invest/research/`
- 发布方式：跟随主站 Hugo + Cloudflare Pages 一起构建发布

## 不再使用

- 独立 `research-hub` 仓库
- 独立 GitHub Pages 部署
- 单独域名/子域名部署流程

## 实际发布步骤

1. 在主仓库修改 `static/invest/research/*`
2. 运行研究模块校验：
   - `python3 static/invest/research/validate_reports.py`
   - `python3 static/invest/research/validate_coverage_map.py`
3. 对 full-cycle 重跑、版本链调整或大批量新增报告，额外运行独立发布契约检查：
   - `python3 /Users/kyx/.codex/skills/company-research-publishing/scripts/check_research_package.py static/invest/research`
4. 本地预览：`hugo server -D`
5. 检查 `http://localhost:1313/invest/research/`、`/invest/research/coverage-map.html` 和目标详情页
6. 提交并推送主仓库
7. 等待主站发布完成

## 常见问题

- 页面 404：确认文件在 `static/invest/research/` 下且路径以 `/invest/research/` 开头。
- 首页没有新研报：确认 `static/invest/research/data/reports.json` 已加入对应条目。
- AI 基建覆盖地图没有新报告：确认 `reports.json` 条目已经设置有效的 `chainLayer`，并运行 `validate_coverage_map.py`。
