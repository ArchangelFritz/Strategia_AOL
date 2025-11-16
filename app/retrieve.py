from sentence_transformers import CrossEncoder
from app.utils.embed import embed_text
from app.utils.bm25 import BM25Index
from app.storage.vector_store import vector_db

# cross-encoder reranker
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def retrieve(query: str, corpus: str, top_k: int = 5):

    # --- Tier 1: BM25 lexical search ---
    bm25 = BM25Index(corpus)
    bm25_results = bm25.search(query, top_k=15)

    # --- Tier 2: Dense vector ANN search ---
    embedding = embed_text([query])[0]
    dense_results = vector_db.search(
        collection=corpus,
        query_embedding=embedding,
        top_k=15
    )

    # merge + dedupe
    candidates = list({doc for doc in bm25_results + dense_results})

    # --- Tier 3: Cross-encoder reranker ---
    pairs = [(query, doc) for doc in candidates]
    scores = reranker.predict(pairs)
    ranked = sorted(
        zip(candidates, scores),
        key=lambda x: x[1],
        reverse=True
    )

    top_docs = [doc for doc, _ in ranked[:top_k]]
    return top_docs
