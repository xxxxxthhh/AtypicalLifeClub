# Research Center 维护说明

`/invest/research/` 已迁移到主博客仓库，不再单独部署。

## 目录结构

```
static/invest/research/
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

1. 添加或更新报告正文：`static/invest/research/*.md`
2. 在 `static/invest/research/data/reports.json` 增加或更新卡片元数据
3. 运行校验：`python3 static/invest/research/validate_reports.py`
4. 在仓库根目录预览：`hugo server -D`
5. 检查 `http://localhost:1313/invest/research/`
6. 提交并推送，走博客现有发布链路

## 新增报告最少改动

1. 在 `data/reports.json` 新增一条记录：
   - `id`
   - `company`
   - `ticker`
   - `title`
   - `titleEn`
   - `summary`
   - `category`
   - `date`
   - `lastUpdate`
   - `file`（固定为 `/invest/research/reports/view.html?id=<id>`）
   - `markdownFiles`（如 `{ "zh": "/invest/research/<zh_report>.md", "en": "/invest/research/<en_report>.md" }`）
   - `tags` / `highlights`
2. 将中英文正文放到 `static/invest/research/*.md`，并在 `markdownFiles` 中映射

## 双语报告约定（必须执行）

- `markdownFiles.zh` 和 `markdownFiles.en` 必须同时存在，且是两个不同的 `.md` 文件。
- 两个语言版本都必须是完整正文，不接受“卡片中文 + 详情英文摘要”这种拆分。
- 建议命名：
  - 中文：`<公司中文名>_深度研究报告_<YYYY-MM>.md`
  - 英文：`<Company>_Deep_Research_Report_<YYYY-MM>.md`
- 两个版本需要保持同一章节结构与关键数据口径一致。
- 详情页支持 `?lang=zh|en`，默认 `zh`。
- 更新任一语种时，需要同次提交更新另一个语种与 `lastUpdate`。

## 注意事项

- 首页数据以 `reports.json` 为准，`app.js` 不再硬编码报告列表。
- 详情页顶部支持 `中文 / EN` 切换，默认优先加载中文版本。
- 主题切换由共享脚本 `/shared/theme-switcher.js` 提供。
- 研究中心内容仅供个人研究记录，不构成投资建议。
