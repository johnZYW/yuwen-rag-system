# Yuwen RAG System

Cleaned public prototype of a retrieval-augmented generation workflow prepared for portfolio and ByteDance AI Full-Stack Challenge review.

This repository demonstrates the core RAG pipeline without exposing private source documents, generated embedding caches, API keys, logs, or internal working files.

## What this repository demonstrates

- Document / article decomposition into retrievable units
- Query representation and semantic-style retrieval
- Context assembly from top-ranked passages
- Answer generation from retrieved evidence
- A public, synthetic sample corpus for safe demonstration

## Why this matters

This project was an early technical foundation for my later Jarvis personal AI assistant work. It helped me understand how long documents can be decomposed, indexed, retrieved, and reassembled into useful context for LLM-based applications.

## Repository layout

```text
README.md
rag_demo.py
requirements.txt
sample_data/
  combined_articles.json
.env.example
.gitignore
SECURITY.md
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python rag_demo.py "How does Jarvis use confirmation before changing user data?"
```

The public demo uses a lightweight TF-IDF retriever so it can run without external API keys. The original private working version also explored LLM/embedding-based retrieval and answer generation.

## Public-data note

The original working article folders, embedding caches, logs, spreadsheets, raw datasets, and internal/private materials were removed before publication. This repository contains only code and synthetic sample data.

## Repository cleaning

Before publication, the following were removed:

- API keys and credential folders
- Generated embedding caches
- Article processing logs
- Raw article folders and internal datasets
- Spreadsheets and private working documents
- macOS metadata and generated caches
