import sys
import os
import time

# scripts ディレクトリをパスに追加（CLI/Colab両対応）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.search_bq import user_query, top_3
from scripts.prompt_gen import build_prompt
from scripts.call_chatgpt import call_chatgpt
from scripts.logging_bq import log_to_bq

# ========== ユーザー入力 ==========
# Colab連携のため、手動入力ではなく変数化
query_text = user_query  # 例："パスワードを変更したい"

# ========== 類似FAQ検索（Top-3） ==========
top_k_faqs = [{"question": q, "answer": a} for _, q, a in top_3]

# ========== プロンプト生成 ==========
prompt = build_prompt(query_text, top_k_faqs)

print("\n===== PROMPT =====")
print(prompt)

# ========== GPT応答生成 ==========
print("\n===== ANSWER =====")
start_time = time.time()
try:
    answer = call_chatgpt(prompt)
    print(answer)
except Exception as e:
    print("❌ GPT応答生成に失敗:", e)
    answer = None
end_time = time.time()

# ========== BigQuery ログ保存 ==========
try:
    if answer:
        log_to_bq(
            query_text=query_text,
            top_match_question=top_k_faqs[0]["question"] if top_k_faqs else "N/A",
            is_resolved=True,
            response_time_ms=int((end_time - start_time) * 1000),
            source="CLI"
        )
        print("✅ ログ書き込み完了")
except Exception as e:
    print("❌ BigQueryログ書き込み失敗:", e)
