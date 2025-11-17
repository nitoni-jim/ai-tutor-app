🚀 AI Tutor App — Intelligent Tutoring System for WAEC / NECO / JAMB

A research-driven project applying Machine Learning, NLP, and RAG for automated exam preparation.








🌟 Overview

AI Tutor App is an intelligent tutoring system designed to support candidates preparing for WAEC, NECO, and JAMB examinations in Nigeria.
This project integrates:

Natural Language Processing (NLP)

Machine Learning (ML)

Semantic Search using Embeddings

Retrieval-Augmented Generation (RAG)

The system performs:

Automated question cleaning & normalization

Semantic embedding of questions

Vector-based retrieval of similar items

LLM-style explanation generation (placeholder for now)

Clear modular structure for future deep learning extension

This repository accompanies my graduate applications to UCSD and Arizona State University (ASU) and demonstrates applied AI engineering and research readiness.

📂 Repository Structure
ai-tutor-app/
│
├── preprocessing/          # Text cleaning & math normalization modules
│   ├── text_cleaning.py
│   └── math_cleaning.py
│
├── embeddings/             # Embedding creation & vector store
│   ├── generate_embeddings.py
│   ├── vector_store.py
│
├── rag/                    # Retrieval and generation pipeline
│   ├── retriever.py
│   ├── generator.py
│   └── pipeline.py         # (future full RAG pipeline)
│
├── evaluation/             # Metrics for retrieval/classification
│   └── metrics.py
│
├── notebooks/
│   └── experiments_full.ipynb   # Full cleaning → embedding → retrieval → generation notebook
│
├── data/
│   └── metadata/           # Saved embeddings, vector store, lookup files
│
├── run_demo.py             # Minimal CLI demo pipeline
└── requirements.txt        # Dependencies

## 🧩 System Architecture

```mermaid
flowchart TD
    A[Raw Exam Questions<br>WAEC / NECO / JAMB] --> B[Preprocessing<br>Text + Math Cleaning]
    B --> C[Embeddings<br>MiniLM / Fallback]
    C --> D[Vector Store<br>.npy + JSON]
    D --> E[Retriever<br>Cosine Similarity]
    E --> F[Generator<br>Placeholder RAG]
    F --> G[Explanations<br>Future LLM Integration]

🧠 Core Features
🔹 1. Question Cleaning & Normalization

Handles:

Unicode inconsistencies

Excess whitespace

Mathematical symbol normalization (× → *, ÷ → /)

Removal of control characters

This ensures consistent text before embedding.

🔹 2. Embedding Generation

Uses:

sentence-transformers/all-MiniLM-L6-v2 (if available)

Otherwise a deterministic fallback for reproducibility

Embeddings are stored in:

data/metadata/vector_store.npy
data/metadata/vector_store_texts.json

🔹 3. Semantic Retrieval

Implements cosine-similarity retrieval:

retriever.retrieve(query_vector, top_k=3)


Used to find semantically similar exam questions.

🔹 4. Placeholder RAG Generation

Combines retrieved context into a structured template.

In the future this will be replaced by an actual LLM API integration (OpenAI, HuggingFace, Phi, etc.)

🔹 5. Evaluation Tools

Includes:

Recall@k

MRR (Mean Reciprocal Rank)

Basic classification metrics

All in evaluation/metrics.py.

🧪 Experiments Notebook

The notebook:

notebooks/experiments_full.ipynb


Contains:

Data cleaning steps

Embedding generation

Vector indexing

Retrieval demonstration

Explanation generation

Evaluation examples

This notebook is designed for academic review and ML reproducibility.

📘 Research Questions

How can we best normalize mixed-format questions (math + text) for NLP models?

Can embeddings detect curriculum-equivalent WAEC/NECO/JAMB items?

How effective is a RAG pipeline in explaining exam questions?

Can lightweight models help under-resourced students learn more effectively?

🧭 Future Roadmap
🔜 Phase 1: Data Expansion

Bulk ingestion of WAEC/NECO past questions

Automated difficulty labeling

Topic tag prediction (syllabus mapping)

🔜 Phase 2: Model Improvement

FAISS vector index

Better embedding models (e.g., bge-large)

Classification model for question topics

🔜 Phase 3: Full RAG System

Fine-tuned model for exam solutions

Multi-step reasoning

Structured explanations (steps, diagrams)

🔜 Phase 4: Mobile App Integration

Android app (Java / Kotlin)

Student performance analytics

Offline-first learning

🧾 Citation

If referencing this work:

@misc{jimogbolo2025aitutor,
  title={AI-Tutor-App: An Intelligent Tutoring System for WAEC/NECO/JAMB Exams},
  author={Nitoni Jim-Ogbolo},
  year={2025},
  url={https://github.com/nitoni-jim/ai-tutor-app}
}

📬 Contact

Nitoni Jim-Ogbolo
AI Developer & Research Enthusiast
Email: nitoni4fj@gmail.com
