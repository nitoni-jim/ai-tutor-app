# generate_embeddings.py
# Generate and store semantic embeddings using sentence-transformers

from sentence_transformers import SentenceTransformer
import json
import os

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

def load_model(model_name=MODEL_NAME):
    """
    Load the embedding model.
    """
    return SentenceTransformer(model_name)

def embed_texts(texts, model):
    """
    Generate embeddings for a list of texts.
    """
    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings

def save_embeddings(texts, embeddings, out_path="./data/metadata/embeddings.json"):
    """
    Save texts and embeddings to a JSON file.
    """
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    data = {
        "texts": texts,
        "embeddings": [e.tolist() for e in embeddings]
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    sample = [
        "Solve for x: 2x + 5 = 11",
        "Find the LCM of 12 and 18."
    ]
    model = load_model()
    embs = embed_texts(sample, model)
    save_embeddings(sample, embs)
    print("Embeddings generated and saved.")
