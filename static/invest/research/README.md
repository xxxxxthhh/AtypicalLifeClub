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
├── reviews/                   # 半年度复盘（与研报分开维护，见下）
│   ├── index.html             # 复盘列表 + 详情渲染器（自带 TOC / 双语 / 主题）
│   ├── reviews.json           # 复盘卡片元数据（独立目录，不进 reports.json）
│   └── *_复盘.md / *_Review.md # 复盘正文 Markdown（内嵌静态 SVG 图表）
└── *.md                       # 报告正文 Markdown
```

## 复盘（Reviews）维护

复盘是对覆盖标的的事后归因，**与研报分开**：单独的 `reviews/` 目录、单独的 `reviews.json`，不写入 `reports.json`，因此不会出现在研报列表里。节奏为**每半年一次**（2026H1、2026H2…）。

复盘正文用与研报相同的 Markdown 管线渲染，但有自己的轻量渲染器（`reviews/index.html`），不套用研报的「11 模块」公司报告骨架。图表用**内嵌静态 SVG**（`marked` 不执行 `<script>`，故不能用 Chart.js）：

- SVG 文字用 `fill="currentColor"` 跟随明暗主题；正负条用固定 `#2a78d6`／`#e34948`（两种主题都可读）。
- 整块 `<figure>…</figure>` 内**不能有空行**，否则 `marked` 会在空行处中断 HTML 块。

新增一期复盘：

1. 写中英文正文 `reviews/<YYYY>H<N>_复盘.md` 与 `reviews/<YYYY>H<N>_Review.md`，把图表 SVG 内嵌进去。
2. 在 `reviews/reviews.json` 增加一条记录（`id` / `title` / `titleEn` / `period` / `date` / `summary` / `summaryEn` / `tags` / `markdownFiles`）。
3. 预览 `http://localhost:1313/invest/research/reviews/`，详情页支持 `?id=<id>&lang=zh|en`。

研报首页 `index.html` 顶部有「查看半年度复盘 →」入口指向该目录。

## 更新流程

1. 添加或更新报告正文：`static/invest/research/*.md`
2. 在 `static/invest/research/data/reports.json` 增加或更新卡片元数据
3. 运行校验：`python3 static/invest/research/validate_reports.py`
4. 在仓库根目录预览：`hugo server -D`
5. 检查 `http://localhost:1313/invest/research/`
6. 提交并推送，走博客现有发布链路

详情页支持同一页面三种浏览视图参数：

- `?lang=zh|en` 选择语言（默认中文）
- `?view=clean|diff|previous` 选择正文视图（默认 `clean`）
  - `clean`：仅展示当前版本正文（清洁版）
  - `diff`：按章节展示与上一周期版本差异
  - `previous`：同页展示上一周期完整正文

`previousAnnualReport` 只在有真实历史版本时展示；没有历史版本的报告不显示视图切换。

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
  - 当前周期正文保持“清洁版”，不在正文内用 `~~...~~` 逐段删除；历史追溯改由详情页 `view=diff|previous` 提供。

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
