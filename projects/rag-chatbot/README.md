# RAG Chatbot — Starter Project (Phase 3)

A minimal Retrieval-Augmented Generation chatbot over local PDFs using:
- **Qdrant** (vector DB — see root `docker-compose.yml`)
- **Ollama** for embeddings + LLM (no paid API key needed)
- **LlamaIndex** for ingestion + retrieval

## Prerequisites

1. Start the data stack from the repo root:
   ```bash
   docker compose up -d qdrant ollama
   docker exec -it ollama ollama pull nomic-embed-text   # embedding model
   docker exec -it ollama ollama pull qwen2.5:7b         # chat model
   ```
2. Create a venv and install deps:
   ```bash
   python -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   ```

## Run

```bash
# 1. Put PDFs in ./data/
# 2. Index them (one-time, re-run when docs change)
python ingest.py

# 3. Chat
python chat.py
```

## What you'll learn

- Chunking + embedding + indexing pipeline
- Cosine similarity retrieval (top-k)
- Prompt assembly with retrieved context
- Source citation
- Where to extend: reranking, hybrid search, GraphRAG, agentic RAG

## Extensions (try these next)

- [ ] Add Cohere/BGE reranking after retrieval
- [ ] Add BM25 hybrid search (rank_bm25)
- [ ] Switch to GraphRAG for entity-heavy docs
- [ ] Add evals with RAGAS
- [ ] Add prompt caching for the system prompt
