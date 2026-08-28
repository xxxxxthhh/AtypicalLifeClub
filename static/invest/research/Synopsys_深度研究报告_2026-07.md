# Synopsys 深度研究报告 - AI 芯片设计的 EDA/IP 与仿真约束

标的收录日期：2026-07-05
最近更新日期：2026-08-28
代码：NASDAQ: SNPS
免责声明：本报告仅用于信息与研究交流，不构成任何投资建议，请自行完成尽职调查。

---

## 执行摘要

> **框架角色：** Synopsys 是 AI 基建 EDA/IP 层的公共约束。本报告的任务是验证链条信号，而不是把单一公司数据直接变成投资建议。

**一句话论点：** AI 基础设施 eda-ip 层的公共约束：SNPS 验证 AI silicon 需求是否穿透到 design automation、verification、simulation、IP blocks 和 system-level complexity。FY2026 Q3 revenue $2.4768B，Design Automation 同比 +53%，Design IP 单季 +11% 但前九个月仍 -1%，backlog $10.9B；FY2026 指引现为 revenue $9.690-9.740B、non-GAAP EPS $15.04-15.10、FCF 约 $2.6B，含约 $2.98B Ansys revenue。$372.33 收盘价及其倍数是明确标注日期的 2026-07-30 历史估值快照，不是当前估值。偏多 / 中确信不变：EDA 与 Ansys 证据增强，但出售 Processor IP 后的 Design IP、整合、出口和客户周期性仍限制确信度。

**当前判断：** **偏多 / 中确信。** v5 情景网格把旧的中性观察重新拆开：SNPS 的估值没有 CDNS 那么拥挤，Ansys 把 simulation 与 EDA/IP durability 合并到同一个平台，30% 牛市 / 50% 基准 / 20% 熊市的权重给出温和正偏斜；但 FY2026 指引里的 Ansys 整合、export-control 假设和客户设计周期仍需要验证。

> **旧价格复核批注 —— 按其写法已失效，被下方的重新裁定取代。** ~~2026-07-31 价格复核（本次未并入新季报）：SNPS 于 2026-07-29（最后一个已完成交易日）收于 $373.69，对照下文标注日期的 $437.16 锚点为 -14.5%，发生于已核实的 2026 年 7 月 AI 基础设施链条整体重定价期间。下文标注日期的价格、市值与倍数数字在其标注日期上依然正确，本次不予改写，但已不是当前水平，请按其标签阅读。该幅度低于本报告自身的重跑阈值（25%），因此估值框架、情景网格、立场与确信度均不变；`priceAsOf` 亦刻意保留，使本报告继续留在常规重跑队列中。~~

> **2026-07-31 立场重新裁定（锚定 2026-07-30 收盘）—— 取代上方"按标签阅读、刻意保留 `priceAsOf`"的旧处理方式。** 业主裁决（2026-07-31）：已发布的立场及其理由必须在**当前价格**上成立，因此本报告重新锚定到最后一个已完成收盘，而不是继续对着旧标签阅读。SNPS 于 **2026-07-30** 收于 **$372.33**，较 2026-07-02 的旧锚点 $437.16 为 **-14.8%**。在本报告自身未变的框架上——约 1.915 亿摊薄股本、约 $8.4B 净债务、FY2026 收入指引 $9.625-9.705B、non-GAAP EPS 指引 $14.72-14.80——市值约 **$71.3B**、EV 约 **$79.7B**，**约 8.2x EV/FY2026E sales**、**约 25.2x FY2026E non-GAAP P/E**（旧口径：约 9.5x、约 29.6x）。本次没有改动任何预估或实际值，只改了价格输入。重新推导**强化而非打破了原有前提**：偏多判断建立在"温和正预期差"之上，而市场内嵌要求（AI EDA/IP durability + Ansys 并表 + FCF 修复）对应的同一套指引框架，如今便宜了约 15%，因此该预期差在当前价格上是**变宽**的。**立场维持偏多（中确信）——依据是上述按当前价格重算的算术，而不是旧的约 9.5x / 约 29.6x 说法。** 确信度不上调：上调触发条件要求的是 Q3 FY2026 的执行证据（Ansys 收入转化、FCF 兑现约 $2.0B 指引），价格变动并不提供这类证据。

> **2026-08-27 雷达更新：Synopsys 2026-08-26 披露 FY2026 Q3 业绩与 10-Q —— Design Automation 同比 +53%、backlog $10.9B，但 Design IP 前九个月仍同比 -1%。仅为监测项更新与已披露事实的现时校正，未重算任何估值倍数，亦未在此重新裁定立场或确信度。**
>
> **披露内容。** 据 2026-08-26 提交的 Form 8-K（事项 2.02，accession 0001193125-26-368620）附件 99.1 新闻稿与同日 Form 10-Q（accession 0000883241-26-000025，季度截至 2026-07-31）：Q3 FY2026 营收 **$2,476.8M**（上年同期 $1,739.7M，同比 +42%），GAAP 每股摊薄收益 **$2.84**、non-GAAP **$3.91**。分部口径：**Design Automation $2,003.0M（同比 +53%）**、**Design IP $473.8M（同比 +11%）**；前九个月 Design Automation $5,826.6M（同比 +69%），而 **Design IP $1,335.0M，对上年同期 $1,344.7M 同比 -1%**。截至 2026-07-31 合同未履约义务（backlog）**$10.9B**，含 **$1.9B 不可撤销 FSA** 承诺；剔除不可撤销 FSA 后约 49% 预计在未来 12 个月确认。公司**上调** FY2026 全年指引至营收 **$9,690-9,740M**、non-GAAP 每股收益 **$15.04-15.10**，并给出全年经营现金流约 **$2,800M**、自由现金流约 **$2,600M**、资本开支约 **$225M**；前九个月**实际**经营活动净现金流为 **$2,298.6M**（上年同期 $878.9M）。全年营收指引含约 **$2.98B** 预期 Ansys 收入，Ansys 当季贡献 $622.2M、前九个月贡献 $2.2B。另据 2026-08-26 的 Form 8-K/A（事项 2.05，accession 0001193125-26-368858），董事会于 **2026-08-21** 将 2025-11-09 重组计划的税前费用估计由 **$300M-$350M** 上调至 **$425M-$500M**：区间两端分别增加 **$125M-$150M**，中点由 **$325M** 升至 **$462.5M**，增幅 **42.3%**。费用主要为遣散与一次性离职福利及全球厂址策略下的部分场地关闭；该文件**未将重组与 Ansys 整合相联系**，本报告亦不作此归因。
>
> **现时校正（本轮已作）。** ~~FY2026 Q2 revenue $2.276B、GAAP EPS $0.09、non-GAAP EPS $3.35；FY2026 指引 revenue $9.625-9.705B、non-GAAP EPS $14.72-14.80、FCF 约 $2.0B、含约 $2.96B Ansys revenue~~ —— 上述为 Q2 FY2026 周期口径，已被 2026-08-26 的 Q3 实际数与上调后指引取代。执行摘要、"最新报告期"与「催化与监测」中凡按 Q2 FY2026 口径书写之处，均以本条为准。
>
> **五个监测项的重评（readingAsOf 均为 2026-08-26）。** `design-automation-growth` → **`within`**；`ansys-integration` → **`within`**；`fcf-conversion` → **`within`**；`export-control-assumption` → **`within`**；`design-ip-pullthrough` → **`unclear`**。最后一项是本轮唯一未评 `within` 者，理由需要写清：该触发条件点名 memory interface IP、embedded memories、security IP 与 **processors** 四类随 custom AI silicon 扩散，而公司已于 **2026-06-01** 将 **Processor IP Solutions** 业务以现金对价 **$443.3M** 出售给 **GlobalFoundries**（税前处置收益 $425.4M，扣除 $44.9M 费用后净额 $380.5M），称此为 Design IP 分部资源向高增长机会再配置的一部分、未按终止经营列示 —— **触发条件点名的一类已从分部内移出**；叠加"季度回正（+11%）与九个月仍为负（-1%）"并存，以及 10-Q 载明 2025 年第三季度实施并其后撤销的部分 BIS 对华限制曾对含 Design IP 分部在内的在华业务产生负面影响，口径不足以判定 IP 是否随 custom AI silicon 扩散，故评 `unclear`。
>
> **证据边界。** ①同比增幅系 **Ansys 完整期间对上年同期部分期间**之比，**不是有机增长口径**。②公司明确声明 backlog 金额**不代表**未来销售或收入。③FY2026 于 **2026-10-31** 结束，`fcf-conversion` 的"兑现"只能在年度结果披露后确认，$2,600M 为**指引**而非已实现自由现金流。④8-K/A 的重组费用上调**未被该文件与 Ansys 整合相联系**，本报告不作此归因。⑤`export-control-assumption` 评 `within` 仅表示"本窗口内未发生新的破坏性变化"，**不表示该风险下降** —— 公司自陈预期未来仍有进一步变化但无法预测范围与时点。
>
> 本次仅更新监测事实与已被自身财报取代的表述，不重新裁定本报告的**偏多／中确信**立场。**2026-07-30／$372.33** 的市值约 $71.3B、EV 约 $79.7B、约 8.2x EV/FY2026E sales 与约 25.2x non-GAAP P/E，是按**当时**的 FY2026 指引口径计算的、明确标注日期的历史估值快照，**未按 2026-08-26 上调后的指引与 Q3 实际数重算**，不代表 2026-08-27 的当前估值。来源：[Q3 FY2026 新闻稿（8-K 附件 99.1）](https://www.sec.gov/Archives/edgar/data/883241/000119312526368620/d157153dex991.htm)；[Form 10-Q（截至 2026-07-31 季度）](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/snps-20260731.htm)；[Form 8-K/A（事项 2.05）](https://www.sec.gov/Archives/edgar/data/883241/000119312526368858/d135796d8ka.htm)。

| 指标 | 当前读数 |
| --- | --- |
| Report id | synopsys-2026 |
| 链条层级 / 角色 | eda-ip / common-constraint |
| 最新报告期 | FY2026 Q3（监测口径）／2026-07-30 估值框架 |
| 价格快照 | $372.33，截至 2026-07-30 |
| 本次升级后 coverageTier | full |
| Stance | 偏多 / 中确信 |
| 估值用途 | 情景与风险容错率，不是目标价 |

## 1. 业务与链条角色

业务问题不是泛泛介绍公司，而是说明 Synopsys 在 AI 基建价值链里承担什么验证工作。原报告已经建立核心事实：它是 EDA/IP 层的公共约束，因此只有当订单、收入结构、资产负债表和 monitoring 项能确认或证伪链条时，公司数据才有研究意义。

补齐 EDA/IP 公共约束：SNPS 验证 AI design starts 与复杂度是否进入 design automation、verification、simulation 和 IP

| 链条变量 | 当前事实基础 | 研究含义 |
| --- | --- | --- |
| Layer job | eda-ip / common-constraint | 限定本报告能证明的问题 |
| 需求信号 | 补齐 EDA/IP 公共约束：SNPS 验证 AI design starts 与复杂度是否进入 design automation、verification、simulation 和 IP | 应确认真实 AI 基建拉动 |
| 财务锚点 | FY2026 Q3 revenue $2.4768B、non-GAAP EPS $3.91；FY2026 revenue 指引 $9.690-9.740B、FCF 约 $2.6B | 必须体现在收入、利润率、backlog 或现金流 |
| 估值锚点 | 2026-07-30 的 $372.33；相关倍数是未按 Q3 重算的历史快照 | 决定失望容错率，同时避免把旧口径写成当前估值 |
| 交叉校验 | 与相邻报告和 coverage-map crossChecks 对照 | 避免单公司叙事 |

## 2. 行业与竞争格局

竞争判断不是普通行业排名，而是相邻节点是否确认同一条建设链。强报告应获得附近 layer 的支持；如果 peer 分化，链条解释就要降权。

| 可比 / cross-check | 为什么重要 | 如何确认 thesis |
| --- | --- | --- |
| CDNS | EDA execution peer | 证据方向与本报告一致 |
| TSM | advanced-node design pull | 证据方向与本报告一致 |
| AVGO | custom silicon demand | 证据方向与本报告一致 |
| MRVL | custom ASIC architecture check | 证据方向与本报告一致 |

竞争风险也有非对称性。公司可以很优质，但如果市场已经充分定价，或真实瓶颈转移到其他 layer，它仍可能不是好的确认信号。

## 3. 财务健康矩阵

财务部分把原报告 prose fact base 转为可复核 scorecard。评分是分析 shorthand，不是信用评级。

| 维度 | 当前证据 | 链条读法 | 评分 |
| --- | --- | --- | --- |
| 收入 / 需求 | FY2026 Q3 revenue $2.4768B；Design Automation $2.0030B（+53%），Design IP $473.8M（单季 +11%、前九个月 -1%） | 确认 EDA 强需求，同时保留 IP 的混合读数 | A-/B+ |
| 利润率 / 盈利 | 沿用原报告披露的报告期利润率、EPS、EBITDA、AFFO 或 FCF 口径 | 检验增长是有利润还是仅有规模 | B+ |
| 现金流 / 资产负债表 | 债务、现金、FCF、AFFO、EBITDA 或回购背景保留自原报告披露 | 决定公司能否承受本轮周期 | B |
| Backlog / bookings / RPO | backlog $10.9B，含 $1.9B 不可撤销 FSA；剔除该 FSA 后约 49% 预计十二个月内确认 | 区分合约需求与叙事需求，不把 backlog 当作保证收入 | B+ |
| 估值容错率 | 当前价格锚点：$372.33（2026-07-30）| 高预期标的必须有更干净的兑现 | Caution |

## 4. 管理层与口径校验

这一节检查管理层执行和数据口径，而不是添加未经验证的新预测。核心规则是把公司披露 actuals 与推导估值情景分开。

| 检查项 | 当前处理 | 为什么重要 |
| --- | --- | --- |
| 公司披露 actuals | 报告期和财务数字保留自原报告 | 避免发明新季度 |
| 市场数据 | 价格快照重新锚定为 $372.33，日期 2026-07-30 | 防止 stale valuation math |
| 情景假设 | 用增长、利润率、FCF 和 multiple regime 反推市场预期 | 不是建议或目标价 |
| 来源质量 | 公司公告、filing、issuer page 或已列 source 继续留在附录 | 保持审计线索 |

管理层在报告数字和链条角色一致时得分；如果 guidance、bookings 或资本配置依赖本报告无法验证的假设，则需要降权。

## 5. 牛市逻辑

牛市逻辑是本报告链条信号继续增强的最强版本。

| 牛市驱动 | 证据 | 更强确认 |
| --- | --- | --- |
| 需求穿透 | 补齐 EDA/IP 公共约束：SNPS 验证 AI design starts 与复杂度是否进入 design automation、verification、simulation 和 IP | 下一报告期继续确认同一方向 |
| 财务转化 | FY2026 Q2 revenue $2.276B、non-GAAP EPS $3.35；FY2026 revenue 指引 $9.625-9.705B | 收入转化为利润率、现金流或 backlog |
| 交叉校验支持 | CDNS, TSM, AVGO | 相邻报告同向移动 |
| 估值韧性 | $372.33 对应约 8.2x EV/FY2026E sales、约 25.2x non-GAAP P/E | 基本面继续验证，倍数不需要扩张也能被分母消化 |

建设性情景不只是股价上涨，而是支持本公司的同一组数据也让整条链条 read-through 更紧。

## 6. 熊市逻辑

熊市逻辑是本报告链条信号可能误导、或已经被估值充分反映的最强版本。

| 熊市驱动 | 风险证据 | thesis-breaking signal |
| --- | --- | --- |
| 预期风险 | 当前价格锚点 $372.33（2026-07-30）| 公司表现不错但已经无法超过内嵌预期 |
| 链条分化 | 相邻报告无法确认同一信号 | 瓶颈在其他 layer，或需求被提前拉动 |
| 执行风险 | guidance、backlog 或产能转化放缓 | 报告证据停止支持该角色 |
| 估值压缩 | Ansys 整合、出口限制或客户 design starts 放缓使 sales 倍数跌破 2026 年 7 月重定价后约 8.2x 的水平 | 长期故事未变但 multiple regime 先收缩 |

偏空读法不否认公司质量，而是追问质量是否已经被资本化，以及本报告是否过度外推了现有证据。

## 7. 关键不确定性与失效条件

| 不确定性 | 为什么重要 | 何时复核 |
| --- | --- | --- |
| Ansys 整合 | Ansys revenue 与 simulation 协同扩大平台，而不是稀释执行 | Q3 FY2026 integration update |
| Design Automation 增长 | AI architecture diversity 推动 verification、manufacturing software 和 system integration 需求 | segment and product demand update |
| Design IP 拉动 | memory interface IP、embedded memories、security IP 与 processors 随 custom AI silicon 扩散 | IP segment update |
| 出口管制假设 | 进一步 export-control / Entity List 变化破坏指引前提 | regulatory disclosures |
| FCF 转化 | 约 $2.6B FY2026 FCF 指引兑现，并随整合噪音下降改善 | Q4/FY2026 实际现金流 |

失效条件：

- 牛市逻辑失效：下一次报告显示需求、转化或 peer confirmation 变弱。
- 熊市逻辑失效：基本面继续改善，同时估值由现金流、backlog 或订单证据支撑。
- 链条读法失效：本报告单独移动，但相邻 layer 没有确认。

## 8. 估值背景

估值只作为风险背景，不是投资建议。v5 不再给单点价格或机械区间，而是用业务假设、multiple regime 和主观概率权重说明当前 $372.33 已经计入了什么。

**情景网格：**

| 情景 | 驱动假设（增长 / backlog / margin / multiple regime） | 估值含义（贵 / 合理 / 便宜 vs 现价） | 主观概率权重 |
| --- | --- | --- |
| 牛市情景 | Ansys simulation 与 EDA 交叉销售顺利；Design IP 在出售后的可比口径转正；FY2026 实际 FCF 兑现约 $2.6B；市场继续给予 durable software/IP multiple | 7 月历史估值框架可由分母增长支持，而无需 multiple 继续扩张 | 30% |
| 基准情景 | 上调后的 FY2026 revenue 与 EPS 指引大致兑现；Ansys 贡献约 $2.98B；Design Automation 保持强劲而出售后的 Design IP 仍混合 | 7 月历史估值框架仍是温和正偏斜，但需等待当前价格重锚 | 50% |
| 熊市情景 | Ansys 整合稀释执行、Design IP 可比口径仍为负、FCF 低于约 $2.6B 指引，或 export-control 变化破坏指引 | 盈利分母与 7 月历史估值前提会同步承压 | 20% |

**已定价预期与预期差（2026-07-31 按 2026-07-30 收盘重新推导）：** 以 2026-07-30 收盘 $372.33、EV 约 $79.7B 计，SNPS 当时约为 8.2x EV/FY2026E sales、约 25.2x FY2026E non-GAAP EPS。这个历史价格要求 AI EDA/IP durability 成立、Ansys revenue 进入 FY2026、且 FCF 暂时承压后能恢复。Q3 强化了经营分母，但本次监测更新未执行当前价格重锚，因此不重新裁定当前预期差。

## 9. 催化与监测

| 监测项 | 最新读数 | 触发器 | 下次检查 |
| --- | --- | --- | --- |
| Ansys 整合 | FY2026 指引含约 $2.98B Ansys revenue；Q3 贡献 $622.2M、前九个月 $2.2B | Ansys revenue 与 simulation 协同扩大平台，而不是稀释执行 | Q4/FY2026 财报 |
| Design Automation 增长 | Q3 revenue $2.0030B（+53%）；前九个月 $5.8266B（+69%） | AI architecture diversity 推动 verification、manufacturing software 和 system integration 需求 | segment and product demand update |
| Design IP 拉动 | Q3 revenue $473.8M（+11%），但前九个月仍 -1%；Processor IP 已于 6 月 1 日出售 | memory interface、embedded memory 与 security IP 在出售后可比口径扩散 | 出售后可比口径更新 |
| 出口管制假设 | 公司指引假设没有进一步 export-control / Entity List 变化 | 进一步 export-control / Entity List 变化破坏指引前提 | regulatory disclosures |
| FCF 转化 | FY2026 operating cash flow 指引约 $2.8B、FCF 约 $2.6B；前九个月实际经营现金流 $2.2986B | 约 $2.6B FY2026 FCF 指引兑现，并随整合噪音下降改善 | Q4/FY2026 实际现金流 |

未来 rerun 应由这些项目触发。只有当 monitoring update 改变链条 read-through 或估值容错率时，报告才需要实质更新。

## 10. 同行比较与结论

| Peer / benchmark | 研究书中的角色 | 与本报告如何对照 |
| --- | --- | --- |
| CDNS | EDA execution peer | 确认、反驳或限定同一链条问题 |
| TSM | advanced-node design pull | 确认、反驳或限定同一链条问题 |
| AVGO | custom silicon demand | 确认、反驳或限定同一链条问题 |
| MRVL | custom ASIC architecture check | 确认、反驳或限定同一链条问题 |

链条验证工作不变：Synopsys 是 EDA/IP 层的公共约束，用来确认 AI silicon 需求是否真正进入 design automation、verification、simulation、IP blocks 和 system-level complexity。

在明确标注日期的 2026-07-30 框架中，$372.33、约 8.2x EV/FY2026E sales 和约 25.2x non-GAAP P/E 对应温和正向预期差。Q3 强化了经营分母，但本次监测更新不把旧框架呈现为当前估值，也不重新裁定预期差。

当前 stance 是 **偏多，中确信**。30% 牛市 / 50% 基准 / 20% 熊市的情景网格给出正偏斜：牛市来自 Ansys+EDA/IP 平台化，基准来自 FY2026 指引兑现和 FCF 恢复，熊市主要来自整合、出口与客户周期性。中确信来自事实基础较扎实，但 Ansys 整合和 export-control 假设仍未完成验证。

升级触发条件：若 FY2026 全年实际自由现金流兑现约 $2.6B 指引，Ansys 与 Design Automation 继续按计划增长，Design IP 在出售 Processor IP 后的可比口径恢复正增长，且没有新增 export-control / Entity List 冲击，则上调至 bullish。降级触发条件：若 Ansys 整合稀释执行、Design IP 在出售后的可比口径仍未转正、Design Automation 增长低于 AI 复杂度叙事、全年自由现金流低于约 $2.6B 指引，或新增 export-control / Entity List 变化破坏 FY2026 指引，则下调至 neutral-watch 或 cautious。

## 附录：来源与假设

- Synopsys FY2026 Q2 10-Q：[SEC filing](https://www.sec.gov/Archives/edgar/data/883241/000088324126000018/snps-20260430.htm)。
- Synopsys FY2026 Q2 earnings release：[Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/883241/000119312526241911/d126227dex991.htm)。
- Synopsys FY2026 Q3 新闻稿（2026-08-26，8-K 事项 2.02 附件 99.1）：[Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/883241/000119312526368620/d157153dex991.htm)——营收 $2,476.8M、Design Automation $2,003.0M、Design IP $473.8M、FY2026 指引上调
- Synopsys FY2026 Q3 10-Q（季度截至 2026-07-31，2026-08-26 提交）：[SEC filing](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/snps-20260731.htm)——分部与九个月口径、backlog $10.9B、前九个月经营现金流 $2,298.6M、Processor IP 出售、出口管制段
- Synopsys Form 8-K/A（2026-08-26，事项 2.05）：[SEC filing](https://www.sec.gov/Archives/edgar/data/883241/000119312526368858/d135796d8ka.htm)——重组税前费用估计上调至 $425M-$500M（董事会 2026-08-21 批准）

- 2026-07-06 深度升级保留原先已核验事实基础，并补齐结构、表格、同行比较和 monitoring parity。
- 2026-07-07 v5 backfill 用情景假设、概率权重和已定价预期替代旧机械价格标尺；这些是预期校准框架，不构成投资建议、预测或目标价。
