"""Stories API examples (httpx).

The /api/v1/stories/ endpoint is the main way to retrieve company news.
You must include at least one filter: org_name, industry, or location.
You can also filter by activity type, recency, and control output format.

Usage: uv run python -m examples.httpx.stories
"""

import httpx

from examples.config import BASE_URL, HEADERS, print_stories


def list_recent_stories():
    """Fetch technology stories from the last 7 days."""
    print("=== Recent Technology stories (last 7 days) ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"industry": "Technology", "days_ago": 7},
        timeout=120.0,
    )
    response.raise_for_status()
    print_stories(response.json())


def filter_by_activity_type():
    """Filter stories by activity type (e.g. M&A, partnerships)."""
    print("=== CorporateFinanceActivity stories in Technology ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={
            "industry": "Technology",
            "type": "CorporateFinanceActivity",
            "days_ago": 30,
        },
        timeout=120.0,
    )
    response.raise_for_status()
    print_stories(response.json())


def simple_output_format():
    """Use the 'simple' output format for a more compact response."""
    print("=== Stories with simple output format ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"industry": "Technology", "output": "simple", "days_ago": 7},
        timeout=120.0,
    )
    response.raise_for_status()
    print_stories(response.json())


def get_story_by_uri():
    """Fetch a specific story by its URI."""
    # First, get a story URI from a list query
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"industry": "Technology", "output": "simple", "days_ago": 7},
        timeout=120.0,
    )
    response.raise_for_status()
    data = response.json()

    if not data["results"]:
        print("No stories found.")
        return

    story_uri = data["results"][0]["uri"]
    print(f"=== Fetching story detail: {story_uri} ===\n")

    detail = httpx.get(
        f"{BASE_URL}/api/v1/stories/{story_uri}/",
        headers=HEADERS,
        timeout=120.0,
    )
    detail.raise_for_status()
    story = detail.json()

    print(f"  Headline: {story['headline']}")
    print(f"  Activity: {story['activity_class']}")
    print(f"  Published: {story['published_date']} by {story['published_by']}")
    print(f"  URL: {story['document_url']}")
    print(f"  Syracuse URI: {story['uri']}")
    print(f"  Extract: {story['document_extract'][:120]}...")
    if story.get("actors_by_role"):
        print(f"  Actors: {story['actors_by_role']}")
    print()


if __name__ == "__main__":
    list_recent_stories()
    filter_by_activity_type()
    simple_output_format()
    get_story_by_uri()
