# scripts/call_chatgpt.py

import os
from openai import OpenAI
from dotenv import load_dotenv

def call_chatgpt(prompt: str) -> str:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in the environment.")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "あなたは行政FAQのアシスタントです。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    with open("data/generated_prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()
    print(call_chatgpt(prompt))

