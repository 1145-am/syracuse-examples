"""Industry cluster examples (httpx).

Browse and search industry classifications, then filter stories by industry.

Industry clusters have a hierarchical structure with topic_id identifiers
and representative_doc names (e.g. ["Appliance Services", "Appliance Care"]).

Usage: uv run python -m examples.httpx.industries
"""

import httpx

from examples.config import BASE_URL, HEADERS, print_stories


def list_industry_clusters():
    """List available industry clusters."""
    print("=== Industry clusters ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/industry-clusters/",
        headers=HEADERS,
        timeout=120.0,
    )
    response.raise_for_status()
    data = response.json()

    print(f"Found {data['count']} industry clusters\n")
    for cluster in data["results"][:10]:
        names = ", ".join(cluster["representative_doc"][:3])
        print(f"  [topic_id={cluster['topic_id']}] {names}")
    print()


def search_industries(query: str = "technology"):
    """Search for industry clusters by keyword."""
    print(f"=== Searching industries for '{query}' ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/industry-clusters/",
        headers=HEADERS,
        params={"search": query},
        timeout=120.0,
    )
    response.raise_for_status()
    data = response.json()

    print(f"Found {data['count']} matching clusters\n")
    for cluster in data["results"][:10]:
        names = ", ".join(cluster["representative_doc"][:3])
        print(f"  [topic_id={cluster['topic_id']}] {names}")
    print()


def stories_by_industry(industry: str = "Technology"):
    """Filter stories by industry name."""
    print(f"=== Stories in '{industry}' industry ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"industry": industry, "days_ago": 30},
        timeout=120.0,
    )
    response.raise_for_status()
    data = response.json()

    print_stories(data)


def stories_by_industry_and_location():
    """Use the /stories/industry-location/ endpoint for combined filtering."""
    print("=== Technology stories in US ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/industry-location/",
        headers=HEADERS,
        params={"industry": "Technology", "location": "US"},
        timeout=120.0,
    )
    response.raise_for_status()
    data = response.json()

    print_stories(data)


if __name__ == "__main__":
    list_industry_clusters()
    search_industries()
    stories_by_industry()
    stories_by_industry_and_location()
