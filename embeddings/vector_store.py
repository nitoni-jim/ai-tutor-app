# vector_store.py
# Simple vector store using numpy for similarity search

import numpy as np
import json
import os

def save_vectors(embeddings, texts, path="./data/metadata/vector_store"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    np.save(path + ".npy", np.array(embeddings))
    with open(path + "_texts.json", "w", encoding="utf-8") as f:
        json.dump(texts, f, indent=2)

def load_vectors(path="./data/metadata/vector_store"):
    vectors = np.load(path + ".npy")
    with open(path + "_texts.json", "r", encoding="utf-8") as f:
        texts = json.load(f)
    return vectors, texts

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
