from fastapi import FastAPI
from app.router import router as chat_router
from app.ingest import router as ingest_router
from app.retrieve import router as retrieve_router

app = FastAPI(title="Strategia AOL Backend")

app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(ingest_router, prefix="/ingest", tags=["ingest"])
app.include_router(retrieve_router, prefix="/retrieve", tags=["retrieve"])

@app.get("/health")
def health():
    return {"status": "ok"}
