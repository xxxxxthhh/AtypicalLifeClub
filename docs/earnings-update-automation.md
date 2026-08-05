# 财报更新定时任务：创建方式与责任边界

## 固定入口

- `static/invest/research/data/earnings-calendar.json` 是所有当前公司财报日期的唯一结构化入口；`reports.json` 中带 `ETF` tag 的标的不进入财报日历。
- `static/invest/research/data/earnings-tasks.json` 是每日生成的任务队列。它是待办输入，不是已完成证明，也不会自动修改或发布研报。
- `reports.json[].monitoring[].nextCheckDate` 继续只承载 `YYYY-MM` 的论文监测窗口，供 verdict 月级逾期判断使用；不要在这里塞入财报日精度。

## 日历记录的创建与升级

每个当前非 ETF `reportId` 必须且只能有一条记录。最低字段为：

```json
{
  "reportId": "example-2026",
  "company": "Example",
  "timezone": "America/New_York",
  "expectedDate": "2026-08-26",
  "precision": "day",
  "status": "issuer-confirmed",
  "session": "after-close",
  "sourceUrl": "https://issuer.example/investors/...",
  "sourceType": "issuer-ir",
  "verifiedAt": "2026-08-01"
}
```

状态升级规则：

1. `unknown`：没有结构化日期，必须使用 `precision: unknown`、`expectedDate: null`、`sourceType: none`。
2. `estimated`：只有月份或第三方估计；使用 `precision: month|day` 和 `sourceType: monitoring`，只能用于补全/复核日期提醒。
3. `recorded`：报告正文已有精确日期，但公司 IR 尚未复核；必须使用 `precision: day` 和 `sourceType: report-body`，只能生成来源复核任务。
4. `issuer-confirmed`：精确日已由公司 IR/官方公告确认，必须使用 `precision: day`、`sourceType: issuer-ir`，提供 HTTPS `sourceUrl`、ISO `verifiedAt`，并把 `session` 明确为 `before-open`、`after-close` 或 `during-market`；只有这一状态可触发正式研究更新。
5. `stale`：已有来源的日期已过且没有完成新周期确认；进入每周维护队列。

`defaultTimezone` 是大多数美股公司事件日期的默认 IANA 时区。若公司的财报日期按其他本地市场定义（例如韩国、上海、台湾、香港或荷兰），必须在对应记录写入 `timezone` 覆盖值。定时任务按每条记录的事件本地日期计算 T-1/T/T+1，不能直接用 UTC 日历日。

维护人取得新的公司 IR 证据后，同一次变更更新 `expectedDate`、`precision`、`status`、`session`、`sourceUrl`、`sourceType`、`verifiedAt`，然后运行：

```bash
python3 static/invest/research/validate_earnings_calendar.py
python3 static/invest/research/earnings_tasks.py --date YYYY-MM-DD
python3 -m unittest discover -s static/invest/research -p "test_*.py"
```

校验器会 fail-closed：缺少当前公司、公司名与 `reports.json` 不一致、误收 ETF、重复 `reportId`、非法真实年月/日期/时区、状态与精度组合不合法、验证日晚于日历 `asOf`，或缺少公司 IR HTTPS 来源及明确事件时段的 `issuer-confirmed` 都会失败。

## 定时任务怎样运行

GitHub Actions 的 `.github/workflows/update-research-prices.yml` 每日 `22:00 UTC` 运行，也可用 `workflow_dispatch` 手动运行。它在现有价格、verdict、calibration 流程中增加两步：先校验财报日历，再以当前 UTC 时刻转换到每条记录的事件时区，生成任务队列。`generatedAt` 保存秒级 UTC 时间戳；`reference` 保存可重放的参考模式和值。正常运行使用 `instant`，`--date YYYY-MM-DD` 测试/回放使用 `literal-date`，把同一个字面日期应用到所有记录。

队列规则：

- `issuer-confirmed + day`：只在 T-1、T、T+1 生成 `research-update`。
- `recorded`：每周一生成 `source-verification`，不得直接更新研报。
- `estimated`（月或第三方日精度）：每周一生成 `date-completion`。
- `unknown` / `stale`：每周一生成 `calendar-maintenance`。
- 日精度日期已过（T+1 之后）：无论状态，每周一生成 `calendar-maintenance`，提醒把记录滚动到下一周期；过期记录不会静默消失。
- 去重键固定为 `earnings:<reportId>:<expectedDate|unknown>:<window>`。下游任务系统必须以该键幂等消费，不能重复开相同任务。

本仓库当前把队列提交回 `main`，不直接创建 GitHub Issue，也不自动发布研究结论。若以后接入 Issue、Agent Office 或其他执行器，它只能读取队列并保留上述去重键和 fail-closed 规则。

## 责任分工

| 责任人/系统 | 责任 | 不负责 |
| --- | --- | --- |
| 定时 workflow | 每日校验日历、生成确定性队列、提交数据变化 | 判断财报内容、改变投资立场、自动发布 |
| 日历维护人 | 优先用公司 IR，维护日期、盘前/盘后、来源和验证日 | 把第三方估计冒充公司确认 |
| 研究执行人 | 消费 `research-update`，核对财报/filing/电话会，更新中英文报告、metadata 和必要的 signal | 仅凭任务出现就沿用旧估值或旧结论 |
| Reviewer | 按任务 id 检查来源、双语一致性、估值边界、验证输出和 diff | 用绿测替代事实复核 |
| Integrator | 只提交已 review、验证通过的最小变更；保留任务 id 作为审计线索 | 合并未确认来源或失败校验的更新 |

研究更新仍必须遵守 `static/invest/research/README.md`：监测读数需要相应 signal；估值敏感内容必须重算或清楚标为旧锚；运行 reports、coverage、prices、verdicts、feed 和构建检查。财报任务只决定何时复核，不替代研究与发布门槛。

## 修改 cron

如确需改运行时间，只修改 workflow 的 `on.schedule` cron，并同时检查覆盖市场的收盘时区。GitHub cron 使用 UTC；当前 `22:00 UTC` 是为了在美股和亚洲市场当日收盘后统一生成数据。改动 cron 必须经 review，并在本文件同步记录新的时区理由。
