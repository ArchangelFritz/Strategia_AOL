from openai import OpenAI
from app.utils.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def embed_text(texts: list[str], semantic: bool = False):
    model = "text-embedding-3-large" if semantic else "text-embedding-3-small"

    resp = client.embeddings.create(
        model=model,
        input=texts
    )
    return [r.embedding for r in resp.data]
