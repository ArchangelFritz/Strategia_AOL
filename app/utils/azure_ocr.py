import time
import requests
from app.utils.config import settings

def extract_text_from_document(file_bytes: bytes) -> str:
    endpoint = settings.AZURE_OCR_ENDPOINT
    key = settings.AZURE_OCR_KEY

    url = f"{endpoint}/formrecognizer/documentModels/prebuilt-document:analyze?api-version=2023-07-31"

    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/pdf"
    }

    response = requests.post(url, headers=headers, data=file_bytes)

    if response.status_code != 202:
        raise Exception(f"OCR failed: {response.text}")

    op_location = response.headers["operation-location"]

    # Poll
    while True:
        result = requests.get(op_location, headers={"Ocp-Apim-Subscription-Key": key}).json()
        if result["status"] == "succeeded":
            return "\n".join([c["content"] for c in result["analyzeResult"]["content"]])
        if result["status"] == "failed":
            raise RuntimeError("OCR failed")
        time.sleep(1)
