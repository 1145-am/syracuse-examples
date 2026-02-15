"""Tests for examples/httpx/organizations.py."""

import respx
from httpx import Response

from tests.fixtures import STORIES_PAGE


@respx.mock
def test_search_organization(capsys):
    respx.get("https://syracuse.1145.am/api/v1/stories/organization/").mock(
        return_value=Response(200, json=STORIES_PAGE)
    )

    from examples.httpx.organizations import search_organization

    search_organization()

    captured = capsys.readouterr()
    assert "Stories about 'Microsoft'" in captured.out
    assert "Found 42 stories" in captured.out


@respx.mock
def test_search_via_main_endpoint(capsys):
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=STORIES_PAGE)
    )

    from examples.httpx.organizations import search_via_main_endpoint

    search_via_main_endpoint()

    captured = capsys.readouterr()
    assert "Stories mentioning 'Apple'" in captured.out
    assert "Found 42 stories" in captured.out
