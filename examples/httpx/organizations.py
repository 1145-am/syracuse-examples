"""Organization search examples (httpx).

Look up company news by organization name using the dedicated
/api/v1/stories/organization/ endpoint or the org_name filter on /stories/.

Usage: uv run python examples/httpx/organizations.py
"""

import os

import httpx
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://syracuse.1145.am"
API_KEY = os.environ["SYRACUSE_API_KEY"]
HEADERS = {"Authorization": f"Token {API_KEY}"}


def search_organization(name: str = "Microsoft"):
    """Search for stories about a specific organization."""
    print(f"=== Stories about '{name}' ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/organization/",
        headers=HEADERS,
        params={"org_name": name},
        timeout=120.0,
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
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"org_name": name, "days_ago": 30},
        timeout=120.0,
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
