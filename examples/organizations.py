"""Organization search examples.

Look up company news by organization name using the dedicated
/api/v1/stories/organization/ endpoint or the org_name filter on /stories/.

Usage: uv run python examples/organizations.py
"""

import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://syracuse.1145.am"
API_KEY = os.environ["SYRACUSE_API_KEY"]
HEADERS = {"Authorization": f"Token {API_KEY}"}


def search_organization_httpx(name: str = "Microsoft"):
    """Search for stories about a specific organization using httpx."""
    import httpx

    print(f"=== Stories about '{name}' — httpx ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/organization/",
        headers=HEADERS,
        params={"org_name": name},
        timeout=30.0,
    )
    response.raise_for_status()
    data = response.json()

    print(f"Found {data['count']} stories\n")
    for story in data["results"][:5]:
        print(f"  [{story['activity_class']}] {story['headline']}")
        print(f"  Published: {story['date_published']}")
        print()


def search_organization_requests(name: str = "Microsoft"):
    """Search for stories about a specific organization using requests."""
    import requests

    print(f"=== Stories about '{name}' — requests ===\n")
    response = requests.get(
        f"{BASE_URL}/api/v1/stories/organization/",
        headers=HEADERS,
        params={"org_name": name},
        timeout=30,
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
    import httpx

    print(f"=== Stories mentioning '{name}' via /stories/ ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"org_name": name, "days_ago": 30},
        timeout=30.0,
    )
    response.raise_for_status()
    data = response.json()

    print(f"Found {data['count']} stories\n")
    for story in data["results"][:5]:
        print(f"  [{story['activity_class']}] {story['headline']}")
        print(f"  Published: {story['date_published']}")
        print()


if __name__ == "__main__":
    search_organization_httpx()
    search_organization_requests()
    search_via_main_endpoint()
