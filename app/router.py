from fastapi import APIRouter
from pydantic import BaseModel
from app.llm_answer import answer_query

router = APIRouter()

class Query(BaseModel):
    query: str

@router.post("/")
async def route_query(query: Query):
    # Determine corpus
    q = query.query.lower()

    if any(w in q for w in ["claim", "payer", "contract", "mco", "reimbursement"]):
        corpus = "finance"

    elif any(w in q for w in ["vacation", "benefits", "hr", "policy", "recruiting"]):
        corpus = "hr"

    else:
        corpus = "general"

    result = answer_query(query.query, corpus)
    return {"corpus": corpus, "answer": result}
