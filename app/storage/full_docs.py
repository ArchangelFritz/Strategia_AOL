# app/storage/full_docs.py

import chromadb

client = chromadb.Client()

class FullDocumentStore:
    def __init__(self):
        self.collection = client.get_or_create_collection("full_documents")

    def upsert_document(self, filename: str, text: str):
        self.collection.upsert(
            documents=[text],
            ids=[filename],
            metadatas=[{"filename": filename}]
        )

    def get_document(self, filename: str):
        res = self.collection.get(ids=[filename])
        if not res["documents"]:
            return None
        return res["documents"][0]

    def list_documents(self):
        return self.collection.get()["ids"]

full_doc_store = FullDocumentStore()
