from google.cloud import bigquery
from datetime import datetime
import os
from dotenv import load_dotenv

# .envから環境変数を読み込む
load_dotenv()

# 環境変数からテーブル情報を取得
project_id = os.getenv("BQ_PROJECT_ID")
dataset_id = os.getenv("BQ_DATASET_ID")
table_name = os.getenv("BQ_TABLE_NAME")
table_id = f"{project_id}.{dataset_id}.{table_name}"

def log_to_bq(query_text, top_match_question, is_resolved=True, source="Colab", response_time_ms=None):
    client = bigquery.Client(project=project_id)

    # データ行（JSON形式）
    row = {
        # "timestamp": datetime.utcnow().isoformat(),
        "query_text": query_text,
        "top_match_question": top_match_question,
        "is_resolved": is_resolved,
        "source": source,
    }
    if response_time_ms is not None:
        row["response_time_ms"] = response_time_ms

    # バッチ書き込み（load_table_from_json を使用）
    try:
        job = client.load_table_from_json([row], table_id)
        job.result()  # バッチ書き込み完了まで待機
        print("✅ BigQuery バッチ書き込み成功")
    except Exception as e:
        print("❌ BigQuery バッチ書き込み失敗:", e)
