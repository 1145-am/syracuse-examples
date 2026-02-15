"""Organization search examples (requests).

Look up company news by organization name using the dedicated
/api/v1/stories/organization/ endpoint or the org_name filter on /stories/.

Usage: uv run python examples/requests/organizations.py
"""

import requests

from examples.config import BASE_URL, HEADERS


def search_organization(name: str = "Microsoft"):
    """Search for stories about a specific organization."""
    print(f"=== Stories about '{name}' ===\n")
    response = requests.get(
        f"{BASE_URL}/api/v1/stories/organization/",
        headers=HEADERS,
        params={"org_name": name},
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()

    print(f"Found {data['count']} stories\n")
    for story in data["results"][:5]:
        print(f"  [{story['activity_class']}] {story['headline']}")
        print(f"  Published: {story['date_published']}")
        print()


def search_via_main_endpoint(name: str = "Apple"):
    """You can also use the org_name param on the main /stories/ endpoint."""
    print(f"=== Stories mentioning '{name}' via /stories/ ===\n")
    response = requests.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"org_name": name, "days_ago": 30},
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()

    print(f"Found {data['count']} stories\n")
    for story in data["results"][:5]:
        print(f"  [{story['activity_class']}] {story['headline']}")
        print(f"  Published: {story['date_published']}")
        print()


if __name__ == "__main__":
    search_organization()
    search_via_main_endpoint()
