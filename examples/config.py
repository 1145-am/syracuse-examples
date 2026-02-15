"""Shared configuration for all examples."""

import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://syracuse.1145.am"
API_KEY = os.environ["SYRACUSE_API_KEY"]
HEADERS = {"Authorization": f"Token {API_KEY}"}


def print_stories(data, limit=5):
    """Print a page of story results."""
    print(f"Found {data['count']} stories\n")
    for story in data["results"][:limit]:
        print(f"  [{story['activity_class']}] {story['headline']}")
        print(f"  Published: {story['published_date']} by {story['published_by']}")
        print(f"  URL: {story['document_url']}")
        print(f"  Syracuse URI: {story['uri']}")
        print(f"  Extract: {story['document_extract'][:120]}...")
        print()
