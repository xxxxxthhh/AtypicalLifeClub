# Research Hub v7 Plan — 覆盖补强、事实/估值更新边界与追踪契约演进

**Status:** Final — Round 4 reviewed GO (Claude × advisor) and signed off by owner, 2026-10-20. PR 2 / PR 3 may start; PR 4 waits for PR 1 ⓐⓑ.  
**Owner:** repository owner  
**Author:** planning session, 2026-10-20  
**Depends on:** [v3 tracking plan](research-hub-v3-tracking-plan.md), [v4 coverage & depth plan](research-hub-v4-coverage-depth-plan.md), [v5 stance & conviction plan](research-hub-v5-stance-conviction-plan.md), [v6 calibration & trigger plan](research-hub-v6-plan.md), [earnings update automation](earnings-update-automation.md), [daily briefing plan](daily-briefing-plan.md), [v7 review log](research-hub-v7-review-log.md)  
**Scope of this doc:** Self-contained specification for the v7 iteration of `static/invest/research/`. Designed for concurrent multi-agent review and incremental PR execution. An implementing or reviewing agent does not need the originating chat context or the external review log to execute this plan.

---

## 0. Context & grounded facts (verified 2026-10-20)

以下所有数据均直接取自 `main`（commit `bf7bf56`）与本地缓存的当日运行分支 `origin/codex/daily-research-2026-10-20`（commit `96fa3a4`；注：`docs/daily-research/2026-10-20-review.md` 位于 `origin/codex/daily-research-2026-10-20`（`96fa3a4`），不在 `main`）。Reviewer agent 可直接运行 `static/invest/research/` 下的只读校验器复现。

| Fact | Value (`main` @ `bf7bf56`) | Evidence / Code Reference | Consequence |
|---|---|---|---|
| **1. 报告库规模与分层** | `reports.json` 共 **79** 条记录：**68** 条当前报告（`isCurrent !== false`）+ **11** 条历史归档（`isCurrent: false`）。当前报告含 **54** 篇 AI 产业链（`chainLayer` 非空）+ **14** 篇非链独立研究（`chainLayer` 缺省）。 | `static/invest/research/data/reports.json` | 54 篇链内报告已形成 14 层拓扑，但部分单点层与亚太硬件节点仍薄弱；14 篇非链报告在 `tracking-rules.js` 的 Trigger Watch 规则中仍被 `!report.chainLayer` 过滤。 |
| **2. 产业链 14 层分布与单点层缺口** | `power` (9), `demand-risk` (9), `memory-storage` (6), `optical` (6), `semicap-equipment` (4), `resources` (4), `compute` (3: NVDA/AMD/CBRS), `datacenter-facility` (3: EQIX/VRT/DLR), `eda-ip` (2: SNPS/CDNS), `advanced-packaging` (2: AMKR/ASX), `custom-merchant-silicon` (2: AVGO/MRVL), `interconnect` (2: ALAB/CRDO), **`foundry` (1: TSMC)**, **`networking` (1: ANET)**。`planned[]` 现有 2 家（`0522.HK` ASMPT、`BESI.AS`）。 | `static/invest/research/data/coverage-map.json` | `foundry` 与 `networking` 为单点层（缺横向白盒交换机/网络硬件对标如 `CLS`）；`eda-ip` 层中 SNPS 已覆盖接口与 Design IP，但缺**独立 CPU 架构授权与版税（Architecture License / Royalty）**视角（`ARM`）。 |
| **3. 地域覆盖集中度** | 68 篇当前报告中，美股/ADR 占 **63** 篇，非美本地交易代码仅 **5** 个：`000660.KS` (SK hynix)、`285A.T` (Kioxia)、`0100.HK` (MiniMax)、`688676.SS` (金盘科技)、`300308.SZ` (中际旭创)。 | `static/invest/research/data/reports.json` (`priceSymbol`), `data/prices.json` | 亚太供应链（尤其台湾服务器电源散热、日本封装载板、欧洲后道设备）覆盖密度低于上游物理约束的实际权重。 |
| **4. 报告结构契约与元数据残缺** | 1) `moduleContract: "heading-comment-v1"`（双语 Markdown 11 个语义模块显式注释契约）当前共 **16 / 68 (23.5%)** 篇启用（**链内 12 篇 + 非链 4 篇**），其余 **52 篇 (76.5%)** 仍依赖标题关键词推断。<br>2) 54 篇链内报告中 **14 篇 (25.9%) 缺失 `chainRole`**（`corning-2026`, `nvidia-2026`, `aaoi-2026`, `gevernova-2026`, `sandisk-2026`, `sk-hynix-2026`, `almonty-2026`, `bloom-energy-2026`, `neov-2026`, `copx-2026`, `amd-2026`, `jinpan-2026`, `broadcom-2026`, `kioxia-2026`）。<br>3) 14 篇非链报告中 **12 篇缺失 `coverageTier`**（仅 `rklb-2026` 为 `full`、`smh-2026` 为 `lite`）。 | `static/invest/research/data/reports.json`, `static/invest/research/README.md:122-160`, `static/invest/research/validate_coverage_map.py:258-264`（`chainRole` 仅在字段存在时校验取值，不强制必填）, `static/invest/research/validate_reports.py:619-656` (`coverageTier`) | 14 篇核心链内报告在拓扑视图中缺少角色标签；12 篇非链报告缺 `coverageTier`（注：`ENFORCE_COVERAGE_TIER` 仅对链内报告强制，非链补值不受门禁保护）。`moduleContract` 迁移属于结构重构，不宜与日常财报更新混绑。 |
| **5. 立场分布与校准观察（Calibration Observation）** | 54 篇链内报告立场：`bullish`: **0**，`constructive`: **6** (11.1%)，`neutral-watch`: **25** (46.3%)，`cautious`: **21** (38.9%)，`bearish-avoid`: **2** (3.7%)；`conviction`: `high`: **0**，`medium`: **48**，`low`: **6**。<br>`calibration-history.json` (`2026-10-19`)：`scoredCount: 115`，`medianRelativePct: -1.8%`，`nonNeutralBeatRate: 43.4%`（`SMH` 基准桶内 33 笔 `cautious` 中位超额收益为 `-7.1%`；注：`calibration_history.py:121-122` 的 `beatRate` 统计跑赢比例而非方向准确率）。 | `static/invest/research/data/reports.json`, `data/verdicts.json`, `data/calibration-history.json`, `static/invest/research/calibration_history.py:121-122` | 仅作为投资组合层面的客观分布观察保留，不作为强推立场调整或机械回填的直接依据。 |
| **6. 复核队列积压与 Reviewer `P-*` 绑定** | 68 篇当前报告中 **46 篇 (67.6%)** 处于复核候选队列（**43 篇** `priceAsOf` > 60 天，集中在 `2026-07-30/31`；**13 篇** `|changePct| >= 25%`：`pltr-2026` +54.5%、`almonty-2026` -46.0%、`minimax-2026` -45.4%、`oklo-2026` -43.7%、`neov-2026` -40.8%、`aaoi-2026` -37.3%、`meta-2026` +30.9%、`vertiv-2026` -29.5%、`marvell-2026` +29.3%、`seagate-2026` -28.2%、`innolight-2026` -27.3%、`nrg-2026` -25.8%、`sk-hynix-2026` -25.7%）。<br>另有 **11 篇报告 `lastUpdate` 比 `priceAsOf` 新 14~60 天**（如 `synopsys-2026` 在 `Synopsys_深度研究报告_2026-07.md:22` 曾做过事实更新但保留旧估值锚）。<br>在 `origin/codex/daily-research-2026-10-20`（`96fa3a4`）中，全部 open items 共 **40 项处于 `deferred`（其中 `P-*` 遗留项为 26 项）**，候选池 `C-01..C-41` 有 **40 项未解决**。 | `static/invest/research/data/reports.json`, `data/prices.json`, `docs/daily-research/2026-10-20-review.md:178,225`（位于 `origin/codex/daily-research-2026-10-20`@`96fa3a4`，不在 `main`） | 事实更新在 reviewer 实践中被完整估值包绑定；绑定来自 reviewer `memory.md` 继承的 `P-*` 条件（`:239` P-25、`:241`、`:248`），而非校验器或 reviewer prompt 本身（10-10 至 10-20 共 11 次 reviewer 主会话落地 0 笔财报事实驱动的报告更新；如 `constellation-energy-2026` 的 Brazos Valley 剥离交割虽已被 reviewer 读过交割稿，仍因等待 `P-25` 完整包导致 `main` 正文 `Constellation_Energy_深度研究报告_2026-07.md:22` 写着「交割尚待 DOJ 批准」）。 |
| **7. 触发器链接门禁、监控项 `reading` 与 Trigger Watch 实况** | 1) **触发器链接数据已完备但门禁仅校验链内单侧**：`reports.json` 中 **`downgrade.monitoringIds` 与 `upgrade.monitoringIds` 在链内 54/54、非链 14/14 均已 100% 配置**，但 `validate_reports.py:424-441` 目前仅对链内 `downgrade.monitoringIds` 实施了强校验。<br>2) **监控项 `reading` 覆盖率（v6 契约下为可选）**：`validate_reports.py:428` 注释锁定 `"reading itself stays optional forever"`。实盘全部当前报告共 **349** 个监控项中 **167 项 (47.9%) 无 `reading`**（链内 **94 / 266 = 35.3%**，非链 **73 / 83 = 88.0%**；**11 篇链内报告 100% 监控项无 `reading`**）。若只看被 `stanceTriggers` 引用的关键监控项：**链内 250 项中有 84 项无 `reading`**，**非链 72 项中有 63 项无 `reading`**（全部当前报告合计 322 项中有 147 项无 `reading`）。<br>3) **Trigger Watch 渲染位置与实跑结果**：`tracking-rules.js:92-124` 的 `buildTriggerWatchRows()` 由 **`verdict-ledger.html`（第 638 行）** 消费，筛选条件为 `reading === 'breached' && linked.has(id) && (!stanceDate || stanceDate <= item.readingAsOf)`。当前全库共 4 个 `breached` 项（链内 `alab-2026` 2 项 `readingAsOf=2026-08-05` < `stanceDate=2026-10-11`；非链 `salesforce-2026` `08-27 < 08-28`、`spotify-2026` `08-04 < 10-02`），因立场均已在 breach 之后重新裁决，**实跑 `buildTriggerWatchRows(reports)` 当前返回 0 行，移除 `!report.chainLayer` 后实盘仍为 0 行（代表所有历史 breach 均已裁决的健康状态）**。 | `static/invest/research/validate_reports.py:424-441`, `static/invest/research/tracking-rules.js:92-124`, `static/invest/research/verdict-ledger.html:638` | 1) `upgrade.monitoringIds` 无需数据回填，只需在校验器开启门禁；<br>2) 移除 `tracking-rules.js:95` 的 `!report.chainLayer` 是前瞻性规则对齐（需同步改写 `test_tracking_rules.mjs` 现有用例 `'non-chain and archived reports are skipped'` 的非链断言）；<br>3) 被引用项必填 `reading` 属于对 v6 契约的显式演进，v7 阶段先锁定为 **chain-only（250 项补 84 项）**。 |
| **8. `verdicts.json` 的 `stale` 契约与月度监控逾期暴露** | `main` 上有 **13 个监控项**的 `nextCheckDate < "2026-10"` 已过月度检查窗（涉及 `arista-2026`, `neov-2026`, `tsmc-2026`, `micron-2026`, `constellation-energy-2026`, `vistra-2026`, `minimax-2026` 共 7 篇报告）。`verdicts.json` 中 54 笔 open verdicts 的 `stale` 均为 `false`。 | `static/invest/research/update_verdicts.py:243`, `docs/research-hub-v5-stance-conviction-plan.md:37,147` | `days_held > 120 and monitoring_overdue` 是 **v5 锁定的 `stale` 契约**（实现与设计一致）。为在不破坏 v5 契约的前提下暴露上述 7 篇监控逾期报告，在 `verdicts.json` 中**独立新增 `monitoringOverdue` 字段**，保留原 `stale` 语义不变。 |
| **9. 财报日历未上屏与 `call` vs `release` 事件模型缺失** | 1) `earnings-calendar.json`（65 条非 ETF 记录：30 `issuer-confirmed`、20 `estimated`、10 `stale`、4 `unknown`、1 `recorded`）与 `earnings-tasks.json`（29 条任务）**尚未被前端页面读取渲染**。<br>2) 在 `docs/daily-research/2026-10-20-review.md:17,40,50`（位于 `origin/codex/daily-research-2026-10-20`@`96fa3a4`，不在 `main`）中，AMZN（公告 `10-29 17:00 ET` 电话会，现日历仍为 `10-22` 估计）、LRCX (`10-21 14:00 PDT / 17:00 EDT`)、CDNS (`10-26 14:00 PT`)、EQIX (`10-28 17:30 ET`)、VST (`11-06 10:00 ET`) 的发行人公告**仅确认了业绩电话会/Webcast 时间，未单列财报新闻稿发布时点（`session`）**。Reviewer 明确给出重开条件：「可读发布日原文，**或**单独测试区分 `call` 与 `release` 的事件模型」。 | `static/invest/research/data/earnings-calendar.json`, `static/invest/research/validate_earnings_calendar.py:125-129`, `docs/earnings-update-automation.md:33,59`, `docs/daily-research/2026-10-20-review.md:17,40,50`（位于 `origin/codex/daily-research-2026-10-20`@`96fa3a4`，不在 `main`） | 必须在日历模型中**拆分 `release`（主记录）与 `call`（子对象）事件类型**，为 `call` 配备独立的 `timezone` 与全状态任务生成规则，并对 `docs/earnings-update-automation.md:33,59` 作出显式契约演进声明。 |
| **10. 价格台账 `TLDR-7` 缺日待查与非链新鲜度门禁** | 1) `docs/daily-research/2026-10-20-review.md:39`（位于 `origin/codex/daily-research-2026-10-20`@`96fa3a4`，不在 `main`）将 `TLDR-7`（4 个非美代码 `000660.KS`, `688676.SS`, `300308.SZ`, `0100.HK` 缺 `2026-10-12` bar）的根因保留待查。`update_prices.py:418` 本就通过 `yfinance` 拉取日线区间，缺口发生在源端还是过滤环节尚未证实。<br>2) `validate_reports.py:121` 中 `ENFORCE_NONCHAIN_FRESHNESS = False` 仍未开启（当前 14 篇非链报告已 100% 满足该校验，0 warning）。 | `static/invest/research/update_prices.py:418`, `static/invest/research/validate_reports.py:121`, `docs/daily-research/2026-10-20-review.md:39`（位于 `origin/codex/daily-research-2026-10-20`@`96fa3a4`，不在 `main`） | 1) `ENFORCE_NONCHAIN_FRESHNESS` 可立即切换为 `True`；<br>2) 价格 5D 序列必须**先复现查明 `TLDR-7` 缺日根因**，并建立连续交易日与同一拆股口径的完整性校验。 |

---

## 1. Principles & Owner Rulings (locked 2026-10-20)

1. **Mode A 准入按「事实是否是估值输入」判定，不再看 review 里有没有 `P-*` 条件（Owner 裁决 1）** —
   - **估值输入的定义**：估值模块算术所消费的量，包括期末股本、净现金/债务、FX、价格锚、倍数分母（含作为分母的盈利或收入指引）、情景权重，以及 `stance` / `conviction`。
   - **Mode A（事实更新，保留旧估值锚）**：适用于不属于估值输入的事实，例如交割完成或终止、订单/出货/积压、监控指标读数、监管或法律事件、新财报期的经营数据。新的指引数字可以在事实模块**记录**，但 Mode A 不得把它**代入**估值算术。即使该报告在 review 中挂着估值类 `P-*` 重开条件，Mode A 事实也可以先行合入；估值条件保持 open，不因此关闭。
   - **Mode B（完整重锚）**：凡要改动上述任一估值输入或估值数值，都走 Mode B。
2. **证据零推断与事件类型分离（Zero Inference on Issuer Confirmation）** — 发行人仅确认业绩电话会（`call`）时，以独立的 `call` 子对象记录 `issuer-confirmed` 及事件本地时区，**严禁**将电话会钟点推断为财报新闻稿发布 `session`（`after-close` / `before-open`），亦不得用电话会日期覆盖尚未确认的 `release` 日期。
3. **尊重既有版本契约，显式声明契约演进（Explicit Contract Evolution）** — 对 v5/v6 及 `earnings-update-automation.md` 已锁定的规则（如 `verdicts.json` 的 `stale` 定义、`reading` 的可选性、正式研究更新任务的触发源与去重键格式），保持向后兼容或通过显式契约修订 + `ENFORCE_*` 开关演进。
4. **范围收敛与小步快跑（Orthogonal Slicing）** — PR 2 与 PR 3 聚焦确定性工程补齐与日历事件模型，不依赖复杂的单篇报告重锚；结构迁移（`moduleContract`、双腿 `crossChecks`、非链 `verdicts`、期间键规范化）单独后置立项。
5. **严守 `DESIGN.md` 视觉规范** — 任何新增前端面板严禁使用红/绿/黄交通灯色表达好坏或涨跌，统一使用纸感底色、墨色层级以及 `DESIGN.md` 定义的真实色值变量 `--accent`（`#2f6fed`）与 `--accent-alt`（`#0f9d8c`）区分结构状态。

---

## 2. Track 1 — 事实更新（Mode A）与完整重锚（Mode B）的准入裁决、Reviewer 同步与试点排期

### 2.1 问题陈述
事实更新在 reviewer 实践中被完整估值包绑定；绑定来自 reviewer `memory.md` 继承的 `P-*` 条件（`:239` P-25、`:241`、`:248`），而非校验器或 reviewer prompt 本身：
- 在 `docs/daily-research/2026-10-20-review.md`（位于 `origin/codex/daily-research-2026-10-20`（`96fa3a4`），不在 `main`）中，`P-27`（TSMC，`:180`）要求「…估值／情景、显式立场复核、双语旧锚处理及精确 monitoringRefs signal 同批完整包；不单刷 latest／日期」；`P-34`（ASML，`:187`）写明「不单刷 latest／lastUpdate」；`P-21`（Micron，`:174`）自 09-30 起要求 EV 口径、资本开支桥与立场裁定一并提交；`P-25`（`:178`）与 `C-39`（`:225`，对应 reviewer `memory.md:286`）要求 `constellation-energy-2026` 的 Brazos Valley 剥离交割随 `P-25` 完整估值包处置，导致 `main` 正文 `Constellation_Energy_深度研究报告_2026-07.md:22` 至今仍写着「交割尚待 DOJ 批准」。
- 10-10 至 10-20 共 11 次 reviewer 主会话期间，`main` 上落地 **零笔财报事实驱动的报告更新**。因此必须同时在本文档与 reviewer 侧（prompt 与 `memory.md` 的 `P-*` 条件分类）解除把非估值输入事实捆进完整估值包的限制。

### 2.2 Mode A / Mode B 准入规则、必填义务与 Reviewer 侧同步（Owner 裁决 1）

#### 1. 估值输入、Mode A 与 Mode B 的定义
- **估值输入的定义**：估值模块算术所消费的量，包括期末股本、净现金/债务、FX、价格锚、倍数分母（含作为分母的盈利或收入指引）、情景权重，以及 `stance` / `conviction`。
- **Mode A（事实更新，保留旧估值锚）**：适用于不属于估值输入的事实，例如交割完成或终止、订单/出货/积压、监控指标读数、监管或法律事件、新财报期的经营数据。新的指引数字可以在事实模块**记录**，但 Mode A 不得把它**代入**估值算术。
  - 即使该报告在 review 中挂着估值类 `P-*` 重开条件，Mode A 事实也可以先行合入；估值条件保持 open，不因此关闭。
- **Mode B（完整重锚）**：凡要改动上述任一估值输入或估值数值，都走 Mode B（全量更新双语 11 个模块、重算估值表与情景权重、推进 `priceAsOf` 与 `lastUpdate`，并运行 `update_prices.py`、`update_verdicts.py`、`update_calibration_history.py`）。

#### 2. Mode A 的必填义务
1. 正文中被新事实证伪的表述必须改正，包括估值模块里的文字陈述；只改事实陈述，不改估值数字。
2. 若新事实使现有估值口径过时，必须在双语估值模块与摘要估值引用处加带日期的边界标注：「估值仍按 YYYY-MM-DD 锚定的旧口径，<哪个输入> 待 Mode B 重算」，并把该报告列入 Mode B 积压表。这是 Mode A 的**必填项**，不是违约，也不阻塞合入。
3. Mode A 推进 `lastUpdate`，不动 `priceAsOf` 和 `prices.json.baseDate`。
4. 仍需满足既有要求：双语一致；`signals.json` 带精确 `monitoringRefs`；`reading` 按该项自身 trigger 文本评级，证据不足填 `unclear`。
5. **Mode A 包的字段范围**：`reports.json` 可改 `reportedPeriod`（仅当涉及新财报期）、`monitoring[].latest` / `reading` / `readingAsOf` / `readingNote` / `nextCheckDate`、`lastUpdate`；`signals.json` 追加 signal 并带 `reportIds` 与精确 `monitoringRefs`；正文双语 Markdown 按第 1、2 条修改。范围外的字段一律不动，尤其是 `priceAsOf`、`stance`、`conviction`、`stanceHistory`，以及 `prices.json`、`verdicts.json`。

#### 3. Reviewer 侧同步（PR 1 交付项，由 owner 授权的会话执行，不由撰写 agent 执行）
- **ⓐ 改 reviewer prompt**（`~/.codex/automations/daily-alc-branch-review-gate/automation.toml`），写入三点：
  1. 「producer 不得改 valuation」中的 valuation 指估值**数值**：倍数、区间、情景权重、分母、`priceAsOf`、`stance` / `conviction`。
  2. 带日期的边界标注是 Mode A 的必填项，不构成违约。
  3. Mode A 推进 `lastUpdate`、不动 `priceAsOf`，不算「单刷 lastUpdate」。
- **ⓑ 重分类 reviewer `memory.md` 里的 `P-*` 条件**：按裁决 1 把每条 `P-*` 拆成「事实部分（Mode A 可闭合）」和「估值部分（继续 open）」。Owner 已授权收窄。重分类结果必须体现在下一轮 `*-review.md` 中，producer 才知道哪些事实腿已放行。
- **验收方式**：ⓐ 的 toml diff 包含上述三点定义；ⓑ 的 `memory.md` 中 P-25、P-27、P-34 各自拆出「事实部分：已放行」行，并出现在下一轮 review 中。

### 2.3 首个 Mode A 试点（CEG）与 Mode B 积压排期（Owner 裁决 2）

#### 1. 首个 Mode A 试点：`constellation-energy-2026` 的 Brazos Valley 剥离交割
- **试点事实**：`constellation-energy-2026`，2026-10-14 Brazos Valley Energy Center（606MW，ERCOT）出售给 LS Power 完成交割（见 `docs/daily-research/2026-10-20-review.md:225` `C-39`（位于 `origin/codex/daily-research-2026-10-20`（`96fa3a4`），不在 `main`）/ reviewer `memory.md:286`；企业 newsroom 交割稿）。
  - **注意**：不是 Calpine。Calpine 收购已于 2026-01-07 完成，报告已记录（`Constellation_Energy_深度研究报告_2026-07.md:14`）。
  - Brazos 剥离**不改股本**。交割稿没有给出对价或所得款，对净债务的影响**数值未知**，以 10-Q 为准（Q3 日历 `2026-11-09`，`estimated`）。
- **试点 Mode A 包只做三件事，不含任何估值数字**：
  1. 报告 `Constellation_Energy_深度研究报告_2026-07.md:22` 中「$860M（交割调整前）……交割尚待 DOJ 批准」改为带日期的交割事实（双语同步）。
  2. 「最后一项」监管承诺出售的措辞，按交割稿所述「约 4.4GW PJM 资产预计 2026 年底前交割」修正。
  3. 估值模块加边界标注：「净债务仍按 2026-07-30 锚（约 $21.6B），Brazos 所得款待 10-Q / Mode B」。
- **执行与目的**：由 owner 的交互式会话执行，经每日 reviewer 审核合入；目的是验证 ⓐⓑ 生效后 reviewer 是否放行 Mode A 包。
- **第二批 Mode A 候选**：`netflix-2026`、`wdc-2026`、`lam-research-2026` 保留为第二批候选；此外，`tsmc-2026` (`P-27`) 与 `asml-2026` (`P-34`) 中已闭合或已 `taken` 的事实腿也可按 Mode A 先行：**TSMC 的 `advanced-node` 当季腿、`cowos`、`customer-concentration`，以及 ASML 的订单读数**。

#### 2. Mode B 积压表（由 owner 手动排期）
在首个试点通过后，再由 owner 决定是否新开每周 Mode B 重锚任务。在那之前，Mode B 积压表由 owner 手动排期，正文中维护以下清单：
- **P-21 Micron**（自 09-30）
- **P-34 ASML**（自 10-15）
- **P-27 TSMC**（自 10-16）
- **P-25 CEG 估值部分**
- **P-6 金盘**
- **P-19 中际旭创**
- **P-22 Synopsys**

其中 `asml-2026` (`P-34`) 与 `tsmc-2026` (`P-27`) 的 **Mode B 部分**具名条件对照如下（引自 `docs/daily-research/2026-10-20-review.md:180,187`，位于 `origin/codex/daily-research-2026-10-20`（`96fa3a4`），不在 `main`）：

| 报告 (`P-*`) | Mode B 部分具名重开条件（保留 open 直至 Mode B 执行；已闭合或已 `taken` 的事实腿可按 Mode A 先行） |
|---|---|
| **`asml-2026` (`P-34` Mode B 部分)** | 1. 独立当前收盘价与同截点 FX；<br>2. 同截点期末普通股 / ADR 换算（加权股数 `383.1M` 或当季回购 `~2.8M` 不得当期末股本）；<br>3. 流动债务拆分及现金 / 短期投资 / 净债务全桥（`€1,963.0M` 仅是非流动债务）；<br>4. FY2026 与 through-cycle 财务 / 估值 / 情景桥（不机械沿用旧 `14.6x`）；<br>5. 显式立场复核（修复 `stanceRationale` 中旧 `€36–40B` 前提）与双语旧锚清理。<br>*（注：ASML 的订单读数属于非估值输入事实，可按 Mode A 先行。）* |
| **`tsmc-2026` (`P-27` Mode B 部分)** | 1. 独立当前收盘价、期末股数与法定 ADR 比例；<br>2. 明确净现金换算的期末即期 FX（`31.98` 为季度平均、`31.8` 为指引假设，均非已核期末即期）；<br>3. 全年财务分母与估值 / 情景重建、显式立场复核、双语旧锚清理；<br>4. 监控项边界：`n3-n2-ramp` 复合 trigger 有未知腿不得机械维持 `within`；`overseas-fab-margin-drag` `66.4% > 60%` 仅证当季阈值；3 项 `nextCheckDate` 须有确定性发行人日历语义。<br>*（注：TSMC 已闭合或已 `taken` 的事实腿——`advanced-node` 当季腿、`cowos`、`customer-concentration`——可按 Mode A 先行。）* |

### 2.4 顶层时间戳校验与 `factsAsOf` 决策
1. **v7 暂缓引入 `factsAsOf`**：不在 `reports.json` 顶层新增 `factsAsOf` 字段，由现有的 `priceAsOf`（估值锚）、`reportedPeriod`（财报期）、`monitoring[].readingAsOf`（单项指标核验日）与 `lastUpdate`（报告包最近实质修订日）协同表达。
2. **在 PR 2 新增 `lastUpdate >= priceAsOf` 校验规则**：
   - 现状：`static/invest/research/validate_reports.py:827` 目前仅校验 `lastUpdate` 与 `priceAsOf` 的 `YYYY-MM-DD` 日期格式。
   - 交付项：在 `validate_reports.py` 中新增断言 `lastUpdate >= priceAsOf`（实测当前 `main` 上 68 篇当前报告 0 违例），并在 `test_validate_reports.py` 中补充单测。

---

## 3. Track 2 — 触发器闭环、判断台账（Verdicts）逾期暴露与非链并轨

### 3.1 `verdicts.json`：保留 v5 `stale` 契约，独立暴露 `monitoringOverdue`
- **背景与契约边界**：
  `static/invest/research/update_verdicts.py:243` 的 `stale = days_held > STALE_DAYS and monitoring_overdue(report, today)` 是 [v5 方案](research-hub-v5-stance-conviction-plan.md)（第 37、147 行）锁定的设计契约。
- **改进方案（零破坏扩展）**：
  1. **保留 `stale` 现有计算公式完全不变**。
  2. 在 `static/invest/research/update_verdicts.py` 生成的每条 open verdict 记录中，仅新增一个独立诊断字段：
     - `monitoringOverdue: bool` — 直接等于 `monitoring_overdue(report, today)`（当任意 `monitoring[].nextCheckDate < today[:7]` 时为 `true`；当前 `main` 上将精准标出 `arista-2026`, `neov-2026`, `tsmc-2026`, `micron-2026`, `constellation-energy-2026`, `vistra-2026`, `minimax-2026` 共 **7 篇报告**）。
  3. 同步更新 `static/invest/research/validate_verdicts.py` 以及单元测试 **`test_update_verdicts.py`** 与 **`test_validate_verdicts.py`**。

### 3.2 对称触发器门禁：将链内 `upgrade.monitoringIds` 纳入强制校验
- **范围锁定**：与 `static/invest/research/validate_reports.py:430-441` 现有的 `is_current_chain_report(report)` 范围严格保持一致（**chain-only，54 篇当前链内报告**）。
- **改进方案**：
  扩展 `static/invest/research/validate_reports.py:424` (`validate_trigger_link_requirements`)：
  - 对**全部当前链内报告（`is_current_chain_report`）**，`stanceTriggers.downgrade.monitoringIds` 必须非空（与现有 `validate_reports.py:430-441` 保持一致）；
  - 当 `stance != "bullish"` 时，`stanceTriggers.upgrade.monitoringIds` 必须非空。
  - 当前 54 篇链内报告已 100% 满足（无需回填数据，开启后 0 error / 0 warning），并在 `test_validate_reports.py` 中补充单测。

### 3.3 演进 v6 契约：为链内被触发器引用的监控项分阶段补齐 `reading`（Chain-Only Scope）
- **现状与契约声明**：
  在 v6 契约中，`monitoring[].reading` 为永久可选（`validate_reports.py:428`）。54 篇当前链内报告共 266 个监控项（94 项无 `reading`），其中**被 `stanceTriggers.{upgrade,downgrade}.monitoringIds` 引用的监控项共 250 项，内有 84 项无 `reading`**（含 11 篇全部监控项无 `reading` 的链内报告：`lam-research-2026`, `eqix-2026`, `sk-hynix-2026`, `bloom-energy-2026`, `copx-2026`, `microsoft-2026`, `meta-2026`, `pltr-2026`, `crdo-2026`, `lumentum-2026`, `cerebras-2026`）。
- **范围锁定与分阶段迁移方案**：
  1. **v7 范围明确锁定为 Chain-Only（`is_current_chain_report` 的被引用监控项，共 250 项，待补 84 项）**；非链报告的 63 项未评级被引用项明确留待后续独立批次处理，不在 v7 门禁内。
  2. **在 `validate_reports.py` 新增 `ENFORCE_LINKED_READING = False`（warn-first 开关）**：
     新增函数 `validate_linked_monitoring_readings(report, report_idx)`，仅对 `is_current_chain_report(report)` 检查其 `stanceTriggers.{upgrade,downgrade}.monitoringIds` 所指向的每个 `monitoring[]` 条目是否具有非空 `reading`。
  3. **分批回填与转正（PR 4）**：
     在 PR 4 中，依据已核实的一手证据为上述 84 个链内被引用监控项补齐 `reading`（`within` | `unclear` | `breached`）、`readingAsOf` 与 `readingNote`（凡公开证据不足以判定阈值或复合触发器存在未知腿的，必须填 `"unclear"`，严禁凑数填 `"within"`）。待 84 项全部补齐、warning 归零后，将 `ENFORCE_LINKED_READING` 切换为 `True`。

### 3.4 移除 `tracking-rules.js` 的链内限制（前瞻性规则对齐）
- **现状与实跑结论**：
  `static/invest/research/tracking-rules.js:95` 的 `buildTriggerWatchRows()` 由 **`static/invest/research/verdict-ledger.html`（第 638 行）** 消费，用于展示「已触发 `breached` 且自 `readingAsOf` 之后尚未重新裁决立场（`!stanceDate || stanceDate <= item.readingAsOf`）」的告警行。
  当前全库 4 个 `breached` 项（`alab-2026` 2 项、`salesforce-2026` 1 项、`spotify-2026` 1 项）的最新 `stanceDate` 均晚于其 `readingAsOf`，因此实跑 `buildTriggerWatchRows(reports)` 在移除 `!report.chainLayer` 前后**均返回 `0` 行**（「0 行 = 所有已发生 breach 均已完成立场复核」的健康状态）。
- **修复与验证方案**：
  1. 在 `static/invest/research/tracking-rules.js:95` 中移除 `!report.chainLayer` 过滤条件，使非链报告与链内报告遵循同一套未裁决 breach 监控规则。
  2. **验收方式**：改写 `static/invest/research/test_tracking_rules.mjs` 现有用例 `'non-chain and archived reports are skipped'`——其中非链腿改为期望返回 1 行（出现未裁决 breach 告警），archived（`isCurrent: false`）腿保留期望返回 `[]`。
- **同步工程收尾（PR 2）**：
  - 在 `static/invest/research/validate_reports.py:121` 将 `ENFORCE_NONCHAIN_FRESHNESS` 从 `False` 切换为 `True`（当前已 0 warning）。
  - 为缺失 `coverageTier` 的 12 篇非链报告补齐 `coverageTier`（11 篇个股标为 `"full"`，`igv-2026` 标为 `"lite"`；注：`validate_reports.py:619-656` 的 `ENFORCE_COVERAGE_TIER` 仅对链内强制，非链补值不受门禁保护），为缺失 `chainRole` 的 14 篇链内报告补齐 `chainRole`。

---

## 4. Track 3 — 财报日历 `release` / `call` 事件分离模型与前端雷达

### 4.1 契约演进：`release` 主记录 + `call` 子对象分离模型
- **显式契约演进声明（对 [`docs/earnings-update-automation.md`](earnings-update-automation.md) 的修订）**：
  1. 原 `docs/earnings-update-automation.md:33,55` 规定每个 `reportId` 仅承载单一财报发布（`release`）事件，且「只有 `issuer-confirmed` 的 `release` 可触发 `research-update` 任务」。v7 演进为：保持每个当前非 ETF `reportId` 在 `entries[]` 中唯一一条主记录（代表 `release` 事件，原字段语义与严苛标准 100% 不变），同时允许挂载可选的 **`call` 事件子对象**，以及可选的 **`fiscalPeriod`** 字段；当主记录尚非 `issuer-confirmed` 而 `call` 为 `issuer-confirmed` 时，允许由 `call` 窗口触发 `research-update` 任务。
  2. 原 `docs/earnings-update-automation.md:59` 锁定任务去重键格式为 `earnings:<reportId>:<expectedDate|unknown>:<window>`。v7 显式扩展去重键契约：由 `call` 子对象触发的任务使用去重键格式 **`earnings:<reportId>:call-<call.expectedDate>:<window>`**。

  ```json
  {
    "reportId": "amzn-2026",
    "company": "Amazon",
    "timezone": "America/New_York",
    "fiscalPeriod": "Q3 2026",
    "expectedDate": "2026-10-22",
    "precision": "day",
    "status": "estimated",
    "session": "unspecified",
    "sourceUrl": "https://www.tipranks.com/stocks/amzn/earnings",
    "sourceType": "monitoring",
    "verifiedAt": "2026-09-08",
    "call": {
      "eventType": "call",
      "timezone": "America/New_York",
      "expectedDate": "2026-10-29",
      "localTime": "17:00",
      "precision": "day",
      "status": "issuer-confirmed",
      "sourceUrl": "https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-to-Webcast-Third-Quarter-2026-Financial-Results-Conference-Call/default.aspx",
      "sourceType": "issuer-ir",
      "verifiedAt": "2026-10-20"
    }
  }
  ```

- **闭合的校验与时区规则（`static/invest/research/validate_earnings_calendar.py`）**：
  1. **主记录（`release`）规则零放松**：只有发行人原文明确了财报发布日及发布时段 `session in {"before-open", "after-close", "during-market"}` 时，主记录才能标为 `issuer-confirmed`。绝不从 `call.localTime` 推断 `release.session`，也不用仅确认了电话会的日期覆盖未确认的 `release.expectedDate`。
  2. **`call` 子对象必填与时区规则**：
     - 当存在 `call` 对象时，必须包含：`eventType: "call"`、`timezone`（合法的 IANA 时区字符串，由 `validate_timezone` 校验——例如 CDNS 的 `"14:00"` PT 必须显式写 `"timezone": "America/Los_Angeles"`，或换算为 `"America/New_York"` 的 `"17:00"`，严禁把 PT 钟点直接塞入默认 ET 时区）、`expectedDate`（`YYYY-MM-DD`）、`localTime`（`HH:MM` 24 小时制或 `"unspecified"`）、`precision: "day"`、`status: "issuer-confirmed" | "stale"`、`sourceType: "issuer-ir"`、HTTPS `sourceUrl`、`verifiedAt <= calendar.asOf`。
     - 当 `call.status == "stale"` 时，要求 `call.expectedDate < calendar.asOf`。
  3. **`earnings_tasks.py` 全状态覆盖与任务语义闭合**：
     - **Case 1（主记录 `release` 已是 `issuer-confirmed + day`）**：按主记录的 `timezone` 与 `expectedDate` 在 `T-1 / T / T+1` 生成 `type: "research-update"` 任务（与现状完全一致；若同时存在同日的 `call`，不重复生成第二条任务）。
     - **Case 2（主记录 `release` 尚非 `issuer-confirmed`，即 `release.status in {"estimated", "unknown", "stale", "recorded"}`，但存在 `call.status == "issuer-confirmed"`）**：
       - **不论主记录是 `estimated`、`unknown`、`recorded`，还是因早先预估日已过而被维护为 `stale`（例如 AMZN 的 `10-22` 预估日过期变为 `stale` 后，其 `10-29` 的 `call` 依然有效）**，均按 `call.timezone` 与 `call.expectedDate` 计算事件本地日偏移：
       - 在 `call.expectedDate` 的 **`T-1 / T / T+1`** 生成任务（`id: "earnings:<reportId>:call-<call.expectedDate>:<window>"`，`type: "research-update"`，`reason: "Issuer-confirmed earnings call window (release time unconfirmed); first verify actual release filing/press release, then update the research package."`）。
       - 当 `call.expectedDate` 已过 `T+1`（`(today - call_date).days > 1`）且主记录仍未更新至下一周期时，在每周一（`weekly`）生成 `calendar-maintenance` 任务，提醒维护人滚动周期。
  4. **禁止无变化的纯 `verifiedAt` 噪音提交**：在 `docs/earnings-update-automation.md` 中明确，若某条记录的日期、状态、`call` 子对象及来源均无新证据变化，不得提交仅刷新 `verifiedAt` 的 diff。

### 4.2 前端上屏：`monitoring-dashboard.html` 新增「14D Earnings & Catalyst Radar」
- **窗口与精度过滤规则**：
  1. **仅纳入日精度（`precision === "day"`）事件**：
     - 若某记录具有 `call` (`status: "issuer-confirmed"`) 且主记录 `release` 尚非 `issuer-confirmed`，雷达面板以 `call.expectedDate` 作为该记录的主展示锚点日（标注 `[Call Confirmed · HH:MM TZ]`，并在括号内附注主记录的 `Release: est YYYY-MM-DD / stale`）；
     - 否则以主记录 `precision === "day"` 的 `expectedDate` 作为展示锚点日。
     - **排除月精度与未知日期**：`precision === "month"`（如 `"2026-10"`）或 `precision === "unknown"`（`expectedDate: null`）且无日精度 `call` 的条目，**不进入** 14D 日级时间轴（仅在面板底部折叠区汇总结算为 `"N entries with month-only / unknown schedule"`）。
  2. **Upcoming 14D（`0 <= offsetDays <= 14`）**：
     - 以 `2026-10-20` 当日为例，合入 `call` 子对象后，`lam-research-2026` (`10-21`, T+1d)、`cadence-2026` (`10-26`, T+6d)、`eqix-2026` (`10-28`, T+8d)、`amzn-2026` (`10-29`, T+9d) 4 家将立即出现在未来 14 天窗口中；而 `vistra-2026` (`2026-11-06`, T+17d) 将于 `2026-10-23` 自动滑入 14D 窗口。
  3. **Recent Past-Due 14D（`-14 <= offsetDays < 0`）原值并列展示**：
     - v7 **不做** `fiscalPeriod === reportedPeriod` 的字符串自动相等判定（因存量 `reportedPeriod` 写法不统一）；
     - Past-Due 面板仅并列展示日历 `fiscalPeriod`（若已填）与报告 `reportedPeriod` 原值，供研究员直接对照。期间键规范化列入 `§6.2` 后置项。

---

## 5. Track 4 — 价格台账 `TLDR-7` 根因排查与序列完整性专项

### 5.1 先复现与定位 `TLDR-7`（4 个非美代码缺 `2026-10-12` bar）
- `docs/daily-research/2026-10-20-review.md:39`（位于 `origin/codex/daily-research-2026-10-20`（`96fa3a4`），不在 `main`）记录了 4 个亚太市场代码（`000660.KS`, `688676.SS`, `300308.SZ`, `0100.HK`）缺少 `2026-10-12` 收盘 bar（`TLDR-7`）。
- 由于 `static/invest/research/update_prices.py:418` 本来就通过 `yfinance` 拉取从 `min(anchors) - 10d` 到当日的日线区间，PR 5 必须**先采集同截点原始行情响应与企业行动（如 `300308.SZ` 在 `2026-10-12` 的除息事件），复现并定位缺口发生在源端还是 `completed_quotes()` 过滤环节**，并补齐日期边界测试。

### 5.2 `prices.json` 近期收盘序列扩展（在根因查明后实施）
- 待 `TLDR-7` 根因查明并完成可重放修复后，若下游需要计算个股短期异动，可在 `static/invest/research/data/prices.json` 的 `entries[]` 中增加可选的 `recentCloses` 数组（以下外层字段为 `main@bf7bf56` 上 `sk-hynix-2026` 的真实数据，`recentCloses` 内部为结构示意占位）：
  ```json
  {
    "reportId": "sk-hynix-2026",
    "symbol": "000660.KS",
    "status": "ok",
    "attemptedAt": "2026-10-19",
    "baseDate": "2026-07-31",
    "basePrice": 1718000.0,
    "lastDate": "2026-10-19",
    "lastClose": 1277000.0,
    "changePct": -25.7,
    "currency": "KRW",
    "recentCloses": [
      { "date": "<trading-day-1>", "close": "<split-adjusted-close>" },
      { "date": "2026-10-19", "close": 1277000.0 }
    ]
  }
  ```
- **严格计算门禁**：
  - 序列末点必须精确等于 `{ "date": lastDate, "close": lastClose }`；
  - 只有在**连续、完整、同一拆股口径（`splitEvents` 一致）与同一数据源**的已完成交易时段（`completed_quotes`）下，才允许计算 1D / 5D 涨跌幅（外部源如 Daum/新浪/腾讯不可混入充当统一行情源）；
  - 若序列存在缺日或口径不连续，必须降级显示，严禁跨缺口强算。
  - 同步更新 `static/invest/research/validate_prices.py`、**`test_update_prices.py`** 与 **`test_validate_prices.py`**。

---

## 6. Track 5 — 覆盖补强优先级与后置立项（Scope Convergence）

### 6.1 新覆盖标的优先级
1. **第一批（已完成立项）**：**ASMPT (`0522.HK`)**、**Besi (`BESI.AS`)** —— 落入 `semicap-equipment` 层。
2. **第二批（消除 `networking` 单点层）**：**Celestica (`CLS`)** —— 归入 **`networking`** 层（以 HPS 白盒 800G/1.6T 交换机和网络硬件为主线对标 `ANET`，机柜级集成作为与 `datacenter-facility` / `custom-merchant-silicon` 的交叉验证；立项时由 Owner 最终确认，不为它新开层）。
3. **第三批（补齐独立架构授权视角）**：**Arm Holdings (`ARM`)** —— 落入 `eda-ip` 层，补充独立 CPU 架构授权与版税率验证视角。

### 6.2 明确后置/单独立项的范围
以下四项从 v7 核心交付流中剥离，作为后续独立子项按需立项：
1. **交叉校验（`crossChecks`，现共 17 条）的上下游双腿状态机**；
2. **非链报告（14 篇）纳入 `verdicts.json` 的 `scope` 改造、ETF 自比豁免与基准桶映射**（以及非链 63 个未评级被引用监控项的 `reading` 回填）；
3. **存量 52 篇报告向 `moduleContract: "heading-comment-v1"`（11 模块显式注释）的批量迁移**；
4. **日历 `fiscalPeriod` 与报告 `reportedPeriod` 的期间键规范化（如 `fiscalPeriodKey: "FY2026Q3"`）及自动同步状态判定**。

---

## 7. Delivery slicing, preconditions & gates

门禁明确拆分为**「只读校验与单元测试（Read-Only Checks）」**与**「生成/构建一致性验证（Write/Build Verification）」**两栏：

| PR | 阶段与开工前置条件 | 核心交付内容与负责方 | 只读校验与单元测试（Read-Only Checks） | 生成/构建一致性验证（Write/Build Checks） |
|---|---|---|---|---|
| **PR 1** | **契约修订与 Reviewer 侧同步** | 1. **本文档定稿**（撰写 agent）。<br>2. **交付项 ⓐ（由 owner 授权的会话执行，不由撰写 agent 执行）**：修改 reviewer prompt（`~/.codex/automations/daily-alc-branch-review-gate/automation.toml`），写入 `§2.2-3` 三点定义（valuation 指估值数值；带日期边界标注是 Mode A 必填项不构成违约；Mode A 推进 `lastUpdate` 不动 `priceAsOf` 不算单刷 `lastUpdate`）。<br>3. **交付项 ⓑ（由 owner 授权的会话执行，不由撰写 agent 执行）**：按 `§1-1` / `§2.2` 裁决 1 重分类 reviewer `memory.md` 里的 `P-*` 条件，把每条 `P-*` 拆成「事实部分（Mode A 可闭合）」和「估值部分（继续 open）」，并体现在下一轮 `*-review.md` 中。 | **ⓐ 验收**：`automation.toml` diff 包含 `§2.2-3` 三点定义。<br>**ⓑ 验收**：`memory.md` 中 `P-25`、`P-27`、`P-34` 各自拆出「事实部分：已放行」行，并出现在下一轮 `*-review.md` 中。 | — |
| **PR 2** | **小型工程补齐**<br>*（前置：`DESIGN.md` 色值、`test_tracking_rules.mjs` 断言改写、全部当前链内 `downgrade` 必填三项已在本文档落实，可立即开工）* | 1. `static/invest/research/tracking-rules.js:95` 移除 `!report.chainLayer`；改写 `test_tracking_rules.mjs` 现有用例 `'non-chain and archived reports are skipped'`（非链腿改为期望出一行，archived 腿保留期望 `[]`；目标消费页为 `verdict-ledger.html`）。<br>2. `static/invest/research/update_verdicts.py` 保留原 `stale` 语义不变，仅新增 `monitoringOverdue: bool`；更新 `validate_verdicts.py`、`test_update_verdicts.py`、`test_validate_verdicts.py`。<br>3. `static/invest/research/validate_reports.py`：(a) 开启 `ENFORCE_NONCHAIN_FRESHNESS = True`；(b) 在 `validate_trigger_link_requirements()`（chain-only）中保持全部当前链内报告 `downgrade.monitoringIds` 必填，并新增 `stance != "bullish"` 时 `upgrade.monitoringIds` 必填；(c) 新增 `lastUpdate >= priceAsOf` 校验；更新 `test_validate_reports.py`。<br>4. 补齐 12 篇非链报告的 `coverageTier`（不受 `ENFORCE_COVERAGE_TIER` 门禁保护）与 14 篇链内报告的 `chainRole`。 | `python3.11 static/invest/research/validate_reports.py`<br>`python3.11 static/invest/research/validate_verdicts.py`<br>`python3.11 static/invest/research/validate_coverage_map.py`<br>`python3.11 -m unittest discover -s static/invest/research -p "test_*.py"`<br>`node --test static/invest/research/reports/report-module-parser.test.mjs static/invest/research/test_tracking_rules.mjs` | 运行 `python3.11 static/invest/research/update_verdicts.py` 更新 `data/verdicts.json` 后再次通过左栏只读校验。 |
| **PR 3** | **财报日历事件模型 + 前端 14D 雷达**<br>*（前置：`call` 任务去重键扩展声明、Past-Due 原值并列展示两项已在本文档落实，可立即开工）* | 1. 更新 `docs/earnings-update-automation.md`、`data/earnings-calendar.json`、`validate_earnings_calendar.py` 与 `earnings_tasks.py`，支持主记录 `release` + 子对象 `call`（含独立 `call.timezone`、全状态 `estimated/unknown/stale/recorded` 覆盖、去重键 `earnings:<reportId>:call-<date>:<window>`）与可选 `fiscalPeriod`；更新 `test_validate_earnings_calendar.py` 与 `test_earnings_tasks.py`。<br>2. 合入 AMZN (`10-29 17:00 America/New_York`)、LRCX (`10-21 14:00 America/Los_Angeles`)、CDNS (`10-26 14:00 America/Los_Angeles`)、EQIX (`10-28 17:30 America/New_York`)、VST (`11-06 10:00 America/New_York`) 的 `call` 记录；停止无变化的纯 `verifiedAt` 刷新。<br>3. `static/invest/research/monitoring-dashboard.html` 新增「14D Earnings & Catalyst Radar」（仅日精度入轴，月/未知精度折叠，Past-Due 并列展示日历 `fiscalPeriod` 与报告 `reportedPeriod` 原值，遵循 `DESIGN.md`）。 | `python3.11 static/invest/research/validate_earnings_calendar.py`<br>`python3.11 -m unittest discover -s static/invest/research -p "test_*.py"` | 运行 `python3.11 static/invest/research/earnings_tasks.py` 更新队列；运行 `hugo --minify` 验证构建通过后，还原构建产生的非目标工作区改动（如 `hugo_stats.json`）。 |
| **PR 4** | **CEG Mode A 首个试点 + 链内被引用项 `reading` 门禁**<br>*（前置：**须等 PR 1 的 ⓐⓑ 生效后再开**）* | 1. **首个试点（由 owner 的交互式会话执行，经每日 reviewer 审核合入）**：按 `§2.3-1` 提交 `constellation-energy-2026` 的 Brazos Valley 剥离交割 Mode A 包（只做 `§2.3-1` 所列三件事，不含任何估值数字）。<br>2. 试点通过后，推进第二批 Mode A 候选（`netflix-2026` / `wdc-2026` / `lam-research-2026` 及 TSMC/ASML 已放行事实腿）。<br>3. 在 `validate_reports.py` 新增 **chain-only** 的 `ENFORCE_LINKED_READING`（先 warn-first），为 54 篇链内报告的 84 个未评级被引用监控项补齐有据可查的 `reading`（证据不足或复合触发有未知腿填 `unclear`），warning 清零后切换为 `True`；更新 `test_validate_reports.py`。 | `python3.11 static/invest/research/validate_reports.py`<br>`python3.11 static/invest/research/validate_coverage_map.py`<br>`python3.11 -m unittest discover -s static/invest/research -p "test_*.py"` | `python3.11 static/invest/research/generate_feed.py && git diff --exit-code static/invest/research/feed.xml`<br>`hugo --minify`（验证后还原 `hugo_stats.json` 等构建副产物） |
| **PR 5** | **价格 `TLDR-7` 根因与序列专项** | 1. 复现并查明 4 个非美代码（`000660.KS`, `688676.SS`, `300308.SZ`, `0100.HK`）缺 `2026-10-12` bar 的真实根因。<br>2. 在解决缺日并补齐日期边界测试后，落地 `recentCloses` 与连续已完成交易日/拆股口径校验（更新 `validate_prices.py`、`test_update_prices.py`、`test_validate_prices.py`）。 | `python3.11 static/invest/research/validate_prices.py`<br>`python3.11 -m unittest discover -s static/invest/research -p "test_*.py"` | — |
| **PR 6+** | **后续新覆盖与独立子项** | 1. 按序交付 `0522.HK` (ASMPT) / `BESI.AS` → `CLS` (`networking`) → `ARM` (`eda-ip`) 深度报告。<br>2. Mode B 积压表（`P-21`, `P-34`, `P-27`, `P-25` 估值部分, `P-6`, `P-19`, `P-22`）按 owner 排期推进。<br>3. 17 条 `crossChecks` 双腿状态机、非链 `verdicts` 与期间键规范化另行独立设计立项。 | 全套仓库只读校验器 + `python3.11 /Users/kyx/.codex/skills/company-research-publishing/scripts/check_research_package.py static/invest/research` | `generate_feed.py` + `hugo --minify`（验证后还原非目标构建副产物） |

---

## 8. Acceptance criteria

- [ ] **PR 1 门禁全绿**：
  - ⓐ `~/.codex/automations/daily-alc-branch-review-gate/automation.toml` 的 diff 包含 `§2.2-3` 三点定义；
  - ⓑ reviewer `memory.md` 中 `P-25`、`P-27`、`P-34` 各自拆出「事实部分：已放行」行，并出现在下一轮 `*-review.md` 中。
- [ ] **PR 2 门禁全绿**：
  - `python3.11 static/invest/research/validate_reports.py` 退出码为 `0`（`ENFORCE_NONCHAIN_FRESHNESS = True`；链内全部报告 `downgrade.monitoringIds` 必填 + `stance != "bullish"` 时 `upgrade.monitoringIds` 必填开启；`lastUpdate >= priceAsOf` 校验开启；12 篇非链 `coverageTier` 与 14 篇链内 `chainRole` 全部补齐）。
  - `verdicts.json` 保持原有 `stale` 语义不变，且 7 篇存在月度监控逾期的 open verdicts 均正确暴露 `monitoringOverdue: true`（不加 `priceAnchorAgeDays`）；`test_update_verdicts.py` 与 `test_validate_verdicts.py` 全部通过。
  - `node --test static/invest/research/test_tracking_rules.mjs` 通过（现有用例 `'non-chain and archived reports are skipped'` 改写后，非链腿返回 1 行、archived 腿返回 `[]`；实盘 `verdict-ledger.html` 的 Trigger Watch 因现有 4 项 breach 均已在此后裁决立场，保持 0 行的健康状态）。
- [ ] **PR 3 门禁全绿**：
  - `python3.11 static/invest/research/validate_earnings_calendar.py`、`test_validate_earnings_calendar.py` 与 `test_earnings_tasks.py`（覆盖 `call.timezone`、扩展去重键 `earnings:<reportId>:call-<date>:<window>` 及主记录为 `estimated`/`unknown`/`stale`/`recorded` 时的 `call` 任务生成）全部通过。
  - AMZN、LRCX、CDNS、EQIX、VST 的官方电话会时间以 `call` 子对象（`issuer-confirmed` + 准确 IANA `timezone`）合规入库，不污染未确认的 `release` 日期或 `session`。
  - `monitoring-dashboard.html` 顶部渲染「14D Earnings & Catalyst Radar」（以 `2026-10-20` 为基准，LRCX/CDNS/EQIX/AMZN 4 家落入 T+14d 窗口，VST `11-06` 位于 T+17d；`precision: month/unknown` 正确排除出日级轴；Past-Due 条目并列展示日历 `fiscalPeriod` 与报告 `reportedPeriod` 原值），符合 `DESIGN.md` 视觉规范。
- [ ] **PR 4 门禁全绿**：
  - **CEG 首个 Mode A 试点通过标准（须同时满足以下三条）**：
    1. reviewer 在下一轮 review 中给出 `taken` / `taken (modified)`；
    2. `main` 上 `Constellation_Energy_深度研究报告_2026-07.md:22` 的措辞已改为交割事实（双语同步，且估值模块带 `§2.3-1` 规定的日期边界标注）；
    3. `priceAsOf` 与 `prices.json.baseDate` 仍为原锚，`priceAsOf == baseDate` 不变式保持 68/68。
  - **54 篇链内报告**被 `stanceTriggers` 引用的 250 个监控项 100% 具备有据可查的 `reading`（补齐剩余 84 项），chain-only `ENFORCE_LINKED_READING = True` 开启后 `validate_reports.py` 0 warning / 0 error。
- [ ] **PR 5 门禁全绿**：
  - 产出 `TLDR-7` 缺日根因复现结论与边界测试，`test_update_prices.py` 与 `test_validate_prices.py` 全部通过，任何新增的价格序列计算均具备「连续已完成交易日 + 同一拆股口径 + 末点对齐 `lastDate/lastClose`」校验与缺数降级保护。

---

## 9. Risks, gotchas & `DESIGN.md` guardrails

1. **严守 Mode A 与 Mode B 的算术边界与必填边界标注**：
   - Mode A 只允许修改非估值输入的事实陈述（含估值模块中的文字陈述），严禁把新指引或新数字代入估值算术；若新事实使现有估值口径过时，必须在双语估值模块与摘要估值引用处加带日期的边界标注（「估值仍按 YYYY-MM-DD 锚定的旧口径，<哪个输入> 待 Mode B 重算」）并列入 `§2.3-2` Mode B 积压表。
2. **严防 `call` 事件污染 `release` 证据等级或时区错配**：
   - 仅宣布电话会时间的官方公告只能写入 `call` 子对象，且必须填写与钟点匹配的 IANA `call.timezone`（如 PT 对应 `America/Los_Angeles`）。
3. **严防机械填 `within` 洗白监控项**：
   - 在补齐 84 个链内被引用监控项的 `reading` 时，凡公开披露口径未直接覆盖或复合触发器含未知腿（如 TSMC `n3-n2-ramp`），必须诚实标为 `"unclear"`。
4. **前端视觉反模式检查**：
   - 新增的 14D 财报雷达面板严禁使用 `#ef4444` / `#22c55e` 等红绿交通灯状态色；统一使用 `DESIGN.md:17-24` 规定的文字变量 `--primary` / `--content` / `--secondary` / `--tertiary`，以及 `--accent` (`#2f6fed`) 与 `--accent-alt` (`#0f9d8c`)。

---

## 10. 评审决议摘要（Review Log Index）

第 1～3 轮多 Agent 评审记录已完整归档至 [`docs/research-hub-v7-review-log.md`](research-hub-v7-review-log.md)，各章节索引如下（所有裁决全文已直接写入本文档 `§1`、`§2` 正文）：

- **[Round 1 Review（Claude × Codex）](research-hub-v7-review-log.md#11-review-round-1--claude-opus-55--codex-gpt-6-astra2026-10-20)**：
  - [`§11.1` 事实与字段勘误](research-hub-v7-review-log.md#111-必须更正的事实错误0-及正文引用处一并改) · [`§11.2` 设计异议](research-hub-v7-review-log.md#112-设计层面的异议两方一致) · [`§11.3` 开放问题回复（Q1–Q5）](research-hub-v7-review-log.md#113-10-开放问题的回复) · [`§11.4` 建议 PR 顺序](research-hub-v7-review-log.md#114-建议的-pr-顺序替换-7)
- **[Round 2 Review（Claude × Codex）](research-hub-v7-review-log.md#12-review-round-2--claude-opus-55--codex-gpt-6-astra2026-10-20)**：
  - [`§12.1` P1 阻塞项（Trigger Watch、`reading` 门禁范围、`call` 时区与任务、生成器名、试点条件）](research-hub-v7-review-log.md#121-p1-阻塞项执行前必须修正) · [`§12.2` P2 准确性问题](research-hub-v7-review-log.md#122-p2-准确性问题) · [`§12.3` R2-1~R2-3 确认点结论](research-hub-v7-review-log.md#123-对-10-r2-确认点的回复) · [`§12.4` 开工条件](research-hub-v7-review-log.md#124-进入执行的条件经-round-4-指令同步更新) · [`§12.6` 审核实践中事实与估值绑定的实证](research-hub-v7-review-log.md#126-对-round-1-结论的更正事实与估值强绑定在审核实践中确实存在)
- **[Round 3 Review（Claude × advisor）](research-hub-v7-review-log.md#13-review-round-3--claude-opus-55--advisor-fable-52026-10-20)**：
  - [`§13.1` Mode A 按事实类别准入、Reviewer `memory.md` 收窄与 CEG 试点](research-hub-v7-review-log.md#131-核心问题126-的四条修订要求正文一条都没有落实) · [`§13.2` 实测细节勘误（9 项；第 10 项 `priceAnchorAgeDays` 见 `§13.3`）](research-hub-v7-review-log.md#132-修订新引入的错误均已实测) · [`§13.3` 架构判断与进入执行的条件](research-hub-v7-review-log.md#133-架构判断与进入执行的条件)
