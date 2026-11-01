import json
from pathlib import Path
from api_intelligence_mcp.models.provider_models import ProviderInfo


# Find the project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Location of provider registry
PROVIDERS_FILE = PROJECT_ROOT / "data" / "providers.json"


def load_providers() -> list[ProviderInfo]:
    """
    Load all API providers from providers.json.
    """

    with open(PROVIDERS_FILE, "r", encoding="utf-8") as file:

        provider_data = json.load(file)

    providers = []

    for provider_id, details in provider_data.items():

        provider = ProviderInfo(
            id=provider_id,
            **details
        )

        providers.append(provider)

    return providers


def get_all_providers() -> list[ProviderInfo]:
    """
    Return all registered API providers.
    """

    return load_providers()


def get_provider(provider_id: str) -> ProviderInfo | None:
    """
    Find a provider using its unique ID.
    """

    providers = load_providers()

    for provider in providers:

        if provider.id.lower() == provider_id.strip().lower():

            return provider

    return None