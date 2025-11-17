from fastapi import FastAPI
from app.router import router as chat_router
from app.ingest import router as ingest_router
from app.retrieve import router as retrieve_router
from app.contract_review import router as contract_router
from app.contract_review import router as contract_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Strategia AOL Backend")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TEMPORARY for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(contract_router, prefix="/contract-review", tags=["contracts"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(ingest_router, prefix="/ingest", tags=["ingest"])
app.include_router(retrieve_router, prefix="/retrieve", tags=["retrieve"])
app.include_router(contract_router, prefix="/contract-review", tags=["contracts"])

@app.get("/health")
def health():
    return {"status": "ok"}
