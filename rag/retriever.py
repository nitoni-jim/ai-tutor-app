"""
RAG Retriever

Implements:
- Cosine similarity retrieval
- Top-k nearest neighbor search
- Vector ranking for semantic question similarity

Forms the retrieval stage of the RAG pipeline.
"""


# retriever.py
import numpy as np
from vector_store import cosine_similarity

class Retriever:
    def __init__(self, vectors, texts):
        self.vectors = vectors
        self.texts = texts

    def retrieve(self, query_vec, top_k=5):
        similarities = np.array([cosine_similarity(query_vec, v) for v in self.vectors])
        idxs = similarities.argsort()[::-1][:top_k]
        return [(self.texts[i], similarities[i]) for i in idxs]
