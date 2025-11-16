from openai import OpenAI
from app.retrieve import retrieve
from app.router import route_query
from app.utils.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def answer_query(query: str):
    # pick which corpus/index to pull from
    corpus = route_query(query)

    # do multi-tier retrieval
    chunks = retrieve(query, corpus)

    # join context
    context = "\n\n----\n\n".join(chunks)

    prompt = f"""
    Use the context ONLY to answer the question.

    CONTEXT:
    {context}

    QUESTION:
    {query}

    Provide answer and cite sources from the provided context.
    """

    resp = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )

    return {
        "answer": resp.output_text,
        "sources": chunks
    }
