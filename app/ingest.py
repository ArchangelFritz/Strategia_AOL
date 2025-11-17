from fastapi import APIRouter, UploadFile, HTTPException
from app.utils.azure_ocr import extract_text_from_document
from app.utils.chunking import chunk_text
from app.utils.embed import embed_text
from app.storage.vector_store import vector_db
from app.utils.classifier import classify_query
from app.storage.full_docs import full_doc_store
from fastapi.background import BackgroundTasks

router = APIRouter()

def process_document(corpus,filename, bytes_data):
    text = extract_text_from_document(bytes_data)
    full_doc_store.upsert_document(filename, text)
    chunks = chunk_text(text)
    embeddings = embed_text(chunks)

    vector_db.add_texts(collection=corpus, texts=chunks, embeddings=embeddings)


@router.post("/file")
async def ingest_file(
    file: UploadFile,
    background_tasks: BackgroundTasks,
    department: str | None = None
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
#     @router.post("/file")
# async def ingest_file(file: UploadFile, background_tasks: BackgroundTasks):
#     bytes_data = await file.read()

#     background_tasks.add_task(process_document, file.filename, bytes_data)

#     return {"status": "processing", "filename": file.filename}
    bytes_data = await file.read()
    background_tasks.add_task(process_document, corpus,file.filename, bytes_data)



    return {"status": "ok"}
    

    

