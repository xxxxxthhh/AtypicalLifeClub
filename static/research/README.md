# Research Center 维护说明

`/research/` 已迁移到主博客仓库，不再单独部署。

## 目录结构

```
static/research/
├── index.html                 # 研究中心首页
├── app.js                     # 首页渲染逻辑（读取 reports.json）
├── data/reports.json          # 研报卡片元数据（唯一列表入口）
├── validate_reports.py        # 元数据校验脚本
├── report-style.css           # 详情页样式
├── reports/view.html          # 通用详情页模板
├── reports/*.html             # 旧链接兼容跳转页
└── *.md                       # 报告正文 Markdown
```

## 更新流程

1. 添加或更新报告正文：`static/research/*.md`
2. 在 `static/research/data/reports.json` 增加或更新卡片元数据
3. 运行校验：`python3 static/research/validate_reports.py`
4. 在仓库根目录预览：`hugo server -D`
5. 检查 `http://localhost:1313/research/`
6. 提交并推送，走博客现有发布链路

## 新增报告最少改动

1. 在 `data/reports.json` 新增一条记录：
   - `id`
   - `company`
   - `ticker`
   - `title`
   - `summary`
   - `category`
   - `date`
   - `lastUpdate`
   - `file`（固定为 `/research/reports/view.html?id=<id>`）
   - `markdownFile`（如 `/research/<your_report>.md`）
   - `tags` / `highlights`
2. 将正文放到 `static/research/<your_report>.md`

## 注意事项

- 首页数据以 `reports.json` 为准，`app.js` 不再硬编码报告列表。
- 主题切换由共享脚本 `/shared/theme-switcher.js` 提供。
- 研究中心内容仅供个人研究记录，不构成投资建议。
