# scripts/search_bq.py
from google.cloud import bigquery
from dotenv import load_dotenv
import numpy as np
import os
import ast

load_dotenv()
project_id = os.getenv("BQ_PROJECT_ID")
dataset_id = os.getenv("BQ_DATASET_ID")
table_id = os.getenv("BQ_TABLE_NAME")
full_table = f"{project_id}.{dataset_id}.{table_id}"

# 疑似入力ベクトル
user_query = "パスワードを変更したい"
user_embedding = np.random.rand(384)

def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return float(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))

# BigQueryから全ベクトルを取得
client = bigquery.Client(project=project_id)
query = f"SELECT question, answer, embedding FROM `{full_table}`"
rows = client.query(query).result()

# 類似度計算
results = []
for row in rows:
    emb = row["embedding"]
    if isinstance(emb, str):
        emb = ast.literal_eval(emb)
    score = cosine_similarity(user_embedding, emb)
    results.append((score, row["question"], row["answer"]))

# 上位表示
results.sort(reverse=True)
print(f"\n🔍 Top 3 FAQs for: \"{user_query}\"")
for score, q, a in results[:3]:
    print(f"\n🔹 類似度: {score:.4f}")
    print(f"Q: {q}")
    print(f"A: {a}")

# 外部スクリプトから使えるようにエクスポート
top_3 = results[:3]
