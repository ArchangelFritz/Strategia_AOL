from openai import OpenAI
from app.utils.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def embed_text(texts: list[str]):
    resp = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [r.embedding for r in resp.data]
