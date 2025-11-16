from rank_bm25 import BM25Okapi
import json
import os

class BM25Index:
    def __init__(self, corpus_name: str):
        self.corpus_name = corpus_name
        self.index_path = f"app/storage/bm25/{corpus_name}.json"

        if os.path.exists(self.index_path):
            with open(self.index_path, "r") as f:
                data = json.load(f)
            self.docs = data["docs"]
            self.tokens = [d.split() for d in self.docs]
            self.bm25 = BM25Okapi(self.tokens)
        else:
            self.docs = []
            self.tokens = []
            self.bm25 = None

    def search(self, query: str, top_k: int = 10):
        if not self.bm25:
            return []
        scores = self.bm25.get_scores(query.split())
        ranked = sorted(zip(self.docs, scores), key=lambda x: x[1], reverse=True)
        return [doc for doc, _ in ranked[:top_k]]
