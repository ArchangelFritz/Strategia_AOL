import chromadb

client = chromadb.Client()

class VectorDB:
    def get_collection(self, name: str):
        return client.get_or_create_collection(name)

    def add_texts(self, collection: str, texts: list[str], embeddings: list[list[float]]):
        coll = self.get_collection(collection)
        ids = [f"{collection}-{i}" for i in range(len(texts))]
        coll.add(documents=texts, embeddings=embeddings, ids=ids)

    def search(self, collection: str, query_embedding: list[float], top_k: int):
        coll = self.get_collection(collection)
        result = coll.query(query_embeddings=[query_embedding], n_results=top_k)
        return result["documents"][0]

    def list_collections(self):
        return client.list_collections()

vector_db = VectorDB()
