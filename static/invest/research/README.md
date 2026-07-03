# Research Center 维护说明

`/invest/research/` 已迁移到主博客仓库，不再单独部署。

## 目录结构

```
static/invest/research/
├── index.html                 # 研究中心首页
├── app.js                     # 首页渲染逻辑（读取 reports.json）
├── data/reports.json          # 研报卡片元数据（唯一列表入口）
├── data/coverage-map.json     # AI 基建覆盖地图配置（层级 / 角色 / crossChecks 校验规则）
├── data/signals.json          # 交叉校验信号日志（链级事件，引用 crossChecks 的 id）
├── validate_reports.py        # 元数据校验脚本
├── validate_coverage_map.py   # 覆盖地图 + 信号日志校验脚本
├── coverage-map.html          # AI 基建覆盖地图页面
├── monitoring-dashboard.html  # 全书监控仪表盘（含交叉校验雷达）
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
3. 如果报告承担 AI 基建链条验证角色，同步维护 `chainLayer` / `chainRole`，并确认 `data/coverage-map.json` 中已有对应层级或角色
4. 观察到链级事件（例如某超大规模厂商开始外售算力）时，在 `data/signals.json` 追加一条信号：`id` / `date`（YYYY-MM-DD）/ 双语 `title` / 双语 `detail`（含来源与日期）/ `crossChecks`（引用 `coverage-map.json` 中 crossChecks 的 `id`）/ `tickers`。监控仪表盘的「交叉校验雷达」会自动把信号挂到对应规则下；如果事件暴露了框架里没有的校验点，先在 `crossChecks` 里新增规则再记录信号。`tickers[]` 需要反链到覆盖报告或价格台账时，使用报告里的 `priceSymbol` 写法（例如 `000660.KS`、`688676.SS`）；只是事件里提到的未覆盖公司或主题标签，可以保持普通短代码写法（例如 `META`、`MU`）
5. 运行仓库内校验：
   - `python3 static/invest/research/validate_reports.py`
   - `python3 static/invest/research/validate_coverage_map.py`
   - `python3 static/invest/research/generate_feed.py`
   - `git diff --exit-code static/invest/research/feed.xml`
6. 对 full-cycle 重跑、版本链调整或大批量新增报告，额外运行独立发布契约检查：
   - `python3 /Users/kyx/.codex/skills/company-research-publishing/scripts/check_research_package.py static/invest/research`
   - 如果只检查单篇报告，可加 `--report-id <id>`
7. 在仓库根目录预览：`hugo server -D`
8. 检查 `http://localhost:1313/invest/research/`、`/invest/research/coverage-map.html`、`/invest/research/monitoring-dashboard.html` 和目标详情页
9. 提交并推送，走博客现有发布链路

## 追踪与复核规则

监控台的复核候选队列只用于排序复核工作，不会自动触发重跑。队列公式固定为 `ageDays / 60 + driftPct / 25`，其中 `ageDays` 来自报告的 `priceAsOf`，`driftPct` 来自 `data/prices.json` 的 `changePct` 绝对值；`ageDays > 60` 或 `driftPct >= 25` 会成为复核候选。缺失价格是一等状态：在队列里显示为 `无价格数据`，只按年龄项排序，不折算成 `0%` 漂移。

Batch-2 的未完成重跑 backlog 也进入同一套队列视角。队列给出排序，人决定是否重跑；不要把队列结果解释成投资信号或自动发布条件。

信号日志 `data/signals.json` 是 append-only。每当一个 monitoring item 有了新的读数（定期 `nextCheckDate` 或事件驱动触发），同一轮更新需要追加 signal，并用 `reportIds` 指向受影响报告、用 `monitoringRefs` 写明 `reportId:monitoringItemId`。如果报告更新是由某个监控读数触发，先或同时追加对应 signal，再更新报告正文和 metadata。

详情页支持同一页面三种浏览视图参数：

- `?lang=zh|en` 选择语言（默认中文）
- `?view=module|full|previous` 选择正文视图（默认 `module`）
  - `module`：按研究模块阅读，左侧导航固定为 11 个研究模块
  - `full`：展示当前版本完整正文
  - `previous`：同页展示上一周期完整正文
- `?module=<moduleId>` 在模块阅读中打开指定模块，例如 `overview`、`financial`、`valuation`
- `?diff=1` 在模块阅读中显示当前模块与上一周期版本的变化对照；只有存在 `previousAnnualReport` 时才有意义

旧参数 `view=clean` / `view=diff` 会被详情页兼容到模块阅读，但新链接应使用 `module|full|previous`。

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
   - AI 基建报告建议补充 `chainLayer`；需要承担验证任务时再补充 `chainRole`
2. 将中英文正文放到 `static/invest/research/*.md`，并在 `markdownFiles` 中映射
3. 如果新增了新的 AI 基建层级或角色，先更新 `data/coverage-map.json`，再运行 `validate_coverage_map.py`

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
