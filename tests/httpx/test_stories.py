"""Tests for examples/httpx/stories.py."""

import respx
from httpx import Response

from tests.fixtures import STORIES_PAGE, STORY_FULL, STORY_SIMPLE


@respx.mock
def test_list_recent_stories(capsys):
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=STORIES_PAGE)
    )

    from examples.httpx.stories import list_recent_stories

    list_recent_stories()

    captured = capsys.readouterr()
    assert "Found 42 stories" in captured.out
    assert "Acme Corp acquires Widget Inc" in captured.out


@respx.mock
def test_filter_by_activity_type(capsys):
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=STORIES_PAGE)
    )

    from examples.httpx.stories import filter_by_activity_type

    filter_by_activity_type()

    captured = capsys.readouterr()
    assert "corporate finance stories" in captured.out


@respx.mock
def test_simple_output_format(capsys):
    page = {**STORIES_PAGE, "results": [STORY_SIMPLE]}
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=page)
    )

    from examples.httpx.stories import simple_output_format

    simple_output_format()

    captured = capsys.readouterr()
    assert "Foo partners with Bar" in captured.out
    assert "Summary:" in captured.out


@respx.mock
def test_get_story_by_uri(capsys):
    page = {**STORIES_PAGE, "results": [STORY_SIMPLE]}
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=page)
    )
    respx.get(url__startswith="https://syracuse.1145.am/api/v1/stories/https").mock(
        return_value=Response(200, json=STORY_FULL)
    )

    from examples.httpx.stories import get_story_by_uri

    get_story_by_uri()

    captured = capsys.readouterr()
    assert "Headline: Acme Corp acquires Widget Inc" in captured.out
    assert "Actors:" in captured.out


@respx.mock
def test_get_story_by_uri_no_results(capsys):
    empty = {**STORIES_PAGE, "count": 0, "results": []}
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=empty)
    )

    from examples.httpx.stories import get_story_by_uri

    get_story_by_uri()

    captured = capsys.readouterr()
    assert "No stories found" in captured.out
