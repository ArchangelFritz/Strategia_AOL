from pydantic_settings import BaseSettings
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


class Settings(BaseSettings):
    # Your Key Vault URL (replace with your actual vault URL)
    KEY_VAULT_URL: str = "https://strategia-aol-vault.vault.azure.net/"

    OPENAI_API_KEY: str | None = None
    DOC_INTEL_KEY: str | None = None
    DOC_INTEL_ENDPOINT: str | None = None

    def load_from_keyvault(self):
        # VM automatically authenticates using its system-assigned managed identity
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=self.KEY_VAULT_URL, credential=credential)

        # IMPORTANT — match EXACT secret names
        self.OPENAI_API_KEY = client.get_secret("openai-api-personal-key").value
        self.DOC_INTEL_KEY = client.get_secret("doc-intel-key").value
        self.DOC_INTEL_ENDPOINT = client.get_secret("doc-intel-endpoint").value


settings = Settings()
settings.load_from_keyvault()
