"""Tests for examples/requests/industries.py."""

import responses as responses_mock

from tests.fixtures import INDUSTRY_CLUSTERS_PAGE, STORIES_PAGE

BASE = "https://syracuse.1145.am"


@responses_mock.activate
def test_list_industry_clusters(capsys):
    responses_mock.add(
        responses_mock.GET, f"{BASE}/api/v1/industry-clusters/", json=INDUSTRY_CLUSTERS_PAGE
    )

    from examples.requests.industries import list_industry_clusters

    list_industry_clusters()

    captured = capsys.readouterr()
    assert "Found 5996 industry clusters" in captured.out
    assert "topic_id=476" in captured.out


@responses_mock.activate
def test_search_industries(capsys):
    responses_mock.add(
        responses_mock.GET, f"{BASE}/api/v1/industry-clusters/", json=INDUSTRY_CLUSTERS_PAGE
    )

    from examples.requests.industries import search_industries

    search_industries()

    captured = capsys.readouterr()
    assert "Searching industries for 'technology'" in captured.out


@responses_mock.activate
def test_stories_by_industry(capsys):
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    from examples.requests.industries import stories_by_industry

    stories_by_industry()

    captured = capsys.readouterr()
    assert "Stories in 'Technology' industry" in captured.out
    assert "Found 42 stories" in captured.out


@responses_mock.activate
def test_stories_by_industry_and_location(capsys):
    responses_mock.add(
        responses_mock.GET, f"{BASE}/api/v1/stories/industry-location/", json=STORIES_PAGE
    )

    from examples.requests.industries import stories_by_industry_and_location

    stories_by_industry_and_location()

    captured = capsys.readouterr()
    assert "Technology stories in US" in captured.out
