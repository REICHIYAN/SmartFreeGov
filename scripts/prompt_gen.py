# scripts/prompt_gen.py

import json
from typing import List, Dict

def load_top_k_faqs(file_path: str) -> List[Dict]:
    """Top-K FAQリスト（JSON）を読み込む"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def build_prompt(user_query: str, top_k_faqs: List[Dict]) -> str:
    """ユーザー質問と類似FAQからプロンプトを構築（ChatGPT向け最適化）"""
    prompt = (
        "あなたはFAQに詳しい市役所のAI案内係です。\n"
        "以下は過去の類似質問とその回答です。参考にして、できるだけ簡潔に質問に答えてください。\n\n"
        "<FAQ>\n"
    )
    for i, faq in enumerate(top_k_faqs, 1):
        prompt += f"Q{i}: {faq['question']}\nA{i}: {faq['answer']}\n\n"
    prompt += "</FAQ>\n\n"
    prompt += f"Q: {user_query}\nA:"
    return prompt

def main():
    # 例: 類似FAQ結果を保存したJSONファイル（Top-K形式）
    top_k_path = "data/top_k_result.json"
    user_query = "引越しした場合の住民票の手続きは？"

    top_k_faqs = load_top_k_faqs(top_k_path)
    final_prompt = build_prompt(user_query, top_k_faqs)

    print("===== Prompt =====")
    print(final_prompt)

if __name__ == "__main__":
    main()
