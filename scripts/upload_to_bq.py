from google.cloud import bigquery
import pandas as pd
import os
from dotenv import load_dotenv

# .env 読み込み
load_dotenv()

# 環境変数の取得
project_id = os.getenv("BQ_PROJECT_ID")
dataset_id = os.getenv("BQ_DATASET_ID")
table_name = os.getenv("BQ_TABLE_NAME")

# テーブルID組み立て
table_id = f"{project_id}.{dataset_id}.{table_name}"

# BigQueryクライアント初期化
client = bigquery.Client(project=project_id)

try:
    # CSVファイル読み込み
    df = pd.read_csv("data/faq_sample.csv")
    
    # DataFrame → BigQuery
    job = client.load_table_from_dataframe(df, table_id)
    job.result()

    print("✅ Uploaded to BigQuery:", table_id)

except Exception as e:
    print("❌ Upload failed:", e)
