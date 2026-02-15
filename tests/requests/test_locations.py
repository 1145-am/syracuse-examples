"""Tests for examples/requests/locations.py."""

import responses as responses_mock

from tests.fixtures import (
    GEONAMES_PAGE,
    LOCATION_GROUP,
    LOCATION_GROUPS_LIST,
    STORIES_PAGE,
)

BASE = "https://syracuse.1145.am"


@responses_mock.activate
def test_list_geonames(capsys):
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/geonames/", json=GEONAMES_PAGE)

    from examples.requests.locations import list_geonames

    list_geonames()

    captured = capsys.readouterr()
    assert "Found 37736 locations" in captured.out
    assert "New York City" in captured.out


@responses_mock.activate
def test_list_location_groups(capsys):
    responses_mock.add(
        responses_mock.GET, f"{BASE}/api/v1/location-groups/", json=LOCATION_GROUPS_LIST
    )

    from examples.requests.locations import list_location_groups

    list_location_groups()

    captured = capsys.readouterr()
    assert "Found 2 location groups" in captured.out
    assert "Top-level regions (2):" in captured.out


@responses_mock.activate
def test_get_location_group_detail(capsys):
    responses_mock.add(
        responses_mock.GET, f"{BASE}/api/v1/location-groups/Americas/", json=LOCATION_GROUP
    )

    from examples.requests.locations import get_location_group_detail

    get_location_group_detail()

    captured = capsys.readouterr()
    assert "Name: Americas" in captured.out
    assert "Children (2):" in captured.out


@responses_mock.activate
def test_stories_by_location(capsys):
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    from examples.requests.locations import stories_by_location

    stories_by_location()

    captured = capsys.readouterr()
    assert "Stories in 'New Zealand'" in captured.out
    assert "Found 42 stories" in captured.out
