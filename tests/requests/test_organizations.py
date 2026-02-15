"""Tests for examples/requests/organizations.py."""

import responses as responses_mock

from tests.fixtures import STORIES_PAGE

BASE = "https://syracuse.1145.am"


@responses_mock.activate
def test_search_organization(capsys):
    responses_mock.add(
        responses_mock.GET, f"{BASE}/api/v1/stories/organization/", json=STORIES_PAGE
    )

    from examples.requests.organizations import search_organization

    search_organization()

    captured = capsys.readouterr()
    assert "Stories about 'Microsoft'" in captured.out
    assert "Found 42 stories" in captured.out


@responses_mock.activate
def test_search_via_main_endpoint(capsys):
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    from examples.requests.organizations import search_via_main_endpoint

    search_via_main_endpoint()

    captured = capsys.readouterr()
    assert "Stories mentioning 'Apple'" in captured.out
    assert "Found 42 stories" in captured.out
