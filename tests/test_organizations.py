"""Tests for examples/{httpx,requests}/organizations.py."""

from tests.fixtures import STORIES_PAGE

BASE = "https://syracuse.1145.am"


def test_search_organization(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/stories/organization/", json=STORIES_PAGE)

    search_organization = mock_http.import_func("organizations", "search_organization")
    search_organization()

    captured = capsys.readouterr()
    assert "Stories about 'Microsoft'" in captured.out
    assert "Found 42 stories" in captured.out


def test_search_via_main_endpoint(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    search_via_main_endpoint = mock_http.import_func("organizations", "search_via_main_endpoint")
    search_via_main_endpoint()

    captured = capsys.readouterr()
    assert "Stories mentioning 'Apple'" in captured.out
    assert "Found 42 stories" in captured.out
