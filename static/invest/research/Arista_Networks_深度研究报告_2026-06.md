# Arista Networks（NYSE: ANET）深度研究报告

标的收录日期：2026-06-30
最近更新日期：2026-06-30
代码：NYSE: ANET
免责声明：本报告仅用于信息与研究交流，不构成任何投资建议，请自行完成尽职调查。所有价格与市值为时点快照，财务数字以公司披露口径为准。

> **背景说明：** 本报告为 Arista Networks 在 AI 基础设施书中的首次覆盖。请配合阅读 NVIDIA、Broadcom、AAOI、Corning、Vertiv 与 CoreWeave。ANET 不是 GPU/加速器层，不是有源光模块层，也不是光纤/光缆层。它是开放以太网交换系统、EOS/CloudVision 软件、遥测和 AI 数据中心 fabric 层，用来检验 AI 集群会标准化在开放以太网和 merchant silicon 上，还是更多网络价值会迁移到 NVIDIA 的垂直一体化堆栈。

---

## 执行摘要

**一句话论点：** Arista 是 AI 集群网络里“开放以太网”路线最清晰的公开市场表达 - 一家高质量、高利润率的系统软件公司，但股价已经反映了很多 Ethernet 份额提升预期。

**当前判断：** **中性 / 高质量但高预期（观察）。** 我更愿意在估值回落，或者开放以太网在 AI 后端网络中拿到更明确、可持续份额证据时，才把 ANET 从“必须跟踪”提升为“积极买入”。公司本身具备本中心喜欢的质量：高增长、高利润率、大额净现金、深度 hyperscaler 暴露，而且直接回答 AI 集群架构问题。但估值已经预支了多年 AI 网络扩张和非常高的执行质量。

**它在本覆盖结构中的意义：** ANET 是 AI 基础设施书的网络 fabric 仪表盘。若 Arista 继续扩大递延收入/RPO、维持 40%+ 营业利润率，并证明大型 AI 客户在规模化选择 Ethernet fabric，这会支持 Broadcom、AAOI、Corning、Vertiv 以及部分 neocloud 需求链。反过来，如果 Arista 减速，或被 NVIDIA 一体化网络栈挤压，它会成为 AI 基础设施多头书的早期预警。

**当前市场口径：** CompaniesMarketCap/Nasdaq 显示 2026 年 6 月 29 日收盘市值为 **$206.62B**。按 Arista 2026 年 4 月 30 日 **12.59 亿股**流通股计算，对应约 **$164/股**。以 Q1 2026 现金及可交易证券约 **$12.35B**、基本无有息债务计算，企业价值约 **$194B**。

**关键数据：**

| 指标 | 当前读数 |
|----|----|
| AI 链条位置 | 开放以太网 AI 集群 fabric：交换系统、EOS、CloudVision、遥测 |
| 市值 | 2026 年 6 月 29 日收盘 $206.62B |
| 隐含股价 | 按 12.59 亿股流通股约 $164/股 |
| 企业价值 | 扣除现金及可交易证券后约 $194B |
| Q1 2026 收入 | $2.709B，同比增长 35.1% |
| Q1 2026 非 GAAP 营业利润率 | 47.8% |
| Q1 2026 非 GAAP EPS | $0.87 |
| Q1 2026 经营现金流 | $1.69B |
| FY2025 收入 | $9.006B，同比增长 28.6% |
| FY2025 客户结构 | 48% Cloud and AI Titans，32% Enterprise，20% AI and Specialty Providers |
| FY2025 产品结构 | 65% Core AI/Cloud/Data Center Networking，18% Cognitive Adjacencies，17% Software and Services |
| 客户集中度 | 两个匿名终端客户分别占 FY2025 收入 26% 和 16% |
| 核心争议 | 开放以太网 + Broadcom merchant silicon + Arista EOS，还是 NVIDIA 一体化网络栈 |

---

## 1. 业务概览

Arista 销售云网络系统和软件，服务大规模数据中心、AI 集群、企业园区、路由和 WAN 场景。公司财务上披露一个经营分部，但战略上用“Centers of Data”拆解市场：AI Centers、Data Centers、Campus Centers、WAN Centers。

真正重要的产品栈有四层：

| 层级 | 在堆栈中的角色 |
|----|----|
| 交换与路由平台 | 高容量交换机、路由器、AI spine/leaf 平台和数据中心系统 |
| EOS | 基于 Linux、状态导向的网络操作系统，目标是在不同硬件平台上保持一致性 |
| CloudVision / NetDL / AVA | 网络遥测、自动化、数据湖式可观测性和 AI 辅助运维 |
| Etherlink / AI networking 平台 | 800G 系统、AI spine/leaf 设计、虚拟输出队列、大 buffer、负载均衡与拥塞管理 |

Q1 2026 中，产品收入 **$2.311B**，服务收入 **$398M**。这个结构很关键：Arista 仍然主要是系统公司，不是纯 SaaS 公司。软件层的意义在于增强客户粘性和运维可靠性，但近期收入引擎仍然是高性能网络硬件。

业务也已经深度绑定 hyperscaler。FY2025 中，Cloud and AI Titans 占收入 **48%**，AI and Specialty Providers 占 **20%**，Enterprise 占 **32%**。产品结构也显示同一件事：Core AI/Cloud/Data Center Networking 占收入 **65%**，Cognitive Adjacencies 占 **18%**，Software and Services 占 **17%**。

## 2. 行业与竞争位置

AI 训练和推理集群不只是加速器问题。几千、几万甚至更多 GPU/XPU/自研加速器连在一起时，整个集群会变成一台网络化的计算机。如果网络 fabric 丢包、延迟高、拥塞管理差，昂贵算力就会空转。因此 AI 后端网络已经不再是普通企业网络更新，而是战略战场。

Arista FY2025 10-K 把 AI 网络拆成三层：**Scale Up** 连接近距离加速器；**Scale Out** 跨机架连接加速器；**Scale Across** 连接集群、数据中心和区域。Scale Up 当前仍更偏专有技术，Scale Out 和 Scale Across 则是开放以太网挑战 InfiniBand 等专有路线最清晰的区域。

### 2.1 NVIDIA：架构竞争，不只是横向对比

NVIDIA 拥有最强的一体化 AI 计算栈：GPU、CUDA、系统、InfiniBand、NVLink/NVSwitch、Spectrum-X Ethernet。Arista 是另一条路线：最佳单点开放以太网系统，叠加 Arista 软件和 merchant silicon。问题不是两家公司能不能同时增长，而是 AI 集群网络的边际价值会流向哪里。

如果客户更看重全栈优化和最快部署路径，NVIDIA 胜率更高。如果 hyperscaler 和 AI 建设者更想要供应商多元化、以太网标准化、运维控制权和跨多种加速器的网络 fabric，ANET 胜率更高。

### 2.2 Broadcom：先是供应商/伙伴，其次才是隐性风险

Arista FY2025 10-K 明确表示，公司主要依赖 Broadcom 供应 merchant switching chips。因此 ANET 是 Broadcom 以太网生态的重要客户和验证者，而不是简单的横向竞争者。Broadcom 赚芯片，Arista 赚系统、EOS、CloudVision、客户部署和运维可靠性的钱。

这很强，但也是风险。Arista 的产品路线图部分受 merchant silicon 可得性、价格和节奏约束。如果 Broadcom 供应紧张、某代芯片延迟，或者 hyperscaler 越来越多自研网络系统，ANET 的利润率和成长叙事都可能变化。

### 2.3 光层、电力层与需求链交叉验证

AAOI 覆盖有源光模块/transceiver。Corning 覆盖光纤、光缆和被动光连接材料。ANET 位于这些层之上，是网络系统和 fabric 厂商。更多 800G AI spine 和 scale-out 网络，意味着更多光链路、更高光纤/光缆密度、更多数据中心连接内容。因此 ANET 是光层需求的架构信号，而不是 AAOI/Corning 的重复覆盖。

Vertiv 和 CoreWeave 补齐交叉验证。VRT 告诉我们数据中心电力与散热设备是否在真实交付。CRWV 告诉我们一部分 AI 需求是否被高杠杆和循环承诺放大。ANET 位于中间：它应当反映实际集群是否正在被连线和上线。

## 3. 财务健康

### 3.1 Q1 2026 与 FY2025 基准

Q1 2026 展现了高质量增长。收入 **$2.709B**，同比增长 **35.1%**，环比增长 **8.9%**。GAAP 营业利润率 **42.7%**，非 GAAP 营业利润率 **47.8%**，GAAP 摊薄 EPS **$0.80**，非 GAAP 摊薄 EPS **$0.87**，经营现金流 **$1.69B**。

| 指标 | Q1 2026 | 解读 |
|----|----|----|
| 收入 | $2.709B | 同比 +35.1%，环比 +8.9% |
| 产品收入 | $2.311B | 主要增长引擎 |
| 服务收入 | $398M | 较小但粘性更强 |
| GAAP 毛利率 | 61.9% | 对系统公司而言非常高 |
| 非 GAAP 毛利率 | 62.4% | 仍然强劲 |
| GAAP 营业利润率 | 42.7% | 极高 |
| 非 GAAP 营业利润率 | 47.8% | 同业顶级盈利能力 |
| GAAP 摊薄 EPS | $0.80 | 利润质量高 |
| 非 GAAP 摊薄 EPS | $0.87 | Q2 指引显示延续性 |
| 经营现金流 | $1.69B | 现金转化非常强 |

FY2025 收入 **$9.006B**，同比增长 **28.6%**。GAAP 净利润 **$3.511B**，GAAP 摊薄 EPS **$2.75**；非 GAAP 净利润 **$3.806B**，非 GAAP EPS **$2.98**。FY2025 GAAP 毛利率 **64.1%**，非 GAAP 毛利率 **64.6%**。

### 3.2 资产负债表、现金流与可见度

截至 2026 年 3 月 31 日，Arista 现金及现金等价物约 **$2.79B**，可交易证券约 **$9.56B**，合计约 **$12.35B**。公司没有明显有息债务负担。Q1 2026 资本开支约 **$55M**，当季自由现金流转化非常高。

递延收入和剩余履约义务是重要观察项。2026 年 3 月 31 日，当前递延收入约 **$4.91B**，非当前递延收入约 **$1.29B**。公司还披露，来自合同负债、递延收入和其他履约义务的未来收入约 **$7.7B**，其中约 **91%** 预计未来两年确认。这给了可见度，但不能等同于无条件 backlog；客户验收期、部署节奏和架构选择仍然重要。

### 3.3 指引与质量检查

Q2 2026 指引为收入约 **$2.8B**、非 GAAP 营业利润率 **46-47%**、非 GAAP 摊薄 EPS 约 **$0.88**。以 Q2 2025 收入 **$2.205B** 为基数，这隐含约 **27%** 同比增长 - 仍然强劲，但低于 Q1 2026 的 **35.1%** - 同时保持极高利润率。

主要财务质量问题不是杠杆，而是集中度和时点。Arista 披露两个匿名终端客户分别占 FY2025 收入 **26%** 和 **16%**，合计 **42%**。公司没有官方点名；正式研究应坚持官方披露的匿名口径，不把市场猜测写成事实。在这个集中度下，任何一家架构切换或资本开支暂停都会很重要。

## 4. 管理层与治理

Jayshree Ullal 仍担任 CEO 和董事会主席。Kenneth Duda 是总裁兼 CTO。Chantelle Breithaupt 是 CFO。Todd Nightingale 是总裁兼 COO。这个管理团队技术底色很强，Arista 的历史经营表现也显示出很高执行纪律。

管理层质量是正面因素。Arista 多次证明自己可以在高速增长下维持高利润率和强现金流。投资者真正需要担心的，不是明显治理问题，而是管理层能否继续处理 hyperscaler 客户集中、merchant silicon 依赖和 AI 架构切换，同时避免库存过度和利润率牺牲。

Q4/FY2025 release 还给了几个执行可信度信号：累计出货 **1.5 亿端口**，下一代 data/AI center networks，AI 运维工具，ESUN 参与，以及从 Broadcom 收购 VeloCloud SD-WAN portfolio。这些不能消除执行风险，但支持 Arista 是少数同时拥有技术深度和 hyperscaler 运维信任的厂商。

## 5. 牛市观点

1. **开放以太网拿到更多 AI 后端网络份额。** 若大型云和 AI 客户在 scale-out 集群中标准化 Ethernet，Arista 有很强胜率。EOS、CloudVision、大 buffer spine 平台、高速 Ethernet 系统，正好对应这个架构。

2. **Hyperscaler 需要供应商多元化和运维控制权。** 拥有庞大内部工程团队的客户，通常不愿完全绑定单一垂直一体化堆栈。客户希望混用加速器、标准化运维、保持网络选择模块化时，Arista 受益。

3. **Broadcom merchant silicon 继续成为生态重心。** 如果 Broadcom 能持续按节奏交付有竞争力的 switching silicon，ANET 可以把芯片能力转化成成品系统和软件价值，而不必承担完整自研芯片风险。

4. **软件和遥测提高锁定。** CloudVision、NetDL、AI 辅助运维不等于纯 SaaS，但一旦客户把网络运维流程建立在这些工具上，Arista 的替换难度会上升。

5. **AI 光层成为结构性拉动。** 更多 800G 及后续更高速部署，应支持 AAOI 这样的有源光模块需求，以及 Corning 这样的光纤/光缆/被动连接需求。ANET 可作为这条拉动的领先信号。

## 6. 熊市观点

1. **NVIDIA 一体化网络栈捕获更多价值。** 如果 Spectrum-X、InfiniBand、NVLink/NVSwitch 和 NVIDIA 系统成为 AI 集群默认架构，Arista 仍可增长，但它在最高价值 AI 网络机会中的份额可能低于多头预期。

2. **客户集中度很高。** 两个匿名终端客户分别占 FY2025 收入 **26%** 和 **16%**。两家合计 **42%** 收入，任何一家资本开支暂停、设计切换或份额流失，都会影响合并增长率。

3. **Broadcom 依赖是双刃剑。** Broadcom 既是生态优势，也是供应商集中风险。Arista 没有长期保证供应合同，其产品路线图依赖与 merchant silicon 厂商的紧密合作。

4. **估值容错率低。** 约 **20x EV/TTM 收入**、约 **47x 当前非 GAAP EPS 运行率**下，即使公司仍然优秀，普通减速也可能让股价承压。

5. **白盒、自研和客户议价压力仍然存在。** 大型云客户有能力拆解系统、自行设计或压低系统毛利。Arista 的护城河是可靠性、软件深度和客户共创，不是免疫客户议价。

## 7. 关键不确定性

1. **Ethernet vs NVIDIA 一体化网络。** 如果 NVIDIA 一体化网络栈成为大型 AI 集群默认选择，ANET 的 AI 机会会变窄。

2. **Scale-up 时间点。** Scale Up 当前仍更偏专有技术。Ethernet 能否更深入 scale-up networks，仍是未来机会，不是完全验证的当前基准情景。

3. **头部客户行为。** 两大匿名客户占 FY2025 收入 **26%** 和 **16%**，会主导季度节奏、库存和部署时点。

4. **RPO/递延收入耐久性。** **$7.7B** 未来收入披露支持可见度，但确认取决于客户部署、验收和架构选择。

5. **Broadcom 芯片节奏。** Arista AI 系统依赖 merchant silicon 路线图。延迟、短缺或价格压力会影响产品时点和利润率。

6. **利润率结构。** AI 规模客户大且议价力强。若非 GAAP 营业利润率跌破 **40%**，且没有清晰投资解释，应视为 thesis warning。

7. **库存和采购承诺。** 大额采购义务在需求时点改变时，会迅速转化为库存风险。

## 8. 估值上下文

按 2026 年 6 月 29 日收盘市值 **$206.62B** 和 Q1 2026 现金/可交易证券约 **$12.35B** 计算，企业价值约 **$194B**。按 2026 年 4 月 30 日 **12.59 亿股**流通股，对应股价约 **$164/股**。

| 指标 | 粗略数值 | 解读 |
|----|----|----|
| 市值 | $206.62B | CompaniesMarketCap/Nasdaq 2026-06-29 收盘 |
| 现金 + 可交易证券 | $12.35B | 2026-03-31 |
| 企业价值 | $194B | 基本无有息债务 |
| TTM 收入 | $9.71B | FY2025 收入 - Q1 2025 + Q1 2026 |
| EV / TTM 收入 | ~20x | 需要持续增长支撑 |
| TTM GAAP 净利润 | $3.72B | FY2025 净利润 - Q1 2025 + Q1 2026 |
| 市值 / TTM GAAP 净利润 | ~56x | 高预期 |
| 当前非 GAAP EPS 运行率 | ~$3.5 | Q1/Q2 约 $0.87-0.88/季度 |
| 股价 / 当前非 GAAP EPS 运行率 | ~47x | 质量已被定价 |

这个估值只有在几件事同时成立时才容易消化：AI 集群网络需求继续强、Ethernet 拿到足够份额、Arista 保持 hyperscaler 信任、Broadcom merchant silicon 持续可得且有竞争力、AI 客户放量时利润率不大幅压缩。

## 9. 催化剂与监控清单

1. **Q2 2026 业绩和 Q3 指引。** 收入接近或高于 **$2.8B**，非 GAAP 营业利润率保持 **46-47%**，叙事才稳。

2. **客户集中度。** 观察前两大客户是否仍在 **40%+** 收入附近，以及任何一家是否出现明显加速或暂停。

3. **递延收入/RPO。** **$7.7B** 未来收入基础继续增长，会支持可见度；若走弱，会挑战 AI 建设叙事。

4. **Ethernet vs NVIDIA networking。** 跟踪客户架构评论、Spectrum-X 采用、InfiniBand 替代、Ultra Ethernet/ESUN 进展。

5. **Broadcom 芯片节奏。** 供应限制、价格压力或路线图延迟，都会影响 Arista AI 系统交付和利润率。

6. **光层拉动。** ANET 强势应当在 AAOI/Corning 的需求信号中有所体现。

7. **现金转化。** Q1 2026 经营现金流 **$1.69B** 很强。若自由现金流转化持续，会支撑质量溢价。

8. **利润率底线。** 若非 GAAP 营业利润率跌破 **40%**，且没有清晰投资解释，说明 AI mix、客户折扣或竞争压力强于预期。

## 10. 结论

ANET 是 AI 基础设施覆盖图里必须补上的一层，因为它回答的是网络层最终变成开放 Ethernet 系统/软件机会，还是变成加速器厂商垂直一体化堆栈机会。公司质量高、资产负债表强、利润率极好，并且直接暴露于 AI 集群建设。

但股价已经理解了很多正确叙事。约 **$206.6B** 市值、约 **$164/股**、约 **20x EV/TTM 收入**、约 **47x 当前非 GAAP EPS 运行率**，意味着证明责任在多头一边。当前最合理判断是 **中性/观察**：承认公司质量，但等待更好价格，或等待开放以太网份额提升仍被市场低估的更强证据。

## 附录：来源与假设

- Arista Networks Q1 2026 earnings release，2026 年 5 月 5 日 Form 8-K Exhibit 99.1：<https://www.sec.gov/Archives/edgar/data/1596532/000159653226000074/ex991q126-earningsrelease.htm>
- Arista Networks 2026 年一季度 Form 10-Q：<https://www.sec.gov/Archives/edgar/data/1596532/000159653226000078/anet-20260331.htm>
- Arista Networks FY2025 Form 10-K：<https://www.sec.gov/Archives/edgar/data/1596532/000159653226000013/anet-20251231.htm>
- Arista Networks Q4/FY2025 earnings release，2026 年 2 月 12 日 Form 8-K Exhibit 99.1：<https://www.sec.gov/Archives/edgar/data/1596532/000159653226000010/ex991q425-earningsrelease.htm>
- Arista Networks Q2 2025 earnings release，2025 年 8 月 5 日 Form 8-K Exhibit 99.1：<https://www.sec.gov/Archives/edgar/data/1596532/000159653225000214/ex991q225-earningsrelease.htm>
- CompaniesMarketCap 的 ANET 市值页面，含 2026 年 6 月 29 日收盘市值：<https://companiesmarketcap.com/arista-networks/marketcap/>
- Nasdaq ANET market activity page，用作市场数据交叉参考：<https://www.nasdaq.com/market-activity/stocks/anet>

估值粗算使用 Q1 2026 现金及可交易证券、基本无有息债务、Q1 2026 股本、FY2025 报告值、Q1 2025/Q1 2026 报告值，以及 2026 年 6 月 29 日收盘市值。所有倍数均为四舍五入。
