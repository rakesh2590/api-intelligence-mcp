import json
from api_intelligence_mcp.services.provider_service import (
    get_all_providers,
    get_provider
)


def main():

    # Get all registered providers
    providers = get_all_providers()

    print("\n========== SUPPORTED API PROVIDERS ==========\n")

    for provider in providers:

        print(f"Provider ID   : {provider.id}")
        print(f"Provider Name : {provider.name}")
        print(f"Provider Type : {provider.provider_type}")
        print(f"Base URL      : {provider.base_url}")
        print(f"Capabilities  : {provider.capabilities}")

        print("---------------------------------------------")

    # Search for a specific provider
    print("\n========== SEARCH PROVIDER ==========\n")

    provider = get_provider("gemini")

    if provider:

        print(json.dumps(
            provider.model_dump(),
            indent=4
        ))

    else:

        print("Provider not found")


if __name__ == "__main__":
    main()