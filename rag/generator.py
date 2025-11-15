# generator.py
# Placeholder for LLM-based explanation generator

def generate_explanation(query, retrieved_docs):
    """
    This will eventually call an LLM. For now, return a placeholder answer.
    """
    context = "\n".join([doc for doc, _ in retrieved_docs])
    return f"Context:\n{context}\n\nExplanation:\n(This is a placeholder. LLM will go here.)"
