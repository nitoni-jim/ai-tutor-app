# pipeline.py
from retriever import Retriever
from generator import generate_explanation

class RAGPipeline:
    def __init__(self, retriever):
        self.retriever = retriever

    def answer(self, query_vec):
        docs = self.retriever.retrieve(query_vec)
        return generate_explanation("", docs)

if __name__ == "__main__":
    print("RAG pipeline placeholder loaded.")
