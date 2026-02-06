# Currency Dashboard 维护说明

`/invest/currency/` 已迁移到主博客仓库，不再独立部署。

## 目录结构

```
static/invest/currency/
├── index.html
├── css/style.css
├── js/main.js
├── data/historical.json
├── fetch_historical_data.py   # 初始化/重建历史数据
├── update_real_data.py        # 日更数据（upsert 当天）
├── validate_data.py           # 数据完整性校验
└── check_alerts.py            # 偏离预警检查（本地脚本）
```

## 本地预览

在仓库根目录运行：

```bash
hugo server -D
```

访问 `http://localhost:1313/invest/currency/`。

## 数据更新链路

### 自动更新（推荐）

GitHub Actions：`.github/workflows/update-currency-data.yml`

流程：
1. 执行 `python3 static/invest/currency/update_real_data.py`
2. 执行 `python3 static/invest/currency/validate_data.py`
3. 仅当 `data/historical.json` 有变化时自动提交

默认每天 UTC `00:00` 运行（北京时间 `08:00`），也支持手动触发。

### 手动更新

```bash
python3 static/invest/currency/update_real_data.py
python3 static/invest/currency/validate_data.py
```

## 首次初始化或重建历史数据

```bash
python3 static/invest/currency/fetch_historical_data.py
python3 static/invest/currency/validate_data.py
```

## 数据源与 schema

- 数据源：`@fawazahmed0/currency-api`
- 当前统一基准货币：`USD`
- 监控货币：`CNY`、`SGD`、`JPY`、`AUD`
- `historical.json.metadata` 关键字段：
  - `base_currency` / `base`
  - `currencies`
  - `total_days`
  - `start_date`
  - `end_date`
  - `last_updated`

## 注意事项

- 主题切换由共享脚本 `/shared/theme-switcher.js` 提供。
- 汇率分析为个人跟踪用途，不构成投资或交易建议。
