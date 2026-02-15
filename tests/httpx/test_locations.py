"""Tests for examples/httpx/locations.py."""

import respx
from httpx import Response

from tests.fixtures import (
    GEONAMES_PAGE,
    LOCATION_GROUP,
    LOCATION_GROUPS_LIST,
    STORIES_PAGE,
)


@respx.mock
def test_list_geonames(capsys):
    respx.get("https://syracuse.1145.am/api/v1/geonames/").mock(
        return_value=Response(200, json=GEONAMES_PAGE)
    )

    from examples.httpx.locations import list_geonames

    list_geonames()

    captured = capsys.readouterr()
    assert "Found 37736 locations" in captured.out
    assert "New York City" in captured.out


@respx.mock
def test_list_location_groups(capsys):
    respx.get("https://syracuse.1145.am/api/v1/location-groups/").mock(
        return_value=Response(200, json=LOCATION_GROUPS_LIST)
    )

    from examples.httpx.locations import list_location_groups

    list_location_groups()

    captured = capsys.readouterr()
    assert "Found 2 location groups" in captured.out
    assert "Top-level regions (2):" in captured.out
    assert "[Americas]" in captured.out


@respx.mock
def test_get_location_group_detail(capsys):
    respx.get("https://syracuse.1145.am/api/v1/location-groups/Americas/").mock(
        return_value=Response(200, json=LOCATION_GROUP)
    )

    from examples.httpx.locations import get_location_group_detail

    get_location_group_detail()

    captured = capsys.readouterr()
    assert "Name: Americas" in captured.out
    assert "Children (2):" in captured.out


@respx.mock
def test_stories_by_location(capsys):
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=STORIES_PAGE)
    )

    from examples.httpx.locations import stories_by_location

    stories_by_location()

    captured = capsys.readouterr()
    assert "Stories in 'New Zealand'" in captured.out
    assert "Found 42 stories" in captured.out
