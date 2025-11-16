import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    AZURE_OCR_KEY: str = os.getenv("AZURE_OCR_KEY")
    AZURE_OCR_ENDPOINT: str = os.getenv("AZURE_OCR_ENDPOINT")

settings = Settings()
