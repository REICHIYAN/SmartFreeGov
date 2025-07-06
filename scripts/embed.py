from sentence_transformers import SentenceTransformer
import pandas as pd
import json
from pathlib import Path

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
df = pd.read_csv('data/faq_sample.csv', encoding='utf-8-sig')
embeddings = model.encode(df['question'].tolist(), convert_to_tensor=False)

output = []
for i, row in df.iterrows():
    output.append({
        "id": row["id"],
        "category": row["category"],
        "question": row["question"],
        "answer": row["answer"],
        "embedding": embeddings[i].tolist()
    })

Path("data/embedding_cache.json").write_text(json.dumps(output, ensure_ascii=False, indent=2))
print("✅ Embedding saved to data/embedding_cache.json")
