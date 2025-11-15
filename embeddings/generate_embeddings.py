# generate_embeddings.py
# Template: generate and store sentence embeddings using sentence-transformers

from sentence_transformers import SentenceTransformer
import json
import os

MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'

def embed_texts(texts, model_name=MODEL_NAME):
    """
    Generate sentence embeddings for a list of texts.
    """
    model = SentenceTransformer(model_name)
    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings

def save_embeddings(embeddings, texts, out_path):
    """
    Save embeddings + source texts as JSON.
    """
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    data = {
        "texts": texts,
        "embeddings": [e.tolist() for e in embeddings]
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    # Example usage
    sample_texts = [
        "Solve for x: 2x + 5 = 11",
        "What is the LCM of 12 and 18?"
    ]

    embs = embed_texts(sample_texts)
    save_embeddings(embs, sample_texts, "./data/embeddings/embeddings.json")

    print("Embeddings generated and saved.")
