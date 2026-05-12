"""Lightweight public RAG demo.

This file intentionally avoids external API calls so the public repository can run
without API keys. It demonstrates the same high-level retrieval flow used in a
larger private prototype: load documents, rank relevant passages, assemble
context, and produce a simple evidence-grounded response.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATA_PATH = Path("sample_data/combined_articles.json")


def load_documents(path: Path = DATA_PATH) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing sample corpus: {path}")
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("Sample corpus must be a list of document objects.")
    return data


def retrieve(query: str, documents: list[dict[str, Any]], top_k: int = 3) -> list[dict[str, Any]]:
    corpus = [f"{doc.get('title', '')}\n{doc.get('text', '')}" for doc in documents]
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(corpus + [query])
    scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()

    ranked = sorted(enumerate(scores), key=lambda item: item[1], reverse=True)[:top_k]
    results: list[dict[str, Any]] = []
    for idx, score in ranked:
        doc = dict(documents[idx])
        doc["score"] = round(float(score), 4)
        results.append(doc)
    return results


def answer(query: str, results: list[dict[str, Any]]) -> str:
    lines = [f"Query: {query}", "", "Top retrieved context:"]
    for i, doc in enumerate(results, start=1):
        lines.append(f"{i}. {doc['title']} (score={doc['score']})")
        lines.append(f"   {doc['text']}")

    lines.extend(
        [
            "",
            "Demo answer:",
            "Based on the retrieved context, the system first identifies relevant knowledge units, ",
            "then assembles them into a grounded response. In the full private workflow, this ",
            "retrieved context can be passed to an LLM for final synthesis.",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    query = " ".join(sys.argv[1:]) or "How does Jarvis use confirmation before changing user data?"
    documents = load_documents()
    results = retrieve(query, documents)
    print(answer(query, results))


if __name__ == "__main__":
    main()
