from fastapi import APIRouter
from app.storage.vector_store import vector_db

router = APIRouter()

def retrieve_chunks(query_embedding, corpus: str, top_k: int = 5):
    return vector_db.search(collection=corpus, query_embedding=query_embedding, top_k=top_k)

@router.get("/")
async def debug_retrieve():
    return {"collections": vector_db.list_collections()}
