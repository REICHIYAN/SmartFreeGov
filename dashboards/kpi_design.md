# 📊 SmartFreeGov KPI設計メモ

---

## ✅ 使用テーブル

- BigQuery: `smartfreegov_ds.faq_query_logs`

---

## 📈 グラフ 1｜クエリ件数の推移

- グラフタイプ：折れ線
- ディメンション：`timestamp`（→ 日単位に集約）
- 指標：`Record Count`

---

## 📊 グラフ 2｜解決率（is_resolved）

- グラフタイプ：円グラフ
- ディメンション：`is_resolved`
- 指標：`Record Count`

---

## ✏️ 今後の拡張案

- `source` ごとの利用傾向（CLI vs Colab）
- `response_time_ms` によるパフォーマンス分析
- `user_id` / `category` カラム追加によるセグメント別集計
