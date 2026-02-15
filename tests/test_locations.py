"""Tests for examples/{httpx,requests}/locations.py."""

from tests.fixtures import GEONAMES_PAGE, LOCATION_GROUP, LOCATION_GROUPS_LIST, STORIES_PAGE

BASE = "https://syracuse.1145.am"


def test_list_geonames(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/geonames/", json=GEONAMES_PAGE)

    list_geonames = mock_http.import_func("locations", "list_geonames")
    list_geonames()

    captured = capsys.readouterr()
    assert "Found 37736 locations" in captured.out
    assert "New York City" in captured.out


def test_list_location_groups(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/location-groups/", json=LOCATION_GROUPS_LIST)

    list_location_groups = mock_http.import_func("locations", "list_location_groups")
    list_location_groups()

    captured = capsys.readouterr()
    assert "Found 2 location groups" in captured.out
    assert "Top-level regions (2):" in captured.out


def test_get_location_group_detail(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/location-groups/Americas/", json=LOCATION_GROUP)

    get_location_group_detail = mock_http.import_func("locations", "get_location_group_detail")
    get_location_group_detail()

    captured = capsys.readouterr()
    assert "Name: Americas" in captured.out
    assert "Children (2):" in captured.out


def test_stories_by_location(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    stories_by_location = mock_http.import_func("locations", "stories_by_location")
    stories_by_location()

    captured = capsys.readouterr()
    assert "Stories in 'New Zealand'" in captured.out
    assert "Found 42 stories" in captured.out
