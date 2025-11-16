from openai import OpenAI
from app.retrieve import retrieve_chunks
from app.utils.chunking import chunk_text
from app.utils.embed import embed_text
from app.utils.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def answer_query(query: str, corpus: str):
    # Embed query
    query_embedding = embed_text([query])[0]

    # Retrieve context
    chunks = retrieve_chunks(query_embedding, corpus=corpus, top_k=5)
    context = "\n\n".join(chunks)

    prompt = f"""
    You are an enterprise AI assistant. Use the context below to answer:

    CONTEXT:
    {context}

    QUESTION:
    {query}

    If the context does not contain the answer, say you don't know.
    """

    completion = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    return completion.output_text
