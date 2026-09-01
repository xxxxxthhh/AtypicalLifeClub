# Atypical Life Club

使用 Hugo 构建、部署在 Cloudflare Pages 的个人站点。除主博客外，`/invest/` 下还挂着三个静态子应用（研究中心、汇率看板、金属看板），它们的数据由仓库内的 Python 脚本 + GitHub Actions 维护。

## 🚀 快速开始

### 本地开发

```bash
# 启动本地开发服务器（包含草稿）
hugo server -D

# 仅正式文章
hugo server
```

访问 [http://localhost:1313](http://localhost:1313)。子应用同样走这个服务器，例如 `/invest/research/`。

首次克隆需要拉取主题 submodule：

```bash
git submodule update --init --recursive
```

### 新建文章

```bash
hugo new posts/my-new-post.md
```

然后编辑 `content/posts/my-new-post.md`。

### 文章格式

```markdown
---
title: "文章标题"
date: 2026-01-03T15:55:00+08:00
draft: false           # true 表示草稿，不会发布
tags: ["标签1", "标签2"]
categories: ["分类"]
description: "文章描述"
cover:
    image: "/images/cover.jpg"  # 可选封面图
    alt: "封面图描述"
---

文章正文...
```

### 添加图片

将图片放入 `static/images/`，然后在文章中引用：

```markdown
![图片描述](/images/your-image.jpg)
```

## 📁 项目结构

```
.
├── content/                      # 博客正文
│   ├── posts/
│   ├── about.md / archives.md / search.md
├── static/
│   ├── images/                   # 静态图片资源
│   ├── shared/                   # 跨模块共享脚本（theme-switcher.js）
│   ├── invest/
│   │   ├── index.html            # 重定向到 /invest/research/
│   │   ├── styles.css / theme-adapter.css
│   │   ├── research/             # 研究中心（详见该目录 README.md）
│   │   │   ├── index.html, app.js, tracking-rules.js
│   │   │   ├── coverage-map.html            # AI 基建覆盖地图
│   │   │   ├── monitoring-dashboard.html    # 监控仪表盘 + 交叉校验雷达
│   │   │   ├── verdict-ledger.html          # 判断台账
│   │   │   ├── reviews/                     # 半年度复盘（独立于研报列表）
│   │   │   ├── reports/                     # 详情页模板 + 模块解析器
│   │   │   ├── data/*.json                  # 见下方「数据文件」
│   │   │   ├── feed.xml                     # 由 generate_feed.py 生成，需与数据同步
│   │   │   ├── validate_*.py / update_*.py / test_*.py
│   │   │   └── *.md                         # 中英文报告正文
│   │   ├── currency/             # 汇率看板（详见该目录 README.md）
│   │   └── metals/               # 金属看板（index.html + js/css + data + 脚本）
│   ├── research/                 # 旧路径兼容跳转（-> /invest/research/）
│   └── currency/                 # 旧路径兼容跳转（-> /invest/currency/）
├── docs/                         # 设计与自动化规格文档（见「维护文档索引」）
├── .github/workflows/            # CI 与 3 条数据自动化流水线
├── themes/PaperMod/              # 主题（Git submodule）
├── DESIGN.md                     # 设计系统（配色 / 字体 / 组件约束）
├── hugo.toml
├── hugo_stats.json               # Hugo writeStats 产物，已纳入版本管理
└── public/                       # 构建产物（gitignore）
```

## 🧩 模块说明

| 路径 | 说明 |
| --- | --- |
| `/` | 主博客（Hugo + PaperMod） |
| `/invest/` | 只做重定向，直接跳到 `/invest/research/` |
| `/invest/research/` | 研究中心：报告列表、详情页、覆盖地图、监控仪表盘、判断台账、半年度复盘、RSS |
| `/invest/currency/` | 汇率看板 |
| `/invest/metals/` | 金属看板（贵金属 / 工业金属期货与相关 ETF） |
| `/research/`、`/currency/` | 兼容旧链接，自动重定向到 `/invest/` 子路径 |

研究中心的数据文件都在 `static/invest/research/data/`：

| 文件 | 内容 | 维护方式 |
| --- | --- | --- |
| `reports.json` | 报告卡片元数据（唯一列表入口） | 人工 |
| `coverage-map.json` | AI 基建层级 / 角色 / 交叉校验规则 | 人工 |
| `signals.json` | 交叉校验信号日志（append-only） | 人工 |
| `benchmarks.json` | 基准标的配置 | 人工 |
| `earnings-calendar.json` | 财报日期与事件时区 | 人工 |
| `prices.json` | 价格台账 | `update-research-prices.yml` |
| `verdicts.json` | 判断台账 | `update-research-prices.yml` |
| `calibration-history.json` | 校准历史 | `update-research-prices.yml` |
| `earnings-tasks.json` | 每日财报待办队列 | `update-research-prices.yml` |

## 🤖 维护与更新流程

各模块的详细约定写在模块自己的文档里，**不要在本文件重复枚举字段规则**（历史上这里的字段清单正是最先过期的部分）：

- 研究中心（报告新增 / 版本模型 / 双语约定 / 模块契约 / 信号与监控规则）：[`static/invest/research/README.md`](static/invest/research/README.md)
- 汇率看板：[`static/invest/currency/README.md`](static/invest/currency/README.md)
- 金属看板：无独立文档，脚本用法见下

### 新增或更新研究报告（最小路径）

1. 中英文正文放入 `static/invest/research/*.md`（两个语种都必须是完整正文）
2. 在 `data/reports.json` 增加或更新一条记录。`validate_reports.py` 硬性要求的字段只有：
   `id`、`company`、`ticker`、`title`、`titleEn`、`summary`、`tags`、`category`、`date`、`lastUpdate`、`file`、`markdownFiles`
   - `file` 固定写 `/invest/research/reports/view.html?id=<id>`
   - `markdownFiles.zh` 与 `.en` 必须是两个不同文件
   - `stance`、`conviction`、`monitoring`、`coverageTier`、`chainLayer`、`versionType` 等增强字段是可选的，但**一旦出现就会被严格校验**；取值语义以 `validate_reports.py` 和 `docs/research-hub-v*-plan.md` 为准
3. 跑下面的「提交前本地检查」
4. 本地预览 `/invest/research/`、目标详情页，以及受影响的 `coverage-map.html` / `monitoring-dashboard.html`

### 金属看板脚本

```bash
python3 static/invest/metals/update_data.py      # 日更，upsert 当天数据
python3 static/invest/metals/validate_data.py    # 校验（失败则不要提交）
python3 static/invest/metals/fetch_historical.py # 重建历史（谨慎，会覆盖）
```

`update_data.py` 需要 `pip install yfinance`（`fetch_historical.py` 只用标准库）。两个脚本都直接决定 `historical.json` 的口径，改动前先读脚本内的注释。

### 汇率看板脚本

```bash
python3 static/invest/currency/update_real_data.py
python3 static/invest/currency/validate_data.py
```

### 共用前端约束

- 主题切换统一使用 `/shared/theme-switcher.js`，不要再往业务目录复制副本
- 子应用资源一律使用绝对路径（如 `/invest/research/...`）
- 配色、字体、组件规则见 [`DESIGN.md`](DESIGN.md)；不要用红/绿/琥珀色表达投资判断

## ✅ 提交前本地检查

以下与 `.github/workflows/ci-smoke.yml` 逐条对应，CI 会在 push 到 `main` 和 PR 上跑同一套。校验脚本需要 Python 3.11+。

```bash
# 单元测试
python3 -m unittest discover -s static/invest/research -p "test_*.py"
node --test static/invest/research/reports/report-module-parser.test.mjs \
             static/invest/research/test_tracking_rules.mjs

# 研究中心校验
python3 static/invest/research/validate_reports.py
python3 static/invest/research/validate_earnings_calendar.py
python3 static/invest/research/validate_coverage_map.py
python3 static/invest/research/validate_prices.py
python3 static/invest/research/validate_verdicts.py

# RSS 必须与数据同步（生成后不允许有 diff）
python3 static/invest/research/generate_feed.py
git diff --exit-code static/invest/research/feed.xml

# 其他模块数据校验
python3 static/invest/currency/validate_data.py
python3 static/invest/metals/validate_data.py

# 构建校验
hugo --minify
```

> ⚠️ `hugo` 构建会重写仓库内已跟踪的 `hugo_stats.json`。提交前确认这个文件的改动是你想要的，否则 `git checkout -- hugo_stats.json` 还原。

## ⏱️ 自动化流水线

| 工作流 | 触发 | 作用 |
| --- | --- | --- |
| `ci-smoke.yml` | push 到 `main` / PR | 上一节的全部测试、校验与 Hugo 构建 |
| `update-currency-data.yml` | 每天 00:00 UTC（北京 08:00）+ 手动 | 更新并校验 `currency/data/historical.json`，有变更才提交 |
| `update-metals-data.yml` | 每天 01:00 UTC（北京 09:00）+ 手动 | 更新并校验 `metals/data/historical.json`，有变更才提交 |
| `update-research-prices.yml` | 每天 22:00 UTC + 手动 | 拉价格 → 生成财报待办、判断台账、校准历史 → 严格校验后提交 |

`update-research-prices.yml` 定在 22:00 UTC 是因为要等美股、首尔、上海、香港全部收盘；`update_prices.py` 另外按各市场本地收盘时间过滤日线，避免把盘中报价写成收盘价。改动排期前请先读该工作流里的注释。

## 📚 维护文档索引

- [`DESIGN.md`](DESIGN.md) — 设计系统
- [`static/invest/research/README.md`](static/invest/research/README.md) — 研究中心完整维护说明
- [`static/invest/currency/README.md`](static/invest/currency/README.md) — 汇率模块
- `docs/research-hub-*-plan.md` — 研究中心 v2–v6 各阶段规格（字段语义的权威来源）
- [`docs/earnings-update-automation.md`](docs/earnings-update-automation.md) — 财报日期与定时任务契约

## ☁️ 部署

Cloudflare Pages 连接 GitHub 仓库，push 后自动构建：

- **Framework preset**: `Hugo`
- **Build command**: `hugo`
- **Build output directory**: `public`
- **环境变量** `HUGO_VERSION`: `0.154.2`（与 CI 保持一致）

自定义域名在 Pages 项目设置的 **Custom domains** 中绑定，Cloudflare 自动配置 DNS 与 HTTPS。

## 📝 发布流程

1. 本地编写 / 修改
2. `hugo server -D` 预览
3. 文章将 `draft: true` 改为 `draft: false`
4. 跑「提交前本地检查」中与改动相关的部分
5. 显式暂存改动的文件（避免 `git add .` 误带入本地临时目录），提交并推送
6. Cloudflare Pages 自动构建发布

## 🔧 站点配置

编辑 `hugo.toml`：`baseURL`、`title`、`params.description`、`params.socialIcons`、`menu.main`。

主题文档：[PaperMod](https://adityatelange.github.io/hugo-PaperMod/)

## 📄 License

MIT
