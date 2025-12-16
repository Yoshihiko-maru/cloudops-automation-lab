# Runbook: ServiceDown

## Purpose
`ServiceDown`（`up{job="cloudops_app"} == 0` が継続）を検知した際に、原因切り分けと復旧を最短で行う。

- Severity: critical
- Rule: `up{job="cloudops_app"} == 0 for 30s`
- Meaning: Prometheus が `/metrics` を 30 秒間 scrape できない

## Impact (expected)
- `cloudops_app` が応答不能または不安定
- 監視データが取得不能のため、診断・復旧判断も遅延する

## First checks (2 minutes)
### 1) Confirm alert state
- Prometheus → Alerts: `ServiceDown` が `PENDING` / `FIRING` か確認
- Alertmanager → Alerts: 受信できているか確認（通知経路の健全性）

### 2) Confirm scrape target
Prometheus → Status → Targets
- `job="cloudops_app"` が **DOWN** なら、アプリ停止/疎通不全が疑わしい
- **UP** なのにアラートが出る場合は、ラベル/ルール不整合を疑う

### 3) Confirm metric series
Prometheus → Graph
```promql
up{job="cloudops_app"}
