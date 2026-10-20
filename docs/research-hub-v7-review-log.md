# Research Hub v7 Plan — Multi-Agent Review Log (Rounds 1–3)

本文件原样归档 [`docs/research-hub-v7-plan.md`](research-hub-v7-plan.md) 的第 1～3 轮多 Agent 评审记录（`§11`–`§13`）。例外：原修订 agent 写的「§12.5 Round 2 修订逐条核对表」属于自评打勾，与第四轮指令「不要自评打勾」冲突，已省略；`§12.4` 与 `§12.6` 中标注的段落为第四轮同步更新。主计划文档正文已吸纳全部裁决与修订并保持独立自包含。

---

## 11. Review round 1 — Claude (Opus 5.5) × Codex (gpt-6-astra)，2026-10-20

> 两个 agent 各自独立对 `main@bf7bf56` 与缓存分支 `origin/codex/daily-research-2026-10-20@96fa3a4` 复算，结论高度一致。**总评：方向（事实/估值双轨、日历上屏、非链纳入 Trigger Watch）值得做，但草案把数项既有设计误判为 bug、存在关键统计错误与契约错配，当前 §7 的 5 个 PR 不能照单实施——请先按本节修订正文再进入执行。** 以下为给修订 agent 的逐条指令；两方分歧处已单独标注，留 owner 裁决。

### 11.1 必须更正的事实错误（§0 及正文引用处一并改）

| 位置 | 草案写法 | 实测（`main@bf7bf56`） | 修订要求 |
|---|---|---|---|
| §0-7、§3.2、§7 PR4、§8 | `upgrade.monitoringIds` 仅 13/54，「回填剩余 41 篇」 | **链内 54/54、非链 14/14 均已有** | 删除「回填 41 篇」工作项；§3.2 只保留「是否把 upgrade 链接也纳入强制校验」这一条（当前已满足，开门禁即可） |
| §0-8、§3.1 | `update_verdicts.py:243` 的 `and` 是 bug | **这是 v5 锁定契约**：`docs/research-hub-v5-stance-conviction-plan.md:37,147` 明写「>120d AND any monitoring nextCheck passed」；实现与设计一致 | 改为「契约修订提案」，不得称修 bug（见 11.2-④） |
| §3.3 | 被引用项 `reading` 强制非空是「消除盲区」 | v6 锁定：`validate_reports.py` 注释「reading itself stays optional forever (absence = not yet graded)」 | 明确写成**修改 v6 契约**的迁移；167/349、链内 94/266、11 篇全空的统计属实。补充：被 trigger 引用的监控项链内 250 项中 84 项无 reading；全部当前报告合计 322 项中 147 项无 reading |
| §3.3、§3.4 | Trigger Watch 渲染 `breached / unclear / within` 三态 | `tracking-rules.js:95` 只列「breached 且立场未变」的项，不是三态总览 | 若要三态面板，按新功能写，不要描述成现状被阻断 |
| 全文 | `scripts/*.py` | 脚本实际在 `static/invest/research/`（`validate_reports.py`、`update_verdicts.py`、`update_prices.py`、`validate_earnings_calendar.py`…）；`generate_briefing.py` 不在 main | 全部路径改正 |
| §7 门禁列 | `update_verdicts.py --check`、`update_prices.py --check`、`generate_briefing.py --dry-run`、`node scripts/test_tracking_rules.js` | 这些 flag 不存在：价格/verdict 生成器会忽略未知参数、照常**写盘**；briefing 的 `--dry-run` 会被参数解析器拒绝；测试文件是 `static/invest/research/test_tracking_rules.mjs` | 门禁只写真实存在的只读命令/测试；需要 `--check` 就把它列为交付项 |
| §4.1、§4.2 | 字段 `nextEarningsDate` / `timeOfDay` / `BMO` / `AMC` | 实际字段 `expectedDate` / `session`（`before-open` / `after-close` / `during-market` / `unspecified`） | 改用真实 schema |
| §5.1 | `prices.json` 示例（ticker 为 key、`lastCloseDate`、SK hynix 价格） | 实际是 `entries[]`，键 `reportId`/`symbol`/`lastDate`；示例数值非 main 数据 | 示例改成真实结构，不得编造价格 |
| §6.3 | 8 个 H2 注入 `<!-- module:M1..M8 -->`，正文是 HTML | 正文是**双语 Markdown**；`heading-comment-v1` 是 **11 个语义模块**（`static/invest/research/README.md` §研报模块语义契约） | 按 README 契约重写 |
| §0-4 | 显式契约 16 篇 =「链内 15 + 非链 rklb」 | 16 = **链内 12 + 非链 4** | 更正 |
| §0-6、§2.3 | `\|changePct\| >= 25%` 12 篇 | **13 篇** | 更正 |
| §6.1 | 9 条 crossChecks | **17 条** | 更正 |
| §0-6 | 「`P-2..P-34` 有 40 项 deferred」 | 40 是全部 open 项，其中 `P-*` 仅 26 项 | 更正 |
| §0-9、§4.2 | AMZN/LRCX/CDNS/EQIX/VST 被 reviewer「误杀」 | review 第 17/40/50 行：发行人原文**只确认电话会**，reviewer 明确给出重开条件「可读发布日原文，**或**单独测试区分 call 与 release 的事件模型」。这不是误杀，是缺事件模型 | 改写为「缺 call/release 事件模型」 |
| §4.2 | VST `2026-11-05` | 官方稿：**2026-11-06 10:00 ET** | 更正 |
| §0-2、§6.2 | `eda-ip`「IP 核为 0 家」 | SNPS 报告已覆盖 Design IP；ARM 补的是**独立 CPU 架构授权/版税**视角 | 改措辞 |
| §10 Q2 | `tsla-2026` 举例为非链 | `tsla-2026` 当前**是链内** | 换例子 |

### 11.2 设计层面的异议（两方一致）

1. **Track 1A「T+48h 合入 main」SLA 不可行** — 与 `docs/earnings-update-automation.md` 的责任边界冲突（研究执行人→Reviewer→Integrator），且 `reading` 是判断不是纯事实搬运。改为：**48h 内完成证据核验、初审与阻塞记录**；合入仍须过 review。
2. **Track 1A 不能规定「只改 M7、禁止碰 M5」** — 应按影响范围同步双语正文、摘要、情景与理由；旧估值可保留（标 `Price / Valuation anchored as of …`），但被新事实证伪的前提必须改。main 上已有先例：SNPS 做过事实更新但未重算估值（`Synopsys_深度研究报告_2026-07.md:22`），所以「门禁把事实与估值强绑定、普遍锁死」的诊断不成立。ASML/MU/TSMC 的 defer 条件里含具体口径缺陷，不能一概按「双轨」解除，需逐项看 review 理由。
3. **日历状态用错** — `recorded` 的契约含义是「报告正文已有日期、尚待 IR 复核」（`earnings-update-automation.md:32`），不能拿来表示「事实已同步」。需要另设研究处理状态（或放到 `earnings-tasks.json`）。
4. **§3.1 新 stale 定义自相矛盾** — `valuationStale` 用 90 天，汇总 `stale` 却用 120d+60d 且不引用它（价格锚 91 天、持有 81 天、无逾期 → `valuationStale=true, stale=false`）。**建议保留原 `stale` 语义**，另外**独立暴露** `monitoringOverdue`（以及价格锚年龄）供台账/简报展示；事实刷新不能清除估值陈旧。
5. **§4.2 `call-webcast` → `issuer-confirmed` 违反现有契约** — `issuer-confirmed` 强制要求 `session` 明确（`earnings-update-automation.md:33`），而电话会稿恰恰不给发布时段；草案的「盘后电话会⇒AMC」是推断，会把推断洗成发行人确认。正确做法：日历记录拆出**事件类型**（`release` / `call`），允许以 `eventType: call` 落地发行人确认的电话会日期（AMZN 10-29 17:00 ET 由此上屏）；`release` 事件的日期与 `session` 保持原 `estimated` / `unspecified`，直到读到发布原文（现 10-22 是未确认估计，10-29 电话会也不能证明实际发布日，不得直接替换 release 日期）；日期已过也不能自动认定「已发布」。需配 validator、任务生成与时区测试。
6. **§5.1 recentCloses 承诺过头** — review 第 39 行把 `TLDR-7`（4 个非美代码缺 `10-12` bar）的根因保留待查，缺口发生在哪个环节**尚未证实**；`update_prices.py` 本就用 yfinance 拉日线区间，若缺口在源端，新数组同样缺，存储数组本身不能证明或修复缺日。只有**连续、完整、同一拆股口径**的已完成交易时段才能算 5D，缺数必须降级显示。briefing 分支目前也没实现个股 1D/5D，不能说成「被此阻塞」。先复现缺日，再加序列与校验。
7. **§0-5「防御性偏误」证据不足** — cautious 桶相对 SMH 为负不能证明「过早谨慎」；`calibration_history.py:119` 的 beatRate 统计的是跑赢比例而非方向准确率。保留为观察，不作为推动 upgrade 回填/立场调整的依据。
8. **范围收敛** — 双腿交叉校验状态机（§6.1）、非链 verdict（§5.2-3）、「触碰即迁移」模块契约（§6.3）宜后置或单独立项，避免把一次事实修订扩大成结构迁移。

### 11.3 §10 开放问题的回复

| 问题 | Codex (astra) | Claude | 建议给 owner 的结论 |
|---|---|---|---|
| **Q1** factsAsOf | 新增独立 `factsAsOf`，**禁止回退** `lastUpdate`；仅表示「一次明确范围的事实复核完成日」，局部指标更新只推进该项 `readingAsOf` | 倾向**暂不新增**：Tier 1「已发报未同步」可由 `earnings-calendar` + `reportedPeriod` 推导，单项新鲜度已有 `readingAsOf`，现阶段没有下游非它不可 | **分歧，owner 定**。共识底线：若加，绝不回退 `lastUpdate`，也不能用来「洗新」整篇 |
| **Q2** 非链 verdict | **B**：先进 Trigger Watch；非链 verdict 另做迁移（open/closed 的 scope、基准选择、ETF 自比、校准过滤都要处理，现汇总不按 scope 过滤，直接放开会默认落到 SMH） | 同意 B | **B** |
| **Q3** reading 强校验范围 | **A**：只强制被 trigger 引用的项，附日期与证据；证据不足填 `unclear`；须写明是修改 v6 契约 | 同意 A；先在 11 篇全空报告上做试点再开门禁 | **A**（warn-first → enforce，沿用 ENFORCE_* 模式） |
| **Q4** call-webcast 自动映射 | **反对**自动映射发布时段 | 反对；见 11.2-⑤ 的事件类型方案 | **拆 release/call 事件类型，不推断 session** |
| **Q5** 新覆盖优先级 | ASMPT/Besi → **CLS** → ARM | 同意；CLS 落 `datacenter-facility` 还是 `networking` 须先定层 | **ASMPT/Besi → CLS → ARM** |

### 11.4 建议的 PR 顺序（替换 §7）

1. **契约修订（本文档）**：纠正 11.1 的事实、字段与路径；写清事件类型模型、Track 1A 边界、SLA 改写、真实验证命令。
2. **小型工程补齐**：非链进入 Trigger Watch；`verdicts.json` 独立暴露 `monitoringOverdue`（**保留原 `stale` 语义**）；开启已经 0 warning 的 `ENFORCE_NONCHAIN_FRESHNESS`；补 12 篇非链 `coverageTier`、14 篇链内 `chainRole`。
3. **日历事件模型 + 前端雷达**：release/call 分离，联动 validator、任务生成与时区测试，再上屏 14D 面板；无变化的 `verifiedAt` 刷新不提交。
4. **事实更新试点**：挑 1–2 篇（如 ASML/TSMC），逐报告修双语受影响主张、signal 与关键 reading；验证可行后扩大，并开启被引用项 reading 门禁。
5. **价格专项**：先复现 `TLDR-7` 缺日，再加序列与校验；briefing 分支独立审查，个股 1D/5D 另列需求。
6. **后续内容与分析**：ASMPT/Besi → CLS → ARM；交叉校验双腿状态与非链 verdict 分别立项。

> 复核记录：两方均运行了 reports / earnings-calendar / prices / verdicts 四个只读校验器，全部通过；本轮未改动任何数据或代码文件。远端分支状态因 DNS 失败未能在线确认，以本地缓存 `96fa3a4` 为准。

---

## 12. Review round 2 — Claude (Opus 5.5) × Codex (gpt-6-astra)，2026-10-20

> 两方再次独立对 `main@bf7bf56` 复算（Codex：5 个校验器、23 个 Node 测试通过；Claude：对 `tracking-rules.js` 做内存实跑），结论一致。**总评：Round 1 的统计、字段与定性错误大部分已改正（§11.1 17 项中 12 项已落实，§11.2 8 条中 4 条已落实），但仍不能整套进入执行——下列 P1 阻塞项需在 Round 3 修订；§11.5 中「全部已修正」的表述目前不成立，请删掉或改为逐条状态。** 行号 `L` 均指 Round 2 修订版。

### 12.1 P1 阻塞项（执行前必须修正）

1. **Trigger Watch 的「3 篇 4 项上屏」是新引入的错误，PR 2 的验收标准按现状会失败**（L23、L91–93、L220、L233）
   - 规则是 `stanceDate <= item.readingAsOf`（`tracking-rules.js:104`），即「breach 之后立场还没动过」才进表。`alab-2026`（立场 10-11 / breach 08-05）、`salesforce-2026`（08-28 / 08-27）、`spotify-2026`（10-02 / 08-04）立场都是在 breach **之后**重新裁决的，所以都应被排除。
   - 实跑：`buildTriggerWatchRows(reports)` 现在返回 **0 行**；去掉 `!report.chainLayer` 之后**仍是 0 行**。「表为空 = 健康状态」正是页面文案的设计。
   - Trigger Watch 渲染在 **`verdict-ledger.html`**（L638 消费），不在 `monitoring-dashboard.html`。
   - **修订要求**：保留「移除链内过滤」这一改动（属于前瞻性修正），但验收改为 `test_tracking_rules.mjs` 中的**合成用例**（非链报告 + 已链接的 breached 项 + 立场早于 breach → 出现一行）；删掉所有「salesforce/spotify 上屏」的承诺，目标页面改为 `verdict-ledger.html`。
2. **`reading` 门禁范围前后不一致**（L80、L86–88 vs L222、L240）
   - §3.3 写的是「所有被引用项」（全库 322 项缺 147），PR 4 和验收却只回填、只验收链内（250 项缺 84）；非链还有 72 项缺 63。若照 L86 的范围开启 `ENFORCE_LINKED_READING`，PR 4 结束时 warning 不会清零。
   - L80 的「所有当前报告（或当前链内报告）」也必须二选一。
   - **修订要求**：明确定为**先 chain-only**（与 `validate_trigger_link_requirements` 现有的 `is_current_chain_report` 范围一致），非链 63 项另列后续批次；或者把这 63 项纳入 PR 4 的回填与验收。
3. **`call` 事件的任务生成与时区规则未闭合**（L140、L144、L153）
   - L144 只覆盖 release 状态为 `estimated` / `unknown` 的情况，漏了 `stale` / `recorded`。AMZN 的 10-22 估计过期后若被维护为 `stale`，按拟议规则就可能**漏掉 10-29 的电话会提醒**（状态不会自动转换，但维护后会落入这个漏洞）。
   - L140 说 `call.localTime`「按记录的 `timezone` 解释」，但日历默认时区是 `America/New_York`，CDNS 的 `14:00 PT` 原样套上去就是错的。`call` 需要自带 IANA `timezone`（或统一换算成 ET 后存储，并在 notes 保留原文时间）。
   - **契约演进未声明**：`earnings-update-automation.md:33` 规定「只有 `issuer-confirmed` release 可触发正式研究更新」。L144 让 `call` 也生成 `research-update`，这是改契约，必须写明。建议在 call 日期生成的任务 reason 写「先核实 release 原文，再做研究更新」，或者另设任务类型。
4. **生成器与日期校验的描述不实**（L50、L59）
   - `calibration_history.py` 是函数库，直接运行退出码为 0 但什么也不生成；实际入口是 **`update_calibration_history.py`**。
   - L59 称「校验规则确保 `lastUpdate >= priceAsOf`」，但 `validate_reports.py:827` 只校验日期格式。现存数据 0 违例，所以加这条规则很便宜，但应列为 **PR 2 的交付项**，不能写成现状。
5. **Mode A 试点与逐报告 review 条件不一致**（L222）
   - ASML (`P-34`) / TSMC (`P-27`) 被 defer，有一部分原因是 review 要求补齐当前估值桥等完整包。「换成 Mode A」本身不能解除这些条件。
   - **修订要求**：试点前逐条列出该报告在 `2026-10-20-review.md` 中的 defer 理由，并说明 Mode A 包如何满足每一条；不满足的，换一个阻塞条件纯属事实口径的报告来做试点。

### 12.2 P2 准确性问题

- **门禁列混入写盘命令**（L215、L217、L221–222）：`generate_feed.py` 会写 `feed.xml`，`hugo --minify` 会写构建产物（并可能改动 `hugo_stats.json`；验证后只还原本次构建造成的变化）。请分成「只读校验」和「生成后 `git diff` 检查」两栏，去掉「全部只读」的表述。
- **测试文件名不存在**（L74、L220、L223）：没有 `test_verdicts.py` / `test_prices.py`。实际文件是 `test_update_verdicts.py`、`test_validate_verdicts.py`、`test_update_prices.py`、`test_validate_prices.py`。
- **外部检查器路径**（L224）：`check_research_package.py` 不在本仓库，按 `static/invest/research/README.md:92` 写全路径 `/Users/kyx/.codex/skills/company-research-publishing/scripts/check_research_package.py`。
- **`prices.json` 示例里的历史价格无来源、未证实**（L185–186）：`1245000` / `1252000` 查不到出处；而且 `2026-10-12` 正是 `TLDR-7` 缺的那根 bar，示例等于凭空补上了缺口。序列末点也没对上 `lastDate`。改用 `…` 占位，或者标明「示意值」。§11.5 的「实盘数值」只适用于 L174–183。
- **14D 窗口承诺**（L153）：从 10-20 到 VST 的 11-06 是 17 天，五家不能「全部」进入 14D 窗口。
- **Recent Past-Due 面板**（L156）：要说明 `precision: month` 和 `expectedDate: null` 的记录怎么处理。
- **研究处理状态缺位**（§11.2-③ 部分落实）：L156 已不再挪用 `recorded`，但仍没有「已发报、研究包已同步」的落点。现在只能靠人工判断，面板无法区分「待同步」和「已同步」。候选方案：给 `earnings-tasks.json` 新增任务关闭状态（现有队列没有，属于新契约），或者用 `reportedPeriod` 对照 `fiscalPeriod`；请选定一个。

### 12.3 对 §10 R2 确认点的回复

| 确认点 | 两方意见 | 结论 |
|---|---|---|
| **R2-1** `call` 挂载形态 | 两方均选 **(A) 主记录 + `call` 子对象**：保留 `reportId` 唯一索引，兼容现有 release 消费者，改动最小 | **A**，前提是补上 12.1-③ 的 `call.timezone`、状态覆盖和任务契约 |
| **R2-2** `factsAsOf` | Codex 维持「若引入须独立、禁止回退」的立场，但同意**暂缓**、不阻塞其余修正；Claude 同意暂缓 | **v7 暂缓**；PR 4 试点后若确有下游需要再加 |
| **R2-3** `CLS` 定层 | 不阻塞 v7 核心 PR。Codex 选 **`networking`**：首覆以交换机和网络硬件为主线，与 ANET 对照，机柜集成作为交叉验证。Claude 同意，前提是论点确实以 HPS 白盒交换机为主；`datacenter-facility`（EQIX/VRT/DLR 都是设施/电力冷却）不贴切 | **倾向 `networking`**，owner 在立项 CLS 报告时确认；不为它新开层 |

### 12.4 进入执行的条件（经 Round 4 指令同步更新）

- **PR 2（小型工程补齐）**：前置为 Round 4 指令第三节第 1–3 项（`DESIGN.md` 色值、`test_tracking_rules.mjs` 现有断言改写、恢复全部当前链内报告 `downgrade` 必填）。
- **PR 3（日历事件模型）**：前置为 Round 4 指令第三节第 4–5 项（`call` 任务 id 去重键扩展声明、Past-Due 面板只并列展示 `fiscalPeriod` 与 `reportedPeriod` 原值）。
- **PR 4（事实更新试点）**：须等 PR 1 的 ⓐ（reviewer prompt 更新）与 ⓑ（reviewer `memory.md` 中 `P-*` 条件重分类）生效后再开。
- PR 2 和 PR 3 都不依赖 PR 4，可以先行。

### 12.6 对 Round 1 结论的更正：「事实与估值强绑定」在审核实践中确实存在

> 本节来自两方审视每日流水线时的新证据，修正 §11.2-② 与本节 12.1-⑤ 的部分判断。

- §11.2-② 写的是「『门禁把事实与估值强绑定、普遍锁死』的诊断不成立」，依据是 SNPS 先例和 sentinel 契约（`~/.claude/scheduled-tasks/daily-research-sentinel/SKILL.md`「Chain reports」节允许只更新监控读数、保留旧估值快照，前提是双语正文标明历史价格边界）。**校验器代码和生产方契约层面，这个判断成立；但 Codex reviewer 的实际审核尺度比契约更严，绑定确实存在**：
  - `2026-10-20-review.md` 中 `P-27`（TSMC）写明重开须「…估值／情景、显式立场复核、双语旧锚处理及精确 monitoringRefs signal **同批完整包；不单刷 latest／日期**」；`P-34`（ASML）同样写「**不单刷 latest／lastUpdate**」；`P-21`（Micron）自 09-30 起要求 EV 口径、资本开支桥与立场裁定一并提交。
  - Codex 另查到 CEG：reviewer 已独立读过交割稿，仍等待完整估值包，main 正文至今写着「交割尚待 DOJ 批准」（`Constellation_Energy_深度研究报告_2026-07.md:22`；reviewer memory `:286`）。
  - 10-10 至 10-20 共 11 次 reviewer 主会话，main 上落地 12 笔研究数据提交（其中 `research(calendar|signal)` 8 笔，另 4 笔为 kla/nrg/glw/amkr 单条记录），**零笔财报事实驱动的报告更新**。窗口内唯一改动报告正文的是 `df7c5cd`（alab 立场重裁），它是 owner 当天下午单独发起的重审，不属于每日流水线产出。
  - **绑定的位置**（Round 3 advisor 实测）：reviewer automation 的 prompt 本身已允许「New factual reading … monitoring latest/nextCheckDate、双语审计轨迹、lastUpdate」；「不单刷 latest／完整包」来自 reviewer `memory.md` 继承的 `P-*` 重开条件（`:239`、`:241`、`:248`）。因此**只改 prompt 不够，必须由 owner 裁决改写或收窄 memory.md 里的 `P-*` 条件**。
- **修订要求**：
  1. Track 1 的问题陈述恢复为「事实更新在 reviewer 实践中被完整估值包绑定」，证据引用上面的 review 条目，**不要**写成校验器限制。
  2. Mode A 必须同时成为 **reviewer 侧的明确准入规则**：写进 reviewer automation 的 prompt，**并**由 owner 裁决收窄 reviewer `memory.md` 中把事实更新捆进完整包的 `P-*` 条件。否则仅改本文档不会改变实际结果。
  3. 12.1-⑤ 的「换一个阻塞纯属事实口径的报告做试点」仍成立，但试点的目的就是验证 reviewer 是否接受 Mode A 包；CEG 交割事实是更合适的首个试点（证据已被 reviewer 读过、只涉及事实主张）。
  4. 需要完整估值包的积压（MU 自 09-30、ASML 自 10-15、TSMC 自 10-16）必须有明确的执行负责人和处理时间；目前三条自动任务里没有一条负责执行完整包：日历 routine 只上报，sentinel 只提 proposal，reviewer 只 defer。

---

## 13. Review round 3 — Claude (Opus 5.5) × advisor (Fable 5)，2026-10-20

> 两方独立对 `main@bf7bf56` 复算（advisor：5 个校验器 exit 0 / 0 WARN，`unittest` 168 OK，node 23/23；§0 全部计数逐项复现）。**总评：作为 Round 3 sign-off 判 NO-GO；但 PR 2 / PR 3 在 13.3 的廉价修订后可先开工。** §12.1 ①–⑤ 与 §12.2 ①–⑦ 的格式、路径、测试名、门禁拆分、计数基本都已落实，但修订稿把最大的瓶颈固化成了规则：附录诊断对了，正文没有一个 PR 指向它。注：原「12.5 对 Round 1 结论的更正」已改编号为 **§12.6**，与修订 agent 的「12.5 核对表」区分。

### 13.1 核心问题：§12.6 的四条修订要求，正文一条都没有落实

正文 §0–§10 对 `automation`、`prompt`、`负责人`、`积压`、`CEG` 零命中（L4 仍是 `Owner: (unassigned)`；§12.5 核对表全部打 ✅，但不覆盖 §12.6）。更关键的是，修订稿把「事实被完整包绑定」从待解决的问题改写成了正式原则：

- §1-1 与 §2.1 Mode A 的硬约束 1 规定：「最新 `review.md` 中**不存在** `P-*` 具名估值重开条件」才能走 Mode A。
- 可是现存积压**几乎每一项**都带这类条件：P-6 金盘、P-19 中际旭创、P-21 Micron、P-22 Synopsys、P-25 CEG、P-27 TSMC、P-34 ASML。
- 这些条件又是 reviewer 自己写的，所以规则成了**闭环**：reviewer 只要给某个事实更新附上一条估值条件，它就永远只能走 Mode B；而 Mode B 在三条自动任务里没有执行者。结果是新规则把现状正式化了，不是在解决它。
- **自相矛盾**：§12.6 建议用 CEG 交割做首个试点，但 review `P-25`（`96fa3a4` 第 178 行）与 `C-39`（第 225 行，reviewer `memory.md:286`）明文写着 CEG 交割「随 P-25 完整包」处置。按 §2.1 的规则 1，CEG 不能走 Mode A。§9-1 的列表也漏了 P-25。

**修订要求**

1. **改写 Mode A 准入**：不再看「review 里有没有 `P-*` 条件」，而是看「这条事实本身是不是估值输入」。
   - **能走 Mode A：** 交割完成、订单或出货数据、监控指标读数、指引文字。这些不改估值分母，即使所属报告挂着估值条件，也可以带着 `Price / Valuation anchored as of …` 声明先行落地；估值条件继续 open。
   - **只能走 Mode B：** 期末股本、净现金/债务、FX、倍数分母本身就是估值输入。
   - 这样 TSMC P-27 中 reviewer 已闭合或 `taken` 的监控行（`advanced-node` 当季腿、`cowos`、`customer-concentration`）、ASML 的订单读数、CEG 交割，都可以先行；估值桥留在 Mode B。
2. **在 §7 PR 1 加入两个交付项**：
   - ⓐ reviewer automation prompt 写入上述 Mode A 准入规则，并由 owner 裁决收窄 reviewer `memory.md` 里把事实捆进完整包的 `P-*` 条件（绑定实际在 memory.md 的继承条件里，见 §12.6；只改 prompt 不够）；
   - ⓑ 为 Mode B 积压（P-21 自 09-30、P-34 自 10-15、P-27 自 10-16、P-25、P-6、P-19、P-22）指定执行负责人和排期：owner 手动，或新开一个每周的重锚任务。在 L4 填写 Owner。
3. **PR 4 首个试点改为 CEG 交割**（按上面第 1 条，它属于 Mode A）。§2.3 路径 4A 的 netflix/wdc/lam 保留为第二批。
4. **结构性隐患（建议同批处理）**：Mode A/B 的准入依据是 `*-review.md` 和 `P-*` 清单，可前者只存在于会被删掉的日分支，后者在仓库外的 reviewer `memory.md`，实现者无法核对。建议把当前开放的 `P-*` 清单（id、reportId、条件分类为事实或估值、开立日期）作为一份仓库内文件维护，由 reviewer 写、producer 读。

### 13.2 修订新引入的错误（均已实测）

| 位置 | 问题 | 实测 | 修订 |
|---|---|---|---|
| L36、L270 | DESIGN.md 色值：`--accent #9e6b3b`、`--accent-secondary #3f5f72` | `DESIGN.md` 实为 `--accent #2f6fed`、`--accent-alt #0f9d8c`；全库搜不到 `9e6b3b`、`3f5f72`、`accent-secondary` | 改为真实变量名，或只保留「禁用交通灯色」原则，不写具体值 |
| L109、L235、L248 | 只写「新增合成用例」 | `test_tracking_rules.mjs` 现有用例 `'non-chain and archived reports are skipped'` 断言非链 → `[]`；移除 `!report.chainLayer` 后**必然失败** | 写明改写该断言：非链腿改为期望出行，archived 腿保留 |
| L87 | `stance != "bearish-avoid"` 时 downgrade 才必填 | 现 `validate_reports.py:430-441` 对全部 54 篇链内（含 coreweave、alab 两篇 bearish-avoid）强制 downgrade；新写法是**放宽** | 恢复「全部链内 downgrade 必填」，或按 §1-3 显式声明放宽 |
| L159 | call 任务 id `earnings:<id>:call-<date>:<window>` | 改变了 `docs/earnings-update-automation.md:59` 锁定的去重键 `earnings:<reportId>:<expectedDate\|unknown>:<window>`，§4.1 契约演进声明没有提到 | 在 §4.1 契约演进声明中补上这一条 |
| §4.2 L172–175 | `fiscalPeriod === reportedPeriod` 字符串相等判断同步状态 | 现存 `reportedPeriod` 写法不统一：`Q2 2026`(24)、`2026Q2`(4)、`Q3 FY2026`、`FY2026 Q3`、`Q2 2026 monitoring / 2026-07-30 valuation frame`(5)、`H1 2026`、`June 2026 quarter`…；直接相等会大面积误判为 Pending Sync | 改为规范化的期间键（如 `fiscalPeriodKey: "FY2026Q3"`，由日历和报告各自显式给出），或 v7 先只展示原值、不做自动判定 |
| L26、L182 | `TLDR-7` 在 `review.md:42` | 实际在 `:39`（`:42` 是 `TLDR-C3`） | 改为 `:39` |
| L13、L22 等 | 引用 `docs/daily-research/2026-10-20-review.md` | 该文件不在 main，只在 `origin/codex/daily-research-2026-10-20`（`96fa3a4`）上 | 引用时注明分支和 SHA |
| L20 | `coverageTier` 校验在 `validate_reports.py:139-147` | 实际在 `:619-656`，且 `ENFORCE_COVERAGE_TIER` 只对链内强制 | 更正行号；补非链 `coverageTier` 时说明它不受门禁保护 |
| L21 | `calibration_history.py:119` | `:119` 是 `def _summary`，beatRate 在 `:121-122` | 更正行号 |

### 13.3 架构判断与进入执行的条件

- **PR 2 的四项在 main 上全是零增量**：Trigger Watch 改前改后都是 0 行，upgrade 链接已是 54/54，`lastUpdate >= priceAsOf` 0 违例，NONCHAIN_FRESHNESS 0 warning。它们属于防退化的门禁，值得做，但不解决问题。PR 3 是真功能，属于日历管道。**唯一碰到瓶颈的 PR 4，又以「通过 Reviewer 门禁」验收**，而 reviewer 规则不变就不会放行。所以 13.1 的修订才是 v7 的主体，不是附录。
- **可以删掉的过度设计**：`priceAnchorAgeDays` 可由前端从 `priceAsOf` 即时算出，没必要写进 `verdicts.json`。
- **开工条件**
  - **PR 2：** 修完 13.2 的 DESIGN.md 色值、测试断言、L87 放宽三条即可开工。
  - **PR 3：** 修完 13.2 的 L159 去重键、§4.2 期间键两条即可开工。
  - **PR 4：** 等 13.1 四条全部落实，并且 owner 裁决了 reviewer memory 中 `P-*` 条件的收窄后再开。
- **需要 owner 拍板**：① 是否授权收窄 reviewer memory 中的 `P-*` 条件，并按 13.1-① 的「事实 vs 估值输入」规则重新分类现有积压；② Mode B 积压由谁执行（owner 手动，还是新开每周重锚任务）。
