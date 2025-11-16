# Strategia AOL Backend

Python FastAPI backend for the Agent Operating Layer.
Includes ingestion, corpus routing, retrieval, reranking, and LLM answer generation.

## Run locally
uvicorn app.main:app --reload --port 8000

## Project structure
app/
  main.py         # FastAPI entrypoint
  ingest.py       # OCR + chunking + embeddings
  router.py       # Query classifier + corpus routing
  retrieve.py     # BM25 + dense + reranker
  llm_answer.py   # Final LLM response synthesis
  storage/        # Vector DB persistent storage
  utils/          # Shared helpers
requirements.txt
