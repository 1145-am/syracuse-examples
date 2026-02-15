"""Quick-start example for the Syracuse Company News API (httpx).

Fetches recent company news stories and prints them out.

Usage:
    1. Copy .env.example to .env and add your API key
    2. Run: uv run python main.py

For a requests version, see main_requests.py.
"""

import os

import httpx
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://syracuse.1145.am"
API_KEY = os.environ["SYRACUSE_API_KEY"]
HEADERS = {"Authorization": f"Token {API_KEY}"}


def main():
    print("=== Fetching recent tech stories ===\n")
    response = httpx.get(
        f"{BASE_URL}/api/v1/stories/",
        headers=HEADERS,
        params={"industry": "Technology", "days_ago": 7},
        timeout=30.0,
    )
    response.raise_for_status()
    data = response.json()

    print(f"Total results: {data['count']}")
    print(f"Showing first page ({len(data['results'])} stories)\n")

    for story in data["results"][:5]:
        print(f"  [{story['activity_class']}] {story['headline']}")
        print(f"  Published: {story['published_date']} by {story['published_by']}")
        print(f"  URL: {story['document_url']}")
        print(f"  Syracuse URI: {story['uri']}")
        print(f"  Extract: {story['document_extract'][:120]}...")
        print()


if __name__ == "__main__":
    main()
