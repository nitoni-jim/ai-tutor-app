🚀 AI Tutor App — Intelligent Tutoring System for WAEC / NECO / JAMB

A research-driven project applying Machine Learning, NLP, Embeddings, and RAG for automated exam preparation.












🌟 Overview

AI Tutor App is an intelligent tutoring system designed for learners preparing for WAEC, NECO, and JAMB examinations in Nigeria.

This project integrates:

Natural Language Processing (NLP)

Machine Learning (ML)

Vector-based Semantic Search

Retrieval-Augmented Generation (RAG)

The system performs:

Automated text cleaning & math normalization

Embedding generation

Vector store indexing

Semantic retrieval

LLM-style explanation templates (with future LLM integration)

The work is part of my MSCS application portfolio for UCSD and Arizona State University (ASU).

📂 Repository Structure
ai-tutor-app/
│
├── preprocessing/              # Text & math normalization
│   ├── text_cleaning.py
│   └── math_cleaning.py
│
├── embeddings/                 # Embeddings & vector store
│   ├── generate_embeddings.py
│   └── vector_store.py
│
├── rag/                        # Retrieval + generation modules
│   ├── retriever.py
│   ├── generator.py
│   └── pipeline.py
│
├── evaluation/                 # Metrics for retrieval
│   └── metrics.py
│
├── notebooks/
│   └── experiments_full.ipynb  # Full pipeline notebook
│
├── data/
│   └── metadata/               # Stored embeddings & text lookup
│
├── run_demo.py                 # Minimal CLI demonstration
└── requirements.txt            # Project dependencies

🧩 System Architecture
flowchart TD
    A[Raw Exam Questions<br>WAEC / NECO / JAMB] --> B[Preprocessing<br>Text + Math Cleaning]
    B --> C[Embeddings<br>MiniLM / Fallback]
    C --> D[Vector Store<br>.npy + JSON]
    D --> E[Retriever<br>Cosine Similarity]
    E --> F[Generator<br>Placeholder RAG]
    F --> G[Explanations<br>Future LLM Integration]

🧠 Core Features
🔹 1. Text Cleaning & Normalization

Handles:

Unicode inconsistencies

Stopword cleanup

Whitespace normalization

Math symbol correction (× → *, ÷ → /)

Math-aware normalization

🔹 2. Embedding Generation

Uses:

sentence-transformers/all-MiniLM-L6-v2 (if installed)

Deterministic fallback embeddings (ensures reproducibility & notebook execution)

Embeddings are stored as:

vector_store.npy
vector_store_texts.json

🔹 3. Semantic Retrieval

Implements cosine-similarity–based retrieval:

retriever.retrieve(query_vector, top_k=3)


Used to fetch semantically similar WAEC/NECO/JAMB exam questions.

🔹 4. Retrieval-Augmented Explanation (Prototype)

The generator:

Retrieves relevant context

Formats a structured explanation template

Prepares for future LLM integration (OpenAI / HuggingFace models)

🔹 5. Evaluation Framework

Includes:

Recall@k

MRR (Mean Reciprocal Rank)

Basic classification metrics

🧪 Experiments Notebook

Full demonstration notebook:
notebooks/experiments_full.ipynb

This notebook contains:

Cleaning pipeline

Embedding generation

Vector indexing

Retrieval demo

Explanation template generation

Evaluation examples

Designed for academic review and ML reproducibility.

🧭 Roadmap
Phase 1 — Data Expansion

Collect more WAEC/NECO/JAMB questions

Difficulty annotation

Topic classification (syllabus mapping)

Phase 2 — ML Improvements

FAISS vector index

Higher-quality embeddings (bge-large, E5-large)

Fine-tuned topic classifier

Phase 3 — Full RAG System

Structured reasoning

Multi-step explanation generator

Math derivation support

Phase 4 — Mobile App

Android app integration

Personalized learning analytics

Offline-first capabilities

📘 Research Questions

How do NLP embeddings handle mixed-format math + text exam questions?

Which embedding models best capture curriculum-level semantic similarity?

What RAG architecture is most effective for educational explanations?

How can AI improve equitable access to learning in Africa?

🧾 Citation
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
