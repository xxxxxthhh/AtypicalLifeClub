# Currency Dashboard 使用指南

## 访问入口

- 本地：`http://localhost:1313/currency/`
- 线上：`https://atypicallife.club/currency/`

## 页面功能

1. 选择基础货币（默认 `SGD`）
2. 选择目标货币
3. 选择时间范围（30/90/180/365/730 天）
4. 查看统计卡片、走势图和均值偏离区间（±1σ / ±2σ）

## 日常维护

### 手动拉取最新数据

```bash
cd static/currency
python3 update_real_data.py
python3 validate_data.py
```

### 手动检查偏离预警

```bash
cd static/currency
python3 check_alerts.py
```

### 重建历史数据

```bash
cd static/currency
python3 fetch_historical_data.py
python3 validate_data.py
```

## 自动任务

- 工作流：`.github/workflows/update-currency-data.yml`
- 默认每天 UTC `00:00`（北京时间 `08:00`）
- 可在 GitHub Actions 页面手动点击 `Run workflow`

## 常见问题

- 页面提示加载失败：先确认 `data/historical.json` 存在且通过 `validate_data.py`。
- 图表异常：检查 `historical.json` 是否有重复日期或缺失货币字段。
