"""Tests for examples/{httpx,requests}/industries.py."""

from tests.fixtures import INDUSTRY_CLUSTERS_PAGE, STORIES_PAGE

BASE = "https://syracuse.1145.am"


def test_list_industry_clusters(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/industry-clusters/", json=INDUSTRY_CLUSTERS_PAGE)

    list_industry_clusters = mock_http.import_func("industries", "list_industry_clusters")
    list_industry_clusters()

    captured = capsys.readouterr()
    assert "Found 5996 industry clusters" in captured.out
    assert "topic_id=476" in captured.out


def test_search_industries(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/industry-clusters/", json=INDUSTRY_CLUSTERS_PAGE)

    search_industries = mock_http.import_func("industries", "search_industries")
    search_industries()

    captured = capsys.readouterr()
    assert "Searching industries for 'technology'" in captured.out


def test_stories_by_industry(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    stories_by_industry = mock_http.import_func("industries", "stories_by_industry")
    stories_by_industry()

    captured = capsys.readouterr()
    assert "Stories in 'Technology' industry" in captured.out
    assert "Found 42 stories" in captured.out


def test_stories_by_industry_and_location(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/stories/industry-location/", json=STORIES_PAGE)

    func = mock_http.import_func("industries", "stories_by_industry_and_location")
    func()

    captured = capsys.readouterr()
    assert "Technology stories in US" in captured.out
