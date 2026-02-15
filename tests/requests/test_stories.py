"""Tests for examples/requests/stories.py."""

import responses as responses_mock

from tests.fixtures import STORIES_PAGE, STORY_FULL, STORY_SIMPLE

BASE = "https://syracuse.1145.am"


@responses_mock.activate
def test_list_recent_stories(capsys):
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    from examples.requests.stories import list_recent_stories

    list_recent_stories()

    captured = capsys.readouterr()
    assert "Found 42 stories" in captured.out
    assert "Acme Corp acquires Widget Inc" in captured.out


@responses_mock.activate
def test_filter_by_activity_type(capsys):
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    from examples.requests.stories import filter_by_activity_type

    filter_by_activity_type()

    captured = capsys.readouterr()
    assert "corporate finance stories" in captured.out


@responses_mock.activate
def test_simple_output_format(capsys):
    page = {**STORIES_PAGE, "results": [STORY_SIMPLE]}
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=page)

    from examples.requests.stories import simple_output_format

    simple_output_format()

    captured = capsys.readouterr()
    assert "Foo partners with Bar" in captured.out
    assert "Summary:" in captured.out


@responses_mock.activate
def test_get_story_by_uri(capsys):
    page = {**STORIES_PAGE, "results": [STORY_SIMPLE]}
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=page)
    responses_mock.add(
        responses_mock.GET,
        f"{BASE}/api/v1/stories/{STORY_SIMPLE['uri']}/",
        json=STORY_FULL,
    )

    from examples.requests.stories import get_story_by_uri

    get_story_by_uri()

    captured = capsys.readouterr()
    assert "Headline: Acme Corp acquires Widget Inc" in captured.out
    assert "Actors:" in captured.out


@responses_mock.activate
def test_get_story_by_uri_no_results(capsys):
    empty = {**STORIES_PAGE, "count": 0, "results": []}
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=empty)

    from examples.requests.stories import get_story_by_uri

    get_story_by_uri()

    captured = capsys.readouterr()
    assert "No stories found" in captured.out
