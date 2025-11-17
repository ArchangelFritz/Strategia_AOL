from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from app.utils.config import settings
import time

def extract_text_from_document(file_bytes: bytes) -> str:
    endpoint = settings.DOC_INTEL_ENDPOINT
    key = settings.DOC_INTEL_KEY

    client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    # Start the job (async)
    poller = client.begin_analyze_document(
        "prebuilt-read",
        document=file_bytes
    )

    # Poll until complete (Azure recommended way)
    result = poller.result()

    # Extract text
    all_text = []
    for page in result.pages:
        for line in page.lines:
            all_text.append(line.content)

    return "\n".join(all_text)
