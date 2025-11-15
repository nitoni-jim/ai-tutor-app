AI-Tutor-App

Adaptive Intelligent Tutoring System using ML/NLP for WAEC/NECO/JAMB
Author: Nitoni Jim-Ogbolo
GitHub: https://github.com/nitoni-jim

📘 Abstract

AI-Tutor-App is a research-driven project focused on building an intelligent, adaptive tutoring system for WAEC/NECO/JAMB examinations in Nigeria. It integrates Natural Language Processing (NLP), semantic embeddings, retrieval-augmented generation (RAG), and evaluation pipelines to deliver curriculum-aware practice questions, explanations, and personalized difficulty progression.

This repository serves as a foundation for graduate-level research in NLP, low-resource education technologies, intelligent learning systems, and adaptive assessment.

🎯 Motivation

Millions of Nigerian students rely on inconsistent or inaccessible exam-prep materials. Most existing systems lack:

True semantic understanding of questions

Adaptive difficulty progression

Curriculum-driven topic classification

Explanatory feedback

Handling of messy real-world question formats (OCR text, math expressions, mixed diagrams)

This project investigates a practical, research-oriented ML/NLP approach to solving these challenges.

🏗️ System Architecture
Overall Pipeline (Mermaid Diagram)

GitHub renders Mermaid diagrams automatically.

flowchart TD
  A[Raw WAEC/NECO/JAMB Question Bank] --> B[Text Cleaning & Normalization]
  B --> C[Tokenization, Sentence Splitting, Metadata Extraction]
  C --> D[Embedding Generation (Sentence-Transformers)]
  D --> E[Vector Store (FAISS / Numpy / Custom)]
  E --> F[Retriever (Semantic Similarity Search)]
  F --> G[RAG Generator (LLM-based)]
  G --> H[Personalized Difficulty Estimation]
  H --> I[Student UI / API Response Layer]
  I --> J[Performance Logging & Feedback Metrics]
  J --> K[Evaluation & Model Improvement Loop]

🧹 1. Preprocessing Pipeline

Located in preprocessing/

Includes:

text_cleaning.py – Unicode normalization, whitespace cleanup, dash fixes

math_cleaning.py – Math expression normalization (× → *, – → -)

OCR noise reduction

Mixed-format question handling

Example:
from preprocessing.text_cleaning import clean_text
cleaned = clean_text("  Solve: 2×(3 + 4) — find the value. ")

🔍 2. Embedding + Vector Search

Located in embeddings/

Components:

generate_embeddings.py

vector_store.py

Uses sentence-transformers for semantic vector representation:

model = SentenceTransformer('all-MiniLM-L6-v2')
embs = model.encode(["Calculate the LCM of 18 and 24"])


Vector store supports:

Saving embeddings

Loading embeddings

Fast cosine similarity search

🤖 3. Retrieval-Augmented Generation (RAG)

Located in rag/

Modules:

retriever.py – nearest-neighbor semantic retrieval

generator.py – placeholder LLM-based explanation generator

pipeline.py – integrates retrieval + generation

Conceptual Flow:

Convert student question → embedding

Retrieve top-k semantically similar past exam questions

Feed retrieved context to generator

Output explanation + next-step guidance

📊 4. Evaluation Pipeline

Located in evaluation/metrics.py

Supports:

Accuracy

Precision

Recall

F1-score

Upcoming additions:

Retrieval metrics (MRR, Recall@k)

Student learning gain tracking

Difficulty progression validation

📁 Project Structure
ai-tutor-app/
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── metadata/
├── preprocessing/
│   ├── text_cleaning.py
│   └── math_cleaning.py
├── embeddings/
│   ├── generate_embeddings.py
│   └── vector_store.py
├── rag/
│   ├── retriever.py
│   ├── generator.py
│   └── pipeline.py
├── evaluation/
│   └── metrics.py
├── notebooks/
│   └── experiments.ipynb
└── README.md

🧪 Experiments

Use notebooks/experiments.ipynb to run:

Embedding comparison tests

Retrieval accuracy experiments

Early RAG prototypes

Difficulty estimation baselines

🔧 Installation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Recommended packages:
sentence-transformers
scikit-learn
numpy
pandas
faiss-cpu
jupyter

🚀 Future Research Directions

Fine-tuning LLMs for Nigerian curriculum domains

Automated difficulty grading

Topic classification using BERT / DistilBERT

Multimodal support for math diagrams and images

User modeling + adaptive learning paths

Integration with mobile learning apps

🤝 Contributions

Open for academic collaborations.
Feel free to fork, open issues, and submit pull requests.

📜 License

MIT License — free to use for research, education, and development.

🧑‍💻 Author

Nitoni Jim-Ogbolo
AI/ML Researcher • Intelligent Tutoring Systems • Applied NLP
GitHub: https://github.com/nitoni-jim
