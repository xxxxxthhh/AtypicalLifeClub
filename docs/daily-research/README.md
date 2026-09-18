# Daily Research Sentinel — 回执索引

合并轨（2026-08-31 起）每日运行的回执。**回执按设计不进 `main`** —— 复核人吸收数据后**保留分支并写下 review doc**，再由**次日运行（下游 producer）**读讫、折入 memory、然后删除分支；回执随分支一并消失。因此本索引只覆盖当前存活分支上的运行。

> **所有权（复核人 2026-09-07 要求写明，2026-09-08／09-09 两轮再次点名）：** review doc 的**消费**与日期分支的**删除**由**下游 producer**（本任务自身，即次日运行）负责，**不是复核人的行动项**。
> 复核人写完 `YYYY-MM-DD-review.md` 后**保留分支**并标记 `AWAITING_DOWNSTREAM_HOUSEKEEPING`；次日运行读讫、把仍生效的裁决折进 memory，再按双测试删除分支。
> **⚠️ 删除前必须先把本 README 从待删分支取回**（它不在 `main` 里），否则索引会随分支永久丢失。

| 日期 | 分支 | 类型 | 计数 (NO_CHANGE / UPDATED / SOURCE_FAILURE) | 提案 | 回执 |
|---|---|---|---|---|---|
| 2026-09-18 | `codex/daily-research-2026-09-18` | **data run**（0 报告编辑、**2 条新 signal**、0 新规则、0 新提案） | 59 / 0 / 0 = 59 | 0 新增；未决 2（P-14 Oracle ＋ P-15 Almonty，均 `deferred`） | [2026-09-18.md](2026-09-18.md) |

## 历史（分支已按"已消费"判定删除，回执随分支一并移除）

| 日期 | 结局 |
|---|---|
| 2026-09-17 | receipt only，59/0/0，0 项新提案。复核 **`NO_RESEARCH_CHANGE`**（review commit `77d2ce6`，producer tip `5b9edf3`，`Merged to main as: not merged`）：**A-1 收盘取数 `taken (modified)` —— 「改用 `/chart` 作默认收盘句柄」被否决**，改为「优先带 ISO 日期参数的 `/historical` 指定日期行；缺行才用 `/chart` 并核 `timeAsOf`/会话/前收/恒等式且标临时，历史补齐后回核」，**并停用 `ser[4]` 等固定下标**（历史首行会前移）；「21 腿句柄分差成因」`deferred`（未重放 producer 时刻原始样本，**不可倒推「早前异常已解决」**）；**回执结构 `dropped` —— TL;DR 必须置于任何正文说明之前**（连续两轮点名）；**「全宇宙无新事件」断言 `dropped`**（须收紧为「已读材料未发现匹配」）；**金盘分派程序与 Sandisk 薪酬 8-K 均 `dropped`**（程序性/治理类不升级、不推进 P-6、不新增 signal）；SMH SAI `deferred`（复核人侧 403，未认证文件范围）；Innolight FF305 含/不含库存股两口径 `taken`；发行人 59/59 与管线时刻 `taken (modified)`（盲区须与计数同口气、每轮重读时刻）；**SKILL.md 把 `codex/coverage-sentinel-2026-08-30` 写成常设保留案例已作废**。开放集 29 项、21 条到期监测、7 项候选逐条 `deferred`。分支已于 2026-09-18 按测试 A 删除 |
| 2026-09-16 | data run，58/1/0，0 项新提案。复核 **`ACCEPT_WITH_CHANGES`**（review commit `ccf9c63`，producer tip `76788dc`，**Merged to main as `b7cc69a`**）：MiniMax EGM 批准事实由复核人独立重建为**正文更正**发布；**本轨的 `funding-dilution` monitoring 改动被撤下（无合法 crossCheck 不能豁免 signal 门禁）**；「第 4 决议＝追加回购额度」永久 `rejected`（实为把已购回股份并入发行授权）；「批准 ⇒ 未执行」绝对断言 `dropped`；Innolight 只能说含库存股总数不变、不能泛称分母完好；价格旗标列表点数错（5D 实 13、vsPA 实 9）；管线时差按 naive UTC 应为约 24h；producer 用 Python 3.14 不能替代 3.11 门禁；开放集 29 项逐条 `deferred`。分支已于 2026-09-17 删除 |
| 2026-09-15 | receipt only，59/0/0，1 项新提案（P-15 Almonty×卢旺达合资）。复核 **NO_RESEARCH_CHANGE**（review commit `f7b1d18`，producer tip `04f3898`）：**「`chain-wide-repricing` 的 if 两腿都成立 ⇒ 共同原因成立」这个推断形式永久 `rejected`**（未发现基本面证伪 ≠ 证明不存在；同跌只支持共变观察）；**「重锚价一律用 2026-09-11 收盘 $150.28」永久 `rejected`**（历史收盘更正不得转为永久固定重锚日）；**「feed 无 diff ⇒ 报告未改」再次 `rejected`**（须用基线至精确 tip 的完整路径 diff）；链报分母纠正为 **48 篇**（59 含 11 非链）；52 周极值断言与「路由覆盖 ⇒ 无事件」均 `dropped`；Nasdaq 字段规则 `deferred` 且「不能仅凭差额小就断言取整」。分支已于 2026-09-16 按测试 A 删除 |
| 2026-09-14 | receipt only，59/0/0，1 项提案（P-14）。复核 **NO_RESEARCH_CHANGE**（review commit `24f5829`，producer tip `35012f2`；09-15 与本份一并补交，故 09-15 回执 A-1 记的「无 review doc」已作废）：A-2/I-1 只关闭标注腿；A-3 Kioxia 路由只作 producer 发现、不据此认证所有 IR 无新增；A-4 Almonty 必需路由 `deferred`（一次 6-K 成功不证明本土路由缺失无代价）；**quiet-day 两提交形状再次 `dropped`** —— 提交前核对行数与日期，最终应只有一笔完整 receipt；来源清单只作 producer 运行日志。分支已于 2026-09-16 按测试 A 删除 |
| 2026-09-13 | receipt only，59/0/0，2 项提案。复核 **`ACCEPT_WITH_CHANGES`（本轨历来第一份 ACCEPT，115 项处置）**：**I-1 判 `taken (modified)` 并关闭** —— CAS 准则标注由复核人独立重建后发布 main `ecda98b7`，同时纠正本轨把港股口径误写为 HKFRS（**实为 IAS 34/IFRS**），「两套毛利率对照」一腿 `dropped`；**「feed 幂等能证明 reports.json 未改」永久 `rejected`**（生成器非单射 ⇒ 改用 `git diff`/文件 hash）；**A-1 收盘价纠错 `taken (modified)`** —— `/historical` 需 ISO 日期参数（MM/DD 返 HTTP 200 ＋ 业务 400），ORCL $150.28／OKLO $36.22 经指定日期行实核；quiet-day 两提交形状 `dropped`（自查须在首个提交前完成）；多条计数口径 `taken (modified)`：59＝美 54（含 3 ETF）＋非美 5、台账 58＝美 53＋非美 5、Kioxia 须用未舍入值判定、MiniMax −7.53% ⇒ Oklo 非唯一 1D 越线、「无新时段」不保证取数逐字节恒等。分支已于 2026-09-14 按测试 A＋B 删除 |
| 2026-09-12 | data run，59/0/0，1 项提案（P-14）。复核 **REJECT**：唯一生产 signal（Oracle 10-Q RPO 转化阶梯 `a4fe5dd`）因复核人侧 10-Q 403、融资计划 429 **未能独立读取而不吸收**，对应候选判 `deferred`（**不是永久否决**）；A-3 Corning 作第二实例判 `dropped`；「退役规则复活/无据改挂 successor」再次永久 `rejected`。分支已于 2026-09-13 按测试 A 删除，**删除前该 signal 全文已存档进 memory**（它未进 main） |
| 2026-09-10 | data run，59/0/0，0 项提案。复核 **REJECT**（65 项裁决，review commit `15cad23`，此前因远端交接未完成而一度被记为「无 review doc」）：ASE signal 判 `dropped` —— 挂在 2026-08-07 已退役的 `advanced-packaging-chokepoint` 上，合计 ATM 营收不构成产能/独立定价/具名项目，**不得复活退役规则、不得只改挂 successor**；「未提交 8-K ⇒ 不重大」永久 `rejected`；六层价格共振 `dropped`；currency **>36h 只是分诊阈值不是故障证据**；退役规则校验器缺口 `deferred`（＝Q-1 仅剩的腿）。分支已于 2026-09-13 按测试 A 删除 |
| 2026-09-11 | data run，57/2/0，1 项提案（P-14）。复核 `ACCEPT_WITH_CHANGES`：**TSMC 单元判 `taken (modified)` —— `advanced-node-utilization` 由 `within` 改为 `unclear`**（正增长不能证明两腿未触发），落 main `a1bfbd6`；**Oracle signal `taken (modified)`**（收窄为已核验交付/现金流，FCF 精确至 −$5.396B），落 main `c0b2e31`；**Broadcom 整单元判 `deferred`**（当季 10-Q 复核人侧不可读，**未进 main** ⇒ 下游新开 B-1，全文已存档 memory）；**「以旧 signal 先例复活退役规则／把不合条件的月营收改挂 successor」永久 `rejected`**（Q-1 处置腿结案，只剩校验器腿）；另有多条口径 `taken (modified)`：双把手同属 Nasdaq 不是两个独立来源、校验须用 Python 3.11、退出价格 flag ≠ 估值工作已完成。分支已于 2026-09-12 按测试 A＋B 删除 |
| 2026-09-09 | receipt only，58/0/0，3 项提案。复核 `ACCEPT_WITH_CHANGES`：**A-2 NeoVolta 财报日判 `taken (modified)`，复核人在 main `4bdb001` 写入 `earnings-calendar.json`（2026-09-23／盘后／issuer-confirmed／发行人文章 URL）并重生成队列**；**P-12 的「未提交 8-K ⇒ 不重大」被永久 `rejected`**；P-11 判 `deferred` 且明示不接受「采纳或永久否决」二选一，其「放宽 `neocloud-financing`」判 `dropped`；另有 7 条口径 `taken (modified)`（亚洲腿本窗五间隔完整、来源失败分两级、时间戳时区、feed 恒等不能证明 reports.json、共振≠因果、`chain-wide-repricing` 要求「多个」非「全部」层、Almonty 需补 SEDAR+）。分支已于 2026-09-10 按测试 A＋B 删除 |
| 2026-09-08 | receipt only，58/0/0，0 项提案。复核 `NO_RESEARCH_CHANGE`：A-1 金盘保荐督导报告判 `taken (modified)` —— **两项「新事实」其实已在双语正文的 08-21 段落里，压缩元数据不必重复正文每一个事实**；SK 海力士/铠侠「共同因子」判 `dropped`（共振不等于因果）；**feed 零 diff 推断判 `dropped`**；开放集行数争议由复核人自行更正（20 行，非 21 行）。分支已于 2026-09-10 按测试 A 删除 |
| 2026-09-07 | receipt only，58/0/0。复核 `ACCEPT_WITH_CHANGES`：**确立「`earnings-calendar.json` 是 producer 可直接写的事实文件」**；另有 6 项计数/口径 `taken (modified)`。分支已于 2026-09-08 删除 |
| 2026-09-06 | receipt only，58/0/0。复核 `NO_RESEARCH_CHANGE`；Corning 会议日程 8-K 判 `dropped`，立下「日程类只作发现」先例。分支已于 2026-09-07 删除 |
| 2026-09-05 | receipt only，58/0/0。复核 `NO_RESEARCH_CHANGE`：P-10 判 `deferred`；两处事实修正（`$3.30` 行权价确已披露；增额权证 `727,273`/`727,272` 8-K 内部冲突）。分支已于 2026-09-06 删除 |
| 2026-09-04 | data run，57/1/0。复核 `ACCEPT_WITH_CHANGES`：Broadcom Q3 重锚方向获认可但**授权路径被否决**，复核人在最新 main 独立重建后以 `72e557f` 发布。分支已于 2026-09-05 删除 |
| 2026-09-03 | data run，57/1/0。复核 `ACCEPT_WITH_CHANGES`，仅 Broadcom Q3 chain signal 并入 main（`baf958f`）；报告整包 deferred。分支已于 2026-09-04 删除 |
| 2026-09-02 及更早 | 已由各自下游运行删除 |
