from fastapi import APIRouter, UploadFile, HTTPException
from app.utils.azure_ocr import extract_text_from_document
from app.utils.chunking import chunk_text
from app.utils.embed import embed_text
from app.storage.vector_store import vector_db
from app.utils.classifier import classify_query


router = APIRouter()



@router.post("/file")
async def ingest_file(
    file: UploadFile,
    department: str | None = None   # Allow overrid
):

    if not file.filename:
        raise HTTPException(400, "No file provided")
    
    # If department is provided manually via UI, use it
    if department:
        corpus = department
    # Otherwise classify based on filename, notes, or default rules
    else:
        # classification based on filename
        corpus = classify_query(file.filename)
    
    bytes_data = await file.read()

    text = extract_text_from_document(bytes_data)
    chunks = chunk_text(text)
    embeddings = embed_text(chunks)

    vector_db.add_texts(collection=corpus, texts=chunks, embeddings=embeddings)

    return {"status": "ok", "chunks": len(chunks)}
    

    

