# app/contract_review.py

from fastapi import APIRouter, HTTPException
from app.storage.full_docs import full_doc_store

router = APIRouter()

@router.get("/{filename}")
async def get_full_document(filename: str):
    doc = full_doc_store.get_document(filename)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found.")

    return {
        "filename": filename,
        "content": doc
    }
