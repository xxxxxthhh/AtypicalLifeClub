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

## 版本模型

报告更新分为两种模式，更新前必须先选定模式：

- `incremental`：同一周期内的小范围更新。保留当前 `id` 和 Markdown 文件，在正文中用删除线保留旧判断，并紧跟带日期的新判断；同步更新 `lastUpdate`、`summary`、`highlights`。
- `full-cycle`：每半年或每年产生的完整新版本；如果公司发生重大变化，也可以提前进入新周期。必须创建新的 `id` 和新的中英文 Markdown 文件，旧版本作为归档保留。

建议字段：

- `period`：报告周期，例如 `2026`、`2026H1`、`2026H2`。
- `versionType`：`initial`、`incremental` 或 `full-cycle`。
- `versionLabel`：页面展示用短标签，例如 `2026H2 Full Version`。
- `isCurrent`：当前公开列表版本为 `true`；旧周期归档版本为 `false`。字段缺省时按 `true` 处理。
- `supersedes`：新完整版本直接替代的上一版报告 `id`。
- `diffBase`：本轮完整版本做差异比较时使用的上一周期终版 `id`。通常与 `supersedes` 相同。
- `previousAnnualReport`：当前详情页展示的上一周期预览对象。

`previousAnnualReport` 只能指向已经保留的真实旧版本报告，不得指向临时摘要 Markdown。最小结构：

```json
{
  "id": "amd-2026h1",
  "label": "2026H1 Full Version",
  "labelEn": "2026H1 Full Version",
  "file": "/invest/research/reports/view.html?id=amd-2026h1",
  "date": "2026-02-04",
  "lastUpdate": "2026-06-22",
  "summary": "上一周期中文结论摘要。",
  "summaryEn": "Previous-cycle conclusion summary."
}
```

版本链规则：

- 首页默认只展示当前版本；如果 `reports.json` 同时保留旧版本，旧版本必须显式标记 `isCurrent: false`。
- 新的 `full-cycle` 版本只和上一周期终版做 diff，不追溯每一次增量更新。
- 旧版本必须保持可访问，`previousAnnualReport.file` 固定使用 `/invest/research/reports/view.html?id=<old-id>`。
- 不要用一个“预览摘要文件”伪装旧版本；预览文案放在 metadata，完整旧报告保留在旧版本条目里。
- 当前周期内的 `incremental` 更新不创建 `previousAnnualReport`，除非该报告本身已经是一个新周期版本并且链接到上一周期终版。

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
