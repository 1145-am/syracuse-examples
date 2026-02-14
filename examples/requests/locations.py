"""Location and geography examples (requests).

Browse GeoNames locations and location groups, and filter stories by location.

GeoNames locations are paginated. Location groups are returned as a flat list
with parent/child relationships forming a hierarchy.

Usage: uv run python examples/requests/locations.py
"""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://syracuse.1145.am"
API_KEY = os.environ["SYRACUSE_API_KEY"]
HEADERS = {"Authorization": f"Token {API_KEY}"}


def list_geonames():
    """List available GeoNames locations."""
    print("=== GeoNames locations ===\n")
    response = requests.get(
        f"{BASE_URL}/api/v1/geonames/",
        headers=HEADERS,
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()

    print(f"Found {data['count']} locations\n")
    for loc in data["results"][:10]:
        print(f"  [{loc['geonames_id']}] {loc['name']} ({loc.get('country_code', 'N/A')})")
    print()


def list_location_groups():
    """List location groups (hierarchical groupings like regions, sub-regions).

    Note: this endpoint returns a flat list (not paginated).
    """
    print("=== Location groups ===\n")
    response = requests.get(
        f"{BASE_URL}/api/v1/location-groups/",
        headers=HEADERS,
        timeout=120,
    )
    response.raise_for_status()
    groups = response.json()  # Returns a list, not paginated

    print(f"Found {len(groups)} location groups\n")
    # Show top-level groups (no parent)
    top_level = [g for g in groups if g["parent"] is None]
    print(f"Top-level regions ({len(top_level)}):")
    for group in top_level:
        print(f"  [{group['id']}] {group['name']} ({len(group['children'])} children)")
    print()


def get_location_group_detail(group_id: str = "Americas"):
    """Get details for a specific location group, including parent/child relationships."""
    print(f"=== Location group: {group_id} ===\n")
    response = requests.get(
        f"{BASE_URL}/api/v1/location-groups/{group_id}/",
        headers=HEADERS,
        timeout=120,
    )
    response.raise_for_status()
    group = response.json()

    print(f"  Name: {group['name']}")
    print(f"  ID: {group['id']}")
    if group.get("parent"):
        print(f"  Parent: {group['parent']}")
    if group.get("children"):
        print(f"  Children ({len(group['children'])}):")
        for child_url in group["children"][:10]:
            print(f"    {child_url}")
    print()


def stories_by_location(location: str = "France"):
    """Filter stories by location.

    The location parameter accepts country names, ISO country codes (US, GB, FR),
    US state codes (NY, CA), and region names (Asia, Europe, Americas) — all case-insensitive.

    You can also use location_id for case-sensitive location group IDs (e.g. "US-CA", "GB").
    """
    print(f"=== Stories in '{location}' ===\n")
    response = requests.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"location": location, "days_ago": 30},
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
    list_geonames()
    list_location_groups()
    get_location_group_detail()
    stories_by_location()
