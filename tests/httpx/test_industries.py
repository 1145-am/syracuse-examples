"""Tests for examples/httpx/industries.py."""

import respx
from httpx import Response

from tests.fixtures import INDUSTRY_CLUSTERS_PAGE, STORIES_PAGE


@respx.mock
def test_list_industry_clusters(capsys):
    respx.get("https://syracuse.1145.am/api/v1/industry-clusters/").mock(
        return_value=Response(200, json=INDUSTRY_CLUSTERS_PAGE)
    )

    from examples.httpx.industries import list_industry_clusters

    list_industry_clusters()

    captured = capsys.readouterr()
    assert "Found 5996 industry clusters" in captured.out
    assert "topic_id=476" in captured.out


@respx.mock
def test_search_industries(capsys):
    respx.get("https://syracuse.1145.am/api/v1/industry-clusters/").mock(
        return_value=Response(200, json=INDUSTRY_CLUSTERS_PAGE)
    )

    from examples.httpx.industries import search_industries

    search_industries()

    captured = capsys.readouterr()
    assert "Searching industries for 'technology'" in captured.out


@respx.mock
def test_stories_by_industry(capsys):
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=STORIES_PAGE)
    )

    from examples.httpx.industries import stories_by_industry

    stories_by_industry()

    captured = capsys.readouterr()
    assert "Stories in 'Technology' industry" in captured.out
    assert "Found 42 stories" in captured.out


@respx.mock
def test_stories_by_industry_and_location(capsys):
    respx.get("https://syracuse.1145.am/api/v1/stories/industry-location/").mock(
        return_value=Response(200, json=STORIES_PAGE)
    )

    from examples.httpx.industries import stories_by_industry_and_location

    stories_by_industry_and_location()

    captured = capsys.readouterr()
    assert "Technology stories in US" in captured.out
