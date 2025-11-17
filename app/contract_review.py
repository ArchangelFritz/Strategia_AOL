# app/contract_review.py

from fastapi import APIRouter, HTTPException
from app.storage.full_docs import full_doc_store
from app.contract_agent import analyze_contract

router = APIRouter()

@router.get("/{filename}")
async def review_contract(filename: str):
    # Step 1: Retrieve full text
    full_text = full_doc_store.get_document(filename)

    if not full_text:
        raise HTTPException(
            status_code=404,
            detail=f"Document '{filename}' not found in full document index."
        )

    # Step 2: Run contract review LLM workflow
    analysis = analyze_contract(filename, full_text)

    # Step 3: Return structured packet
    return {
        "filename": filename,
        "analysis": analysis,
        "raw_text": full_text
    }
