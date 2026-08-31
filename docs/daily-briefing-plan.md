# 每日简报（Daily Briefing）— 生成与投递规格

**Status:** Locked for implementation · **Owner:** (unassigned — handoff to implementing agent)
**Author:** planning session, 2026-08-31 · **Revised:** 2026-08-31，与 Codex reviewer 轨对坐定稿（两侧各纠正对方一处事实，见 §0）
**Depends on:** 五个生产者，不是三个——
- GitHub Actions 三条数据 cron：`update-currency-data.yml`（00:00 UTC）、`update-metals-data.yml`（01:00 UTC）、`update-research-prices.yml`（22:00 UTC）
- **Claude 侧 `daily-research-sentinel`**（daily 08:30 CST，生产者）：58/58 全覆盖证明 + 链层雷达 → 分支 `codex/daily-research-YYYY-MM-DD`
- **Codex 侧 `daily-alc-branch-review-gate`**（复核人，daily 09:30 CST，**本规格不改它**，见 §2.1）：选择性重建后 ff-only 推 `main`，review doc 回写生产者分支

`signals.json` / `reports.json` / `verdicts.json` / `earnings-calendar.json` 均为现役数据源。

**Scope of this doc:** 四条 track——**Track 1 金属数据完整性**（修复未复权拆分，补上连续性校验；**这是阻塞项**）、**Track 2 简报生成器**（确定性 Python，双输出 md + json）、**Track 3 发布契约**（仓库只产文件并自述完整度；投递由下游 bot 消费，不在本规格内）、**Track 4 裁决队列私有通道**（reviewer 侧机器块 + 本机 ledger，永不进 `main`）。

本文自包含——实现 agent 不需要读原始对话。

**它要解决的问题：** 仓库每天自动拉取汇率、金属、研究价格三类数据，提交进 git，渲染成看板——**然后等人主动打开网页**。数据在增长，注意力没有出口。`currency/check_alerts.py` 已经写好 σ 偏离检测和消息格式化，末尾停在一行 `# 这里可以集成WhatsApp发送功能` 的占位注释，从未接通。本规格把那条通路补完，并把范围从汇率扩到研究与金属。

**本次修订改了什么（原草案 → 定稿）：**

| 原草案 | 定稿 | 依据 |
|---|---|---|
| 研究段选取键 = `signals.json` 的 `date` 为昨日 | **SHA cursor + 稳定 ID 语义 diff** | 对象级回放：旧规则漏 45% 的 signal，12 天里 4 天研究段整段为空（§4.2） |
| 触发 = 挂在 metals 后的 `workflow_run` | **`workflow_run` ∪ `push` ∪ `schedule` 三触发并集** | GITHUB_TOKEN 推送不触发 `push:` workflow，两类推送走两条互不重叠的通道（§2.2） |
| 排期不涉及 agent 轨 | **两侧 cron 都不改**（先推后复核人、后又推翻，过程见 §2.1） | 复核人的结束前 rescan 已覆盖生产者实测分布的绝大部分；买尾部要天天付一小时（§2.1） |
| 投递时刻由双方对表 | **不对表**：简报是当日摘要，迟到的东西进第二天那份 | cursor 只在成功产出后才前移 ⇒ 不丢；不需要等齐/补发/完整度标记（§5.1） |
| 裁决队列未涉及 | **公开产物只带计数，实质留在需授权才能读的生产者分支上**（Track 4） | `latest.json` 是公开 URL；把未复核提案推上公网＝用投递通道抵消授权模型（§6，owner 已拍板） |

---

## 0. Context & grounded facts（2026-08-31 实测）

### 0.1 数据完整性（Track 1）

| Fact | Value | Consequence |
|---|---|---|
| **PPLT/PALL 历史未复权** | 两只 ETF 在 **2026-05-18** 拆分（Yahoo `events.splits`：PPLT **10:1**、PALL **5:1**，均在 ts `1779111000`）。仓库存的 2026-05-15 收盘为 PPLT `179.03` / PALL `128.77`；Yahoo 现在同日返回 `17.903` / `25.754`——**正好 10× 与 5×** | Track 1 阻塞项。任何跨越该日的波动率/σ 计算被污染：PPLT 的 90 日日波动率被算成 **9.80%**（真实约 2%），于是它**永远不会触发任何阈值**，在简报里静默失灵 |
| **污染范围只有这两只** | 同日对照：GLD `417.29`、SLV `69.04`、COPX `83.05` —— 仓库值与 Yahoo 当前返回值**完全一致**。5 个金属期货无拆分无分红 | 全量重拉是安全的、diff 最小的：只有 PPLT/PALL 在 2026-05-18 之前的行会变 |
| **根因在增量更新，不在拉取** | `update_data.py::fetch_latest` 用 `yf.Ticker(s).history(period="5d")` **只 upsert 最后一天**，从不回溯已处理历史。Yahoo chart API 本身是**回溯复权**的 | 修复方向明确：不是换数据源，是让日更脚本能感知拆分并回改历史 |
| **`validate_data.py` 无连续性检查** | 现有校验覆盖 schema、日期升序、日期去重、数值有限性——**没有任何单日跳变检查**，-90% 静默通过 | Track 1 补一条 fail-closed 的跳变校验。这是本次事故真正的漏网点 |
| **`fetch_historical.py` 读的是 `quote[0].close`** | 非 `adjclose`。实测该字段**已含拆分复权、不含分红复权** | 正合需求：看板要显示真实价格。**不要改用 `adjclose`** |

### 0.2 统计口径

| Fact | Value | Consequence |
|---|---|---|
| **金属必须用收益率 z，不能用价格 z** | 2026-08-28 实测：黄金单日 **-3.38%**，价格 z(1y) = **+0.54σ**（毫无信号），收益率 z(90d 波动) = **-2.22σ**（正确）。钯金 +4.24% → 价格 z +0.20σ vs 收益率 z +1.78σ | 黄金一年里是趋势上涨的，价格 z 只能说"现在价格偏高"，回答不了"今天这根跌是不是异常"。简报问的是后者 |
| **汇率相反，用价格 z** | 换汇决策问的就是"当前价位在历史区间的哪里"。`check_alerts.py` 现有口径：365 天固定窗口 + `statistics.stdev`（**样本**，n-1），1.5σ 黄 / 2.0σ 红 | 汇率段沿用该口径 |
| **前后端 σ 口径不一致** | `check_alerts.py` 用样本标准差 + 固定 365 天；`currency/js/main.js` 用**总体**标准差（除以 n）+ 用户可选窗口。实测 USD/CNY = **-1.43σ(365d)** vs **-1.71σ(90d)** | 简报每行必须带窗口标签。前端默认窗口对齐到 365 天 |
| **各段 as-of 天然不一致** | 实测：汇率数据到 08-29，金属数据只到 08-28（期货结算滞后） | **每段必须独立标注 as-of**，不标即误导 |

### 0.3 🔴 时序与触发（本次修订新增，全部实测）

| Fact | Value | Consequence |
|---|---|---|
| **🔴 GITHUB_TOKEN 推送不触发 `push:` workflow** | `ci-smoke.yml` 挂的就是 `on.push.branches[main]`，最近 **15 次运行全部**是人/reviewer 署名的提交；三条数据 workflow 的 `Update * data` bot 提交**一次都没触发过**。三条 workflow 都是 `checkout@v4` 默认持久化凭据 + 裸 `git push`，无 PAT/App token 覆盖（`update-metals-data.yml:39`）。GitHub 官方规则一致 | **`push: main` 单独用永远收不到汇率/金属/研究价格更新**；`workflow_run` 单独用又收不到 reviewer 推送。二者恰好互补，必须取并集（§2.2） |
| **🔴 `signals.date` 是证据日不是落地日** | 对象级回放最近 12 次 `signals.json` 落地：新增 **22** 条 signal，`date == 落地日前一天` 只接住 **12** 条，**漏 10 条（45%）**；**08-16 / 08-19 / 08-21 / 08-31 四天研究段整段为空（12 天里 4 天 = 33%）**。差值 0–5 天，取决于门户可达性与复核排队 | 原 §3.1 的「`date` 为昨日」规则必须废除（§4.2）。08-31 那条 MiniMax H1（证据日 08-26，HKEXnews 门户盲区晚 5 天）是当天唯一研究结论，旧规则会整条丢掉 |
| **reviewer 实际耗时** | 近 8 次从会话启动到**推完** `origin/main`：13:43 / 25:56 / 16:39 / **38:17** / 26:27 / 29:42 / 14:10 / 19:10。中位 22.6 分钟，均值 23.0，范围 **13.7–38.3**。08-25 实际到 **10:09**，08-28 首推后有修正、最终到 **10:00** | 当天研究段最晚约 **11:18** 才推完 `main`。git commit 时间不能代替远端 push 时间 |
| **生产者实际耗时（按分支提交时间实测 6 次）** | 旧 `coverage-sentinel` 轨（cron 08:36）到最后一个生产提交：08-25 **35:42** / 08-27 **49:10** / 08-28 **49:59** / 08-29 **44:10** / 08-31 **40:15**，范围 **35.7–50.0 分钟**、中位约 44。旧 `research-radar` 轨（cron 07:02）08-31 ＝ **40:13**。合并轨首跑（两轨合一）11:20:01 → 12:19:59 ＝ **59:58** | 合并轨 ≈ 两条 40–50 分钟的轨叠加，稳态预期 **45–70 分钟**。08:30 → 09:30 的 60 分钟窗口**在中位数附近就会越线**；120 分钟窗口才有真实余量 |
| **🔴 生产者会整场错过自己的 cron** | `codex/coverage-sentinel-2026-08-30` 分支的提交时间是 **2026-08-31 01:32:04**——08-30 那天的生产者晚了约 **17 小时**才跑（本机 `execution_environment` 睡眠/离线）。近 7 天里 1 次 | 生产者整场缺席**上周就发生过一次**。它不会造成丢失（cursor 会在次日补上），但会让研究段的 `asOf` 停着不动——那正是该被看见的信号（§5.1） |
| **reviewer 无「等今日生产分支」门禁** | 启动后 fetch 并处理当时可见分支；结束前再 rescan 一次，运行期间出现的分支有机会同轮捕获；若在最终 rescan 之后才出现就**留到次日**；零候选走 no-candidate 路径，**不产结构化 producer-missing 状态** | 研究段不是必然晚一天，而是**机会式竞争**。简报必须能表达 `producer-missing`，不能伪装成「研究段为空」 |
| **metals 完成时间漂移** | 近 10 次：8 次 09:23–09:32，2 次异常 **10:38 / 11:46** | 挂 metals 的 `workflow_run` 常态下早于 reviewer 推 main（漏研究段），尾部情况下 11:46 才落地，晚于当天简报生成 ⇒ 金属段进第二天那份（§5.1） |
| **财报窗口逻辑已存在但窗口过窄** | `earnings_tasks.py` 已实现按每条记录的事件本地时区换算 T-1/T/T+1。当天 `earnings-tasks.json` 的 `tasks` 为空 | **时区换算可复用，窗口要放宽**：未来 5 个交易日。实测下一场是 **2026-09-02 盘后 Broadcom**（`issuer-confirmed`） |

### 0.4 边界与门禁

| Fact | Value | Consequence |
|---|---|---|
| **`signals.json` 已是策展好的双语条目** | 每条含 `date` / `title{zh,en}` / `detail{zh,en}` / `tickers[]` / `crossChecks[]` / `reportIds[]` / `monitoringRefs[]` | 简报直接引用 `title`，**不需要 LLM 改写**。生成器保持确定性 |
| **verdict 变化拿不到快照** | `verdicts.json` 每日覆盖写，只有当前状态 | 用 §4.2 的同一条 cursor 取前值比对，取不到时降级跳过该段，不得报错 |
| **🔴 `latest.json` 是公开 URL** | 部署到 `atypicallife.club/invest/briefing/latest.json` | 把开放集实质内容（如 P-9 的 ALAB 权证冲减收入 2.60% 越线）写进去＝**公开发布未经复核的判断**，正是 fail-closed/提案架构要防的事（§6） |
| **复核人常设指示 7** | 「扫描回执与路由记账不进 `main`」；生产者规范亦写明回执是 human-facing record、不得作为已发布研究数据的派生源 | 把同一套 open/disposition 账本换个 JSON 外壳写进 `main`，只是绕路发布（§6） |
| **生产者分支会被删** | 消费完 review doc 后删分支；记忆里当前就有三条待删 | 分支一删，那天的裁决队列不可回放 ⇒ 需要一个不进 `main` 的**持久**落点（§6.3） |
| **DESIGN.md 第 44 行** | "Do not encode investment judgment with red, green, amber, or stance-colored visuals." | 归档页与 `.md` 正文**严格禁用**红/绿/琥珀判断色与 🔴🟡 交通灯 emoji（§4.5） |
| **CI 门禁形态** | `ci-smoke.yml` 在 push/PR 上跑：research 单测 + 各 validator + `generate_feed.py` + `git diff --exit-code feed.xml` + `hugo --minify` | 新增校验器与"简报产物是否同步"检查按同一模式接入，不要另起 workflow |
| **仓库无任何推送凭据** | 全仓 grep 无 telegram / webhook / smtp / secret 使用 | Track 3/4 维持这个性质：**仓库零 secret**，凭据由消费方自持 |

---

## 1. Principles（locked）

1. **仓库产事实，不产判断，也不负责投递。** 生成器只做阈值筛选和引用；措辞由 `signals.json` 原文承担。**投递是下游消费方的事，本规格到产物为止。**
2. **确定性优先。** v1 不引入 LLM。"言简意赅"由阈值决定，不由文笔决定。
3. **数字必须自带口径。** 每个 z 值带窗口标签，每段带 as-of 日期。没有口径的数字在简报里就是噪音。
4. **"今天没事"和"今天挂了"是两个状态，永远不许混。** 前者是 `empty: true` 的正常产物，后者是文件根本没生成。**在各段内部，承担这件事的是 `asOf`**——一段连续几天空且 `asOf` 不动，就是那条轨可能挂了（§5.1）。不为此另发明状态词汇。
5. **静默失效是最严重的失败模式。** 数据被污染而校验通过、cron 挂掉而无人知晓——都必须由 fail-closed 校验或投递侧存活检测兜住。
6. **沿用既有纪律。** fail-closed 校验器、`test_*.py` 单测、CI 产物同步检查、无判断色——全部继承，不重新发明。
7. **🔴 未经复核的判断不进公开产物。** 简报的投递通道**不得**成为绕过 stance/估值 fail-closed 门禁的旁路。被复核人裁为 `deferred` 的提案，其实质内容只走私有通道（§6）；公开产物里它只能以**计数**形式存在。

---

## 2. 时序拓扑 — 五个生产者，一个简报

本节是本次修订新增的核心。原草案只看见 GitHub Actions 三条数据 cron，漏掉了每天真正决定「研究段有没有内容」的两条 agent 定时任务。

### 2.1 每天实际发生什么（定稿排期，owner 已拍板）

```
时刻(CST)   谁                                  产出                              落点
─────────  ──────────────────────────────────  ────────────────────────────────  ─────────────────
06:15      GH Actions update-research-prices    prices.json                       main（bot 凭据）
           （cron 22:00 UTC 前一日）
08:2x-08:5x GH Actions update-currency-data     currency/data/historical.json     main（bot 凭据）
           （cron 00:00 UTC）
08:30      Claude daily-research-sentinel       58/58 覆盖证明 + 链层雷达          codex/daily-research-YYYY-MM-DD
           【生产者】                             回执 docs/daily-research/*.md     ← 分支，永不进 main
09:2x      GH Actions update-metals-data        metals/data/historical.json       main（bot 凭据）
           （cron 01:00 UTC，实测漂到 11:46）
09:30      Codex daily-alc-branch-review-gate   选择性重建 → ff-only 推 main       main（人署名凭据）
           【复核人】（保持不动，见下）            review doc + 机器块 → 生产者分支    ← 分支
                                                 ledger 追加一行                    ← 本机
~09:50     GH Actions update-briefing           briefing/YYYY-MM-DD.md + latest.json  main
           （三触发并集，见 §2.2）
╌╌╌╌╌╌╌╌╌  ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
           以下归下游消费方，不在本规格内：读 latest.json + 分支机器块 → 发送
```

**定稿：两侧 cron 都不改。** 这一条在本次修订中被推翻过一次，记录推翻的过程，因为理由变了：

- **原判断（已作废）**：复核人 09:30 → 10:30，把生产窗口从 60 分钟拉到 120 分钟。当时的理由是「让下游 11:45 那次拉取一定拿到当天研究段」。
- **理由消失**：投递不归本规格管（§5），且迟到的东西会进第二天那份（§5.1）。于是「保证当天拿到」不再是需要付代价去买的东西。
- **重算**：生产者 08:30 + 实测 45–70 分钟 ⇒ 09:15–09:40 完成。复核人 09:30 启动时 fetch 一次、**结束前再 rescan 一次**（实测结束在 09:44–10:08），所以 09:40 前推上来的分支**当轮就能被捕获**。09:30 已经覆盖了实测分布的绝大部分。
- **10:30 买到的是尾部**（生产者 > ~74 分钟的那些天），**付出的是每天晚一小时**。在「迟到不要紧、第二天会补」的前提下，这笔交易不划算——尾部的代价只是那条研究晚一天，而一小时是天天付。
- 08-30 生产者晚 17 小时那种整场缺席，**10:30 同样接不住**，不构成支持它的理由。

**因此 PR-0 消失，本规格不要求任何 cron 改动。** 若日后观察到生产者经常越过 09:40，再把复核人推到 10:30 即可——那是一行配置，不是架构决定。

### 2.2 触发并集（定稿）

单一触发点做不到，因为两类推送用两套凭据、走两条互不重叠的事件通道：

| 触发 | 接住谁 | 为什么单独不够 |
|---|---|---|
| `workflow_run:` `[Update Currency Data, Update Metals Data, Update Research Prices]`，`types: [completed]` | 三条 bot 数据提交 | 收不到 reviewer 与人工推送 |
| `push:` `main` + 正向 `paths` 白名单 | reviewer 推送、owner 手工修复 | **收不到任何 bot 数据提交**（GITHUB_TOKEN 规则，§0.3） |
| `schedule:` 每日一次（建议 03:07 UTC ＝ 11:07 CST） | 什么都没发生的安静日 | 不知道 reviewer 完没完，GitHub 整点 cron 也会漂 15–60 分钟 |

三者进入**同一个幂等生成器**，`concurrency: {group: briefing, cancel-in-progress: true}`——最后落地的 `main` 状态赢。

**五条实现约束（不写进代码就会踩）：**

1. **`push` 事件不能同时写 `paths` 和 `paths-ignore`**（GitHub 不允许同一事件同时配置两者）。用**正向白名单**：简报目录不在白名单里，自然不会自触发。
2. **白名单要覆盖生成器真正读的全部源文件**，不只研究那四个 JSON——否则人工修汇率/金属数据不会重算：`currency/data/historical.json`、`metals/data/historical.json`、`research/data/signals.json`、`reports.json`、`prices.json`、`verdicts.json`、`earnings-calendar.json`。
3. **不要用 `workflow_run` 事件 payload 里的 `head_sha`。** 它是上游 workflow **启动时**的 SHA，不是它后来 `git push` 造出来的数据 commit。生成器必须自己 fetch 并锁定当时的 `origin/main`，把解析出来的 SHA 写进 `sourceMainSha`。
4. **`workflow_run` 监听 `completed` 而不只监听成功。** 上游失败时对应段标 `failed` / `degraded`，**不能把旧数据包装成当天正常的空简报**（Principle 4）。
5. **`actions/checkout` 要 `fetch-depth: 0`**（或至少能回溯到上一份简报的 `sourceMainSha`），否则 §4.2 的 cursor diff 取不到基线。原草案 §7 关于 `fetch-depth: 1` 的风险由此一次性解决——**显式选择深克隆这条路**。

### 2.3 研究段的时间语义

生产者与复核人构成一条**跨天的流水线**，不是当日闭环：

- 生产者 08:30 扫的窗口是**前一天**的发行人事件；
- 复核人 09:30 审的是**当天**生产者刚推的分支（靠结束前的 rescan 兜住 09:40 前推上来的）；
- 复核人**没有**「等今日生产分支出现」的门禁（§0.3）。

所以「今天的研究段」≠「今天发生的事」，而是 **「今天首次进入 `main` 的已复核结论」**。这正是 §4.2 把选取键换成 SHA cursor 的根本原因——**按落地取，迟到的自然滚进下一份**（§5.1）。

---

## 3. Track 1 — 金属数据完整性（阻塞项，先做）

**在此 track 落地前不得启动 Track 2。** 带着拆分污染发简报，等于每天对两个标的说谎。

### 3.1 修复历史

跑 `fetch_historical.py` 全量重拉（它读 `quote[0].close`，已含拆分复权）。**预期 diff 仅限 PPLT/PALL 在 2026-05-18 之前的行**——若 diff 波及其他标的，停下来查原因，不要直接提交。

验收：`PPLT` 2026-05-15 收盘由 `179.03` 变为 `17.903`；`PALL` 由 `128.77` 变为 `25.754`；GLD/SLV/COPX 及 5 个期货**逐行不变**。

### 3.2 让日更脚本感知拆分

`update_data.py` 增加拆分检测。两种实现皆可，实现者择一并在 PR 描述里说明理由：

- **A（推荐，最小改动）**：日更时对每个标的额外请求 `&events=splits`；若返回的 split 事件日期晚于本地历史中已处理的最后一个 split，则把该日期之前的所有 `close` 除以 `splitRatio`，并在 `metadata` 记录 `lastSplitApplied: {symbol: date}` 作为幂等依据。
- **B**：每周一次全量重拉覆盖（复用 `fetch_historical.py`），日更仍只 append。实现更简单，代价是每周一次大 diff，且拆分最长可潜伏 6 天。

无论选哪个，`metadata` 都要留下可审计的痕迹，**不能静默改写历史**。

### 3.3 补连续性校验（本次事故的真正漏网点）

`validate_data.py` 新增：任一标的单日 |涨跌| > **25%** 即 **fail**，除非该日期在 `metadata.knownSplits[]` 白名单里。白名单条目需含 `symbol` / `date` / `ratio` / 一句人写的理由。

这条校验会在 CI 与日更两处生效。它的意义不是拦住这次——这次已经发生了——而是**保证下一次拆分不会再静默通过**。

配套单测（`test_validate_data.py` 已存在，扩写即可）：
- 造一个 -90% 跳变且不在白名单 → 必须 FAIL
- 同一跳变加进白名单 → 必须 PASS
- 白名单条目缺 `ratio` 或 `date` 非法 → 必须 FAIL

---


## 4. Track 2 — 简报生成器

新目录 `static/invest/briefing/`，与 research 模块同构：`generate_briefing.py`、`validate_briefing.py`、`test_generate_briefing.py`、`test_validate_briefing.py`。

### 4.1 数据源与四段结构

固定顺序，每段无内容则整段省略；四段全空则输出 `empty: true`。

| 段 | 源 | 选取规则 |
|---|---|---|
| 研究 | `signals.json` | **§4.2 的 cursor diff 取新增 signal**；引用 `title` 原文，不改写 |
| | `reports.json` | 同一 cursor diff 取新增/实质变化的 report；输出公司 + `versionLabel` |
| | `verdicts.json` | 同一 cursor 取前值比对 `stance` / `conviction` / `stale` 的变化。取不到前值时**跳过本项**，不报错 |
| 财报前瞻 | `earnings-calendar.json` | 未来 5 个交易日内、`precision: day` 的记录。复用 `earnings_tasks.py` 的事件本地时区换算 |
| 金属 | `metals/data/historical.json` | **收益率 z**：`(今日收益率 − 90 日均值) / 90 日收益率标准差`，\|z\| ≥ **2.0** 才列 |
| 汇率 | `currency/data/historical.json` | **价格 z**：365 天窗口 + 样本标准差，与 `check_alerts.py` 一致。四个货币对**全部列出**（换汇是持续决策，不只在越线时才有意义），越 1.5σ / 2.0σ 的加标记 |

### 4.2 🔴 研究段选取键：SHA cursor + 稳定 ID 语义 diff

**这条替换原草案的「`date` 为昨日」。原规则错在哪：**

`signals.json` 的 `date` 是**证据日**（发行人事件发生那天），不是**落地日**（结论进 `main` 那天）。两者相差 0–5 天，取决于门户可达性与复核排队。对象级回放最近 12 次 `signals.json` 落地：

| | 条数 |
|---|---|
| 实际新增 signal | **22** |
| `date == 落地日前一天` 命中 | 12 |
| **漏掉** | **10（45%）** |
| 研究段整段为空的天数 | **4 / 12（33%）**：08-16、08-19、08-21、08-31 |

08-31 那条（MiniMax H1 2026，证据日 08-26，因 HKEXnews 门户盲区晚了 5 天才落地）是当天**唯一**的研究结论，按旧规则会被整条丢掉。

**新规则：**

1. 本次开始时 fetch 并锁定 `origin/main` 为 `currentMainSha`；cursor 基线 `baseSha` 从既有 `latest.json` 取：
   ```
   baseSha = (latest.json.date == 今天) ? latest.json.previousSourceMainSha   # 同日重跑：沿用当日首跑的基线
                                        : latest.json.sourceMainSha          # 当日首跑：从上一份简报的 source 起算
   ```
   本次写出时 `previousSourceMainSha = baseSha`、`sourceMainSha = currentMainSha`。
   **`previousSourceMainSha` 因此始终指向前一日最近一份成功简报的 source**——这是同日重跑幂等的全部机制所在。
2. 断言 `baseSha` 是 `currentMainSha` 的祖先（`git merge-base --is-ancestor`）；不是则 **fail closed**（历史被改写或克隆太浅），不得静默降级。
3. 对 `baseSha` 与 `currentMainSha` 两份 JSON 快照按稳定键做**对象级**比较，取新增与实质变化：
   - signal → `id`
   - report → `id`
   - verdict → `reportId`
   - monitoring → `reportId` + `monitoring.id`
4. `date` / `readingAsOf` / `lastUpdate` **只用于显示 as-of**，不参与「算不算今天的」判断。

> **一句话口径：** 「新鲜」由**自上一份成功简报以来首次进入 `main` 的稳定对象版本**决定；证据日期回答 as-of，不回答何时进简报。

**为什么不是 `git diff --name-only`：** `signals.json` 每次落地整个文件都变，路径级 diff 只能回答「这个文件动了」，回答不了「哪几条是新的」。对象级 diff 才是需要的粒度。

**🔴 同日重跑必须幂等。** 当天会被触发多次（数据 workflow、reviewer 推 main、schedule 兜底），**基线在整个当天必须保持不变**——这正是上面那条三元式存在的理由。若第二次触发直接拿 `latest.json.sourceMainSha`（＝第一次跑写下的 `currentMainSha`）当基线，就只会 diff 第一次→第二次这一小段，**把第一次已收录的条目（例如 06:15 落地的 `prices.json`）全部丢掉**。基线也不是 `HEAD~1`。**当天文件是累积的，不是增量的。**

### 4.3 双输出

- **`briefing/YYYY-MM-DD.md`** —— 人读 + 站点归档页
- **`briefing/latest.json`** —— 机器读，下游消费这个。**不要让消费方去解析 Markdown。**

```json
{
  "date": "2026-08-31",
  "generatedAt": "2026-08-31T02:47:12Z",
  "sourceMainSha": "ad554557a1c0...",
  "previousSourceMainSha": "e75cca3b09f2...",
  "empty": false,
  "asOf": {
    "currency": "2026-08-29",
    "metals":   "2026-08-28",
    "prices":   "2026-08-28",
    "research": "2026-08-31"
  },
  "openItemCount": 12,
  "sections": {
    "research":  [{ "ticker": "MRVL", "text": "...", "url": "...", "evidenceDate": "2026-08-26" }],
    "earnings":  [{ "date": "2026-09-02", "company": "Broadcom",
                    "session": "after-close", "status": "issuer-confirmed" }],
    "metals":    [{ "name": "黄金", "price": 4478.10, "changePct": -3.38,
                    "z": -2.22, "window": 90, "level": "alert",
                    "asOf": "2026-08-28" }],
    "currency":  [{ "pair": "USD/CNY", "rate": 6.7285, "z": -1.43,
                    "window": 365, "level": "none", "asOf": "2026-08-29" }]
  }
}
```

**必填字段与取值域：**

- `sourceMainSha` / `previousSourceMainSha` —— §4.2 的 cursor 两端。**必填**；缺失即视为产物非法。
- `asOf.*` —— 每段独立的 as-of，**必填**（Principle 3）。`asOf.research` ＝ 最近一次有研究内容落到 `main` 的日期；它停着不动就是研究轨可能挂了的信号（§5.1）
- 上游 workflow `completed` 但非 success 时，对应段的 `asOf` 自然停在旧值——**不需要额外的状态字段**，也**不许**把旧数据当成当天新数据
- `openItemCount` —— **只有计数，没有实质内容**（§6 的公开边界）；取不到裁决队列时省略该字段，不写 0
- `level` ∈ `none` | `warning` | `alert` —— **是统计阈值档位，不是投资判断**
- `window` 与 `asOf` 必填，兑现 Principle 3

### 4.4 语言与周末（原 §8 开放问题，现已定）

- **语言：中文。** `signals.json` 双语齐备，但 `latest.json` 双语会让下游消息长一倍、且读者是单一 owner。**归档页保持中英双语**（走既有 `PAGE_LABELS`/`localize()` 模式，双语成本在归档页是零）。
- **周末：照常生成 `empty: true` 的文件。** 不生成就无法区分「没事」和「挂了」，Principle 4/5 直接崩塌。空文件的仓库噪音是可接受代价——它正是存活证据本身。
- **归档页 `briefing/index.html`：做，但排在 PR-3。** `briefing/*.md` 提交进仓库本身已有存档价值，归档页不是 v1 阻塞项。

### 4.5 排版约束

- 每个 z 值渲染时带窗口：`z -1.4σ(1y)`
- 每段头部带 as-of：`【金属】as of 08-28`
- **不用红/绿/琥珀色，也不用 🔴🟡 交通灯 emoji**（DESIGN.md 第 44 行）。用中性标记：`[2σ]` / `[1.5σ]` 前缀，或直接让带符号的数字自己说话
- 归档页复用 `/shared/theme-switcher.js`，绝对路径引用资源

### 4.6 接入 workflow

新建 `.github/workflows/update-briefing.yml`，按 §2.2 的三触发并集。流程：fetch 并锁定 `origin/main` → 生成 → 校验 → 仅在有变更时提交 `static/invest/briefing/`。

`ci-smoke.yml` 追加两步：`validate_briefing.py`，以及仿照 `feed.xml` 的产物同步检查。

---

## 5. Track 3 — 发布契约（对下游消费者）

**本规格到产物为止。** 投递侧（VPS 上已有的 bot）只消费我们产出的东西并负责发送——它的拉取时刻、重试、去重、消息排版都不在本规格范围内，本节只定义**我们保证提供什么**。

```
GitHub Actions / Codex reviewer          Cloudflare Pages
──────────────────────────────           ────────────────
数据 workflow / reviewer 推 main
      ↓ workflow_run ∪ push ∪ schedule
generate_briefing.py
      ↓ 提交
static/invest/briefing/
  ├─ 2026-08-31.md          （人读 + 归档）
  └─ latest.json            （机器读）
      ↓ 自动部署
              atypicallife.club/invest/briefing/latest.json    ← 公开事实段

codex/daily-research-YYYY-MM-DD
  └─ review doc 内 daily-review-state:v1                        ← 私有裁决段（需 token）
                                                            ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
                                                            以下归消费方，不在本规格内
```

**我们保证的两件事：**

1. **每天都有产物。** 无论多空、无论上游是否失败，`latest.json` 与 `YYYY-MM-DD.md` 都会生成。「今天没事」是 `empty: true`，「今天挂了」是文件根本没更新——消费方按 `date` 区分（Principle 4）。
2. **字段一旦发布即为对外接口。** 变更要向后兼容或提前通知。

**仓库零 secret**：公开事实段走站点 URL（拉到就说明部署也成功了，多一层验证）；私有裁决段留在生产者分支上，读它需要消费方自己的凭据——**本仓库不持有任何凭据**。

### 5.1 迟到的东西不会丢，它进第二天的简报

简报是**当日摘要**，不是账本。因此这里**不做**「等齐了再发」「补发」「完整度标记」那一类机制——它们服务的是审计，不是「知道当天信息」。

不丢的保证来自 §4.2 的 cursor，而不是来自等待：

- `previousSourceMainSha` 只在**成功产出一份简报之后**才前移。
- 所以任何在今天生成之后才落到 `main` 的东西（metals 漂到 11:46、reviewer 晚推、生产者整场缺席后次日补跑），都仍然落在**明天那份简报的 cursor 窗口内**。
- 它不会消失，只会晚一天出现。

**唯一需要的诚实机制是每段的 `asOf`**（Principle 3 本来就要求）——它是统一的，不需要为研究段另发明一套状态词汇：

| 段 | `asOf` 的含义 |
|---|---|
| 汇率 / 金属 / 价格 | 该数据源最新一根 bar 的日期 |
| 研究 | **最近一次有研究内容落到 `main` 的日期** |

研究段连续几天空、`asOf` 停在 08-26 不动——这本身就是「轨道可能挂了」的信号，和金属数据停更是同一种读法、同一种排版。**不需要为此再发明第二套状态词汇。**

---

## 6. Track 4 — 裁决队列：公开产物与私有通道的边界

简报里对 owner 最有决策价值的一段，是「今天有什么等我裁决」：当前开放集 12 项（含 P-9 这类被 stance 联动硬门禁挡下、fail-closed 成提案的条目）。它今天只活在 review doc（生产者分支上）与 Claude 侧记忆里。

### 6.1 为什么它不能进 `latest.json`

两条独立且各自充分的理由：

1. **`latest.json` 部署到公开 URL。** 把 P-9 的实质内容（ALAB Q2 权证冲减收入 $10.216M ÷ 收入 $392.4M ＝ 2.60%，越过「约 2%」触发器）写进去，等于**公开发布一条未经复核的判断**。复核人已把 P-9 裁为 `deferred`，理由正是「诚实评级与完整 stance 重裁被硬绑定」——绕开这个门禁把数字推到公网，是**用投递通道抵消掉授权模型**（Principle 7）。
2. **常设指示 7：「扫描回执与路由记账不进 `main`」。** 严格解释下，它不仅禁止原文件，也禁止把同一套 open/disposition 账本换个 JSON 外壳写进 `main`——那只是绕路发布。生产者规范本身也写明回执是 human-facing record，不得作为已发布研究数据的派生源。

### 6.2 定稿通路（复核人已同意提供机器块）

```
Codex reviewer（09:30）
   ├─ review doc → codex/daily-research-YYYY-MM-DD      ← 分支，不进 main
   │     内含固定标记的 fenced JSON: daily-review-state:v1
   ├─ 推送后验证远端 branch tip == review commit
   └─ 验证通过后才 append 一行到本机 append-only ledger
         ~/.codex/automations/daily-alc-branch-review-gate/review-ledger.jsonl

╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
消费方（持自己的 token，不在本规格内）
   ├─ 公开：站点 latest.json          ← 事实段 + openItemCount
   └─ 私有：读生产者分支上的机器块      ← 裁决段实质
```

- `latest.json`（公开）只带**计数**：`openItemCount`，不带任何开放项实质内容。
- 裁决段实质**只存在于生产者分支上**，需要凭据才能读到，**不落公网**。
- **仓库仍然零 secret**：我们负责把它放在一个需要授权才能读的位置，谁去读、怎么发，不归本规格管。

`daily-review-state:v1` 最小字段（fenced JSON，不用 YAML front-matter）：

```json
{
  "schemaVersion": 1,
  "date": "2026-08-31",
  "reviewedProducerCommit": "<40-char-sha>",
  "reviewStatus": "complete",
  "stateHash": "<规范化后的哈希>",
  "requiresDecisionNow": [],
  "deferredOpenItems": [],
  "closedThisRun": [],
  "openItemCount": 12
}
```

每项至少含稳定 `id`、`reportIds`、`openedOn`、`disposition`、中文标题、`decisionNeeded`、`nextAction`、`maturityCondition`。

**🔴 块缺失、SHA 不匹配或 schema 非法时必须输出 `reviewStatus: invalid` / `unavailable`，绝不能当成零待办。**

### 6.3 分支会被删，所以还需要持久落点

生产者消费完 review doc 后会删分支（记忆里当前就有三条待删）。分支一删，那天的裁决队列不可回放。因此**两个落点职责分开**：

| 落点 | 职责 | 生命周期 |
|---|---|---|
| 分支 review doc 内的 `daily-review-state:v1` | 当天跨系统**传输接口**，供下游读取 | 随分支被删 |
| 本机 `review-ledger.jsonl`（append-only） | 分支删除后的**永久审计与历史回放** | 永久 |
| `memory.md` | 人读的运行摘要与当前 checkpoint | 不作为稳定机器接口 |

**写入顺序必须保证不留假记录：**

1. 生成 fenced JSON 与规范化 `stateHash`
2. 随 review doc commit 推到生产者分支
3. 验证远端 branch tip == review commit
4. **验证通过后**才向 ledger 追加一行
5. ledger 追加失败 ⇒ 本轮标为未完整完成；下轮从仍可达的 review commit 幂等补录

唯一键 `(reviewedProducerCommit, reviewCommit)`；修订**追加**新行并带 `supersedesReviewCommit`，**不覆盖旧行**。

**不用 GitHub artifact**（有 retention），**不新建常驻 ledger 分支**（会撑大现有 namespace 与清理契约）。当前边界下本机 append-only ledger 最干净。

### 6.4 排版：不要把 12 项都做成「今天要裁决」

渲染归消费方，但**分组是数据结构，归我们**——机器块必须把三类分开，否则下游只能自己猜：

| 字段 | 含义 | 典型条数 |
|---|---|---|
| `requiresDecisionNow[]` | 今天真正需裁决、或刚重新成熟的 | 0–1 |
| `deferredOpenItems[]` | 仍被硬门禁挡住、**不需要今天动作**的 | 当前 12 项的绝大多数 |
| `closedThisRun[]` | 本轮已关闭 / 已采取的 | 0–数条 |

P-9 当前是 `deferred`，等的是完整 ALAB 估值 + stance 包。**把 12 项一律塞进 `requiresDecisionNow` 会让整段迅速失去信号**——分组本身就是这段内容的主要价值。

---

## 7. Delivery slicing & gates

| PR | 内容 | Gate |
|---|---|---|
| PR-1 | Track 1 全部：`fetch_historical.py` 重拉修复历史 + `update_data.py` 拆分感知 + `validate_data.py` 跳变校验 + 单测 | diff 仅限 PPLT/PALL 2026-05-18 之前的行；PPLT 2026-05-15 = `17.903`、PALL = `25.754`；三条新单测绿；`/invest/metals/` 看板两只 ETF 曲线不再断崖 |
| PR-2 | `generate_briefing.py` + `validate_briefing.py` + 单测。**先不接 workflow**，用 `--date` + `--since-sha` 回放历史日期人工核对 | 2026-08-28 回放：金属段只出黄金 1 条（钯金 +1.78σ、铜 -1.58σ 未达 2.0σ）；**2026-08-31 回放：研究段必须出 MiniMax H1（证据日 08-26）——这条是新旧选取键的分水岭，旧规则会丢掉它**；周末回放：`empty: true`；同日两次触发回放：第二次不得丢掉第一次的条目 |
| PR-3 | `update-briefing.yml`（三触发并集）+ `ci-smoke.yml` 两步 + 归档页 `briefing/index.html` | 手动 `workflow_dispatch` 跑通并提交；**造一次 bot 数据提交与一次人署名提交，两条路径都要能触发**；产物同步检查生效；归档页 zh/en 双语无判断色 |
| PR-4 | 前端 σ 口径对齐：`currency/js/main.js` 默认窗口改 365 天，与 `check_alerts.py` 同口径 | 看板 USD/CNY 显示 `-1.43σ`，与简报一致 |
| REV | **复核人侧（Codex 轨，仓库外）**：review doc 输出 `daily-review-state:v1` fenced JSON + `review-ledger.jsonl` append 顺序。改的是 automation 的 `prompt`——**走 Codex Automations 界面或 `automation_update`，不要手改 `automation.toml`**（手改因约 30 秒轮询大概率生效，但会留下陈旧 `updated_at`、不重算 `next_run_at`） | 块可被 `json.loads` 解出；ledger 行在远端 tip 校验通过后才出现；连续两轮 `stateHash` 可复算 |
| — | **投递侧（下游消费方）** | 不在本规格范围。我们对它的全部承诺就是 §5 的两条：每天有产物、字段是稳定接口 |

PR-1 → PR-2 → PR-3 严格顺序。**PR-1 未合并前不开始 PR-2。** REV 可并行。**本规格不要求任何 cron 改动**（§2.1）。

---

## 8. Acceptance criteria

**Track 1**
- [ ] `historical.json` 中不存在任何单日 |涨跌| > 25% 且不在 `knownSplits[]` 白名单里的记录；造一个假跳变能让 `validate_data.py` FAIL
- [ ] PPLT 90 日日波动率回到 2% 量级（当前 9.80%），两只 ETF 能正常参与阈值筛选

**Track 2**
- [ ] 金属段用收益率 z，汇率段用价格 z；每个 z 值渲染时带窗口标签，每段带独立 as-of
- [ ] **研究段按 `sourceMainSha` cursor + 稳定 ID 选取，不使用 `date == 昨日`**；2026-08-31 回放能出 MiniMax H1
- [ ] **同日多次触发幂等**：当天文件累积，不因重跑丢条目。**具体检验：同一天连跑两次，第二次的 `previousSourceMainSha` 必须与第一次相同**（不得前移到第一次的 `sourceMainSha`）
- [ ] `sourceMainSha` 非 `currentMainSha` 祖先时 **fail closed**，不静默降级
- [ ] `latest.json` 通过 `validate_briefing.py`；`empty: true` 与"文件缺失"在消费侧可区分
- [ ] **迟到不丢**：回放「metals 在当天简报生成之后才落地」，该条目必须出现在**次日**那份里，且不重复出现
- [ ] 每段带独立 `asOf`；`asOf.research` ＝ 最近一次研究内容落到 `main` 的日期
- [ ] verdict 段在拿不到前值时降级跳过，不抛异常

**触发链**
- [ ] `update-briefing.yml` 由 `workflow_run` ∪ `push` ∪ `schedule` 三者触发；**bot 数据提交与人署名提交两条路径都实测能触发**
- [ ] `push` 只用正向 `paths` 白名单（无 `paths-ignore`），且白名单覆盖全部源文件
- [ ] `sourceMainSha` 来自生成器自己 fetch 的 `origin/main`，**不是** `workflow_run` payload 的 `head_sha`
- [ ] `checkout` 用 `fetch-depth: 0`
- [ ] `ci-smoke.yml` 覆盖简报校验与产物同步检查

**边界**
- [ ] 简报正文与归档页无红/绿/琥珀判断色、无交通灯 emoji
- [ ] 仓库中不存在任何推送凭据或 secret 引用
- [ ] **公开 `latest.json` 中不含任何开放项/提案的实质内容，只有 `openItemCount`**
- [ ] 回执、review doc、`daily-review-state:v1`、ledger **全部不在 `main`**

---

## 9. Risks & gotchas

- **拆分白名单会被当成消音开关。** 它的用途是记录**已核实**的公司行为，不是"这条校验太吵所以关掉"。每个条目必须有 `ratio` 和一句人写的理由；review 时把无理由条目视同校验失败。
- **`empty: true` 会诱使人省略文件。** 一旦某天"没内容就不提交"，投递侧的存活检测立刻失效，Principle 4 崩塌。**无论多空都要产出文件。**
- **回放测试要固定时间源与 cursor。** 生成器接受 `--date YYYY-MM-DD` 与 `--since-sha`，仿照 `earnings_tasks.py` 的 `reference: {mode, value}` 模式，否则单测不可重放。
- **阈值会随波动率环境漂移。** 2.0σ 在低波动期会话痨、高波动期会失声。跑一两周后按实际条数复核一次，不要一次定死。
- **不要顺手给简报加 LLM 润色。** 若将来确实要加，它只能在 `latest.json` **之后**作为独立的可选层，绝不能进生成路径——数字的权威性来自确定性。
- **🔴 两侧 agent 轨都跑在本机，睡眠即缺席——且已经发生过。** `codex/coverage-sentinel-2026-08-30` 的提交时间是 08-31 01:32，那天生产者晚了约 17 小时。复核人同理：笔记本睡眠 = 当天没有 reviewer 推送。**改 cron 接不住这类缺席**（§2.1）。但它**不造成丢失**——cursor 会在次日补上。要看见它，靠的是研究段 `asOf` 停着不动（§5.1）。
- **🔴 生产者分支删除会带走当天的裁决队列。** 这是 §6.3 本机 ledger 存在的唯一理由。ledger 追加必须在远端 tip 校验之后——顺序反了就会留下"记了但没推上去"的假记录。
- **🔴 `workflow_run` 的 `head_sha` 陷阱。** 它指向上游 workflow 启动时的 SHA，不是数据 commit。直接用它会让 `sourceMainSha` 系统性落后一个提交，cursor diff 于是重复收录或漏收。
- **🔴 三触发并集会同时到达。** 数据 workflow、reviewer push、schedule 兜底可能在几分钟内连续触发。必须 `concurrency` 串行化 + `cancel-in-progress`，且生成器幂等——否则会产生互相覆盖的半份简报。

---

## 10. 已关闭的开放问题

原 §8 的三个开放问题，本次全部定案（依据见对应小节）：

| 原问题 | 定案 | 依据 |
|---|---|---|
| 周末是否生成 | **照常生成 `empty: true`** | §4.4，Principle 4/5——不生成就无法区分「没事」与「挂了」 |
| 中文还是双语 | **`latest.json` 中文，归档页双语** | §4.4——双语让下游消息长一倍，归档页双语零成本 |
| 归档页是否值得做 | **做，排在 PR-3，非 v1 阻塞项** | §4.4 |

本次新增并已定案：

| 问题 | 定案 | 依据 |
|---|---|---|
| 研究段选取键 | SHA cursor + 稳定 ID 语义 diff | §4.2，22/12/10 实测回放 |
| 生成器触发点 | `workflow_run` ∪ `push` ∪ `schedule` | §2.2，GITHUB_TOKEN 规则实证 |
| 两侧 cron 排期 | **都不改**（10:30 方案在投递出范围后被推翻） | §2.1 |
| 上游迟到怎么办 | **什么都不做**：迟到的进第二天那份 | §5.1——cursor 保证不丢；简报是当日摘要不是账本 |
| 裁决队列通道 | 公开只带计数，实质留在需授权的生产者分支上 | §6，owner 拍板 |
