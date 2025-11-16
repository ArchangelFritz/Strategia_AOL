# app/router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.retrieve import retrieve_passages
from app.llm_answer import llm_answer_from_contexts
from app.utils.classifier import classify_query

router = APIRouter()


# ---------------------------
# Request / Response Models
# ---------------------------

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str
    sources: list


# ---------------------------
# Main QA Endpoint
# ---------------------------

@router.post("/ask", response_model=QueryResponse)
async def ask_question(payload: QueryRequest):
    query = payload.query

    # Step 1: Route the query to correct corpus ------------------------
    try:
        corpus = classify_query(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Classifier failed: {str(e)}")

    # Step 2: Retrieve documents (BM25 + Dense + Rerank) ---------------
    try:
        top_passages = retrieve_passages(query, corpus)   # returns list of {text, score, source}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Retriever failed: {str(e)}")

    if not top_passages:
        return QueryResponse(answer="I couldn’t find relevant information.", sources=[])

    # Step 3: LLM Final Answer -----------------------------------------
    try:
        answer = llm_answer_from_contexts(query, top_passages)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM answer failed: {str(e)}")

    # Format sources for UI
    source_list = [
        {
            "source": p.get("source", "unknown"),
            "score": p.get("score", None)
        }
        for p in top_passages
    ]

    return QueryResponse(answer=answer, sources=source_list)
