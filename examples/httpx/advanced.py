"""Advanced usage examples (httpx).

Combining multiple filters, pagination, and other advanced patterns.

Usage: uv run python examples/httpx/advanced.py
"""

import os

import httpx
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://syracuse.1145.am"
API_KEY = os.environ["SYRACUSE_API_KEY"]
HEADERS = {"Authorization": f"Token {API_KEY}"}


def combine_filters():
    """Combine industry, location, and activity type filters."""
    print("=== Combined filters: Technology + US + PartnershipActivity ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={
            "industry": "Technology",
            "location": "US",
            "type": "PartnershipActivity",
            "days_ago": 90,
        },
        timeout=120.0,
    )
    response.raise_for_status()
    data = response.json()

    print(f"Found {data['count']} stories\n")
    for story in data["results"][:5]:
        print(f"  {story['headline']}")
        print(f"  Published: {story['date_published']}")
        print()


def paginate_results():
    """Walk through paginated results."""
    print("=== Paginating through stories ===\n")
    page = 1
    total_fetched = 0

    while page <= 3:  # Limit to 3 pages for this example
        response = httpx.get(
            f"{BASE_URL}/api/v1/stories/",
            headers=HEADERS,
            params={"industry": "Technology", "days_ago": 30, "page": page},
            timeout=120.0,
        )
        response.raise_for_status()
        data = response.json()

        results = data["results"]
        total_fetched += len(results)
        print(f"  Page {page}: {len(results)} stories (total so far: {total_fetched}/{data['count']})")

        if not data.get("next"):
            break
        page += 1

    print()


def with_and_without_similar():
    """Compare results with and without similar story grouping."""
    print("=== With combine_similar=true (default) ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"industry": "Technology", "days_ago": 7, "combine_similar": True},
        timeout=120.0,
    )
    response.raise_for_status()
    data = response.json()
    print(f"  {data['count']} stories\n")

    print("=== With combine_similar=false ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"industry": "Technology", "days_ago": 7, "combine_similar": False},
        timeout=120.0,
    )
    response.raise_for_status()
    data = response.json()
    print(f"  {data['count']} stories\n")


def multiple_industries():
    """Filter by multiple industries at once."""
    print("=== Multiple industries: Technology, Healthcare ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"industry": ["Technology", "Healthcare"], "days_ago": 30},
        timeout=120.0,
    )
    response.raise_for_status()
    data = response.json()

    print(f"Found {data['count']} stories\n")
    for story in data["results"][:5]:
        print(f"  [{story['activity_class']}] {story['headline']}")
        print()


def multiple_locations():
    """Filter by multiple locations at once."""
    print("=== Multiple locations: US, GB ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"location": ["US", "GB"], "days_ago": 30},
        timeout=120.0,
    )
    response.raise_for_status()
    data = response.json()

    print(f"Found {data['count']} stories\n")
    for story in data["results"][:5]:
        print(f"  [{story['activity_class']}] {story['headline']}")
        print()


if __name__ == "__main__":
    combine_filters()
    paginate_results()
    with_and_without_similar()
    multiple_industries()
    multiple_locations()
