# Yuwen RAG System

A cleaned public prototype of my retrieval-augmented generation workflow. The project demonstrates document decomposition, embedding-based retrieval, semantic search, and query-to-response generation.

## What this repository demonstrates

- Document / article decomposition into retrievable units
- Query embedding and semantic similarity search
- Article and paragraph ranking
- Retrieval-augmented answer generation
- Evaluation utilities for retrieval quality exploration

## Public-data note

The original working article folders, embedding caches, logs, and internal/raw datasets were removed before publication. This public repository contains code plus a small synthetic sample dataset so the structure is visible without exposing private or potentially non-public materials.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install openai numpy scikit-learn pandas openpyxl
export OPENAI_API_KEY="your_key_here"
```

## Example

```bash
python query_to_response.py
```

You may replace `sample_data/combined_articles.json` with your own public corpus.

## Repository cleaning

Before publication, API keys, `API_key/`, generated embedding caches, article logs, raw article folders, spreadsheets, macOS metadata, and potentially sensitive working documents were removed.
