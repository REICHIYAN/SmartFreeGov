# 🏡 SmartFreeGov - Retrieval-Augmented FAQ Generator

BigQuery × GPT-4 による「自治体FAQ自動応答システム」のPoC（RAG構成）です。

---

## ✨ What is this?

* ❓ 市民の自然文質問に対して
* 📂 BigQueryに蓄積されたFAQをもとに
* 🧠 GPT-4で自動的に自然言語応答を生成

→ 行政・教育・ヘルプデスクなどの「FAQ業務」の自動化を目指すプロトタイプです。

---

## 🧹 System Architecture

```txt
[User Query]
     │
     ▼
[Local Embedding (MiniLM)]
     │
     ▼
[BigQuery FAQ検索 (cosine類似度)]
     │
     ▼
[Top-K類似FAQ → Prompt生成]
     │
     ▼
[OpenAI GPT-4 応答生成]
     │
     ▼
[Answer Output]
```

---

## 🚀 Quickstart（CLI実行）

### 🔧 Step 1. `.env` にキーを設定

```
OPENAI_API_KEY=sk-...
BQ_PROJECT_ID=ambient-empire-429902-p2
BQ_DATASET_ID=smartfreegov_ds
BQ_TABLE_NAME=faq_table
```

### ▶ Step 2. パイプライン実行

```bash
PYTHONPATH=. python3 tests/run_pipeline_test.py
```

---

## 🧺s Try it on Colab（非技術者向け）

* ▶ [SmartFreeGov\_RAG\_demo.ipynb](notebooks/SmartFreeGov_RAG_demo_fixed.ipynb) を開いて、GUIで体験できます
* GCPキー（JSON）をアップロード後、OpenAIキーを入力すれば動作します

> ⚠ Colab左側の「ファイル」から `ambient-empire-xxx.json` を手動アップロードし、ノート内で以下を設定：

```python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/ambient-empire-xxx.json"
```

---

## 📂 File Overview

| Path                                          | Description                   |
| --------------------------------------------- | ----------------------------- |
| `scripts/search_bq.py`                        | 類似FAQ検索（BigQuery × cosine類似度） |
| `scripts/prompt_gen.py`                       | GPTへの入力用プロンプト生成               |
| `scripts/call_chatgpt.py`                     | GPT-4 API呼び出し（OpenAI SDK v1）  |
| `tests/run_pipeline_test.py`                  | 上記を一括実行するRAGパイプライン            |
| `notebooks/SmartFreeGov_RAG_demo_fixed.ipynb` | Colab GUI体験版                  |

---

## 📊 Dataset

* 📁 `data/faq_sample_with_embedding.csv` に収録
* 項目：`id`, `category`, `question`, `answer`, `embedding`
* 埋め込み：MiniLMによる384次元ベクトル

---

## ✅ Output Example

```
🔍 Top 3 FAQs for: "パスワードを変更したい"

Q1: マイナンバーカードの更新は必要？
A1: 電子証明書の有効期限（5年）ごとに更新が必要です。

Q2: 転出届はいつまでに？
A2: 引越しの14日前から当日までに提出。

Q3: アカウントロックされたら？
A3: 窓口で本人確認の上、再発行可能です。

🧠 Answer:
パスワードはアカウント設定画面から変更可能です。
```

---

## 📈 KPI可視化（Looker Studio連携）

FAQログの実行経路を BigQuery に記録し、Looker Studio で KPI を可視化しています：

🔗 [SmartFreeGov Looker Dashboard](https://lookerstudio.google.com/reporting/ba4d7d42-d1af-492f-8c6d-36bad9eb490c)

* 詳細は [`dashboards/kpi_design.md`](dashboards/kpi_design.md)

---

## 🔭 Motivation

* RAG（検索＋生成）の信頼性ある行政適用PoC
* GPTの出力に根拠を持たせ、暴走を抑止
* GCP × LLM × 公共ユースケースの実証設計

---

## 🔮 Future Enhancements

* ✅ Looker StudioでFAQログ可視化
* ✅ CLI → Colab化（GUI体験）
* ↻ PDF / 音声入力 / 多言語対応
* 🔐 セキュアなAPIキー管理（Vault連携など）

---

## 👨‍💻 Author

Developed by **REICHIYAN**, as a SmartGov + GenAI PoC project.
Feel free to fork, extend, or integrate.

---
