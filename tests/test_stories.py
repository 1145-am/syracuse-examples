"""Tests for examples/{httpx,requests}/stories.py."""

from tests.fixtures import STORIES_PAGE, STORY_FULL, STORY_SIMPLE

BASE = "https://syracuse.1145.am"


def test_list_recent_stories(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    list_recent_stories = mock_http.import_func("stories", "list_recent_stories")
    list_recent_stories()

    captured = capsys.readouterr()
    assert "Found 42 stories" in captured.out
    assert "Acme Corp acquires Widget Inc" in captured.out


def test_filter_by_activity_type(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    filter_by_activity_type = mock_http.import_func("stories", "filter_by_activity_type")
    filter_by_activity_type()

    captured = capsys.readouterr()
    assert "corporate finance stories" in captured.out


def test_simple_output_format(mock_http, capsys):
    page = {**STORIES_PAGE, "results": [STORY_SIMPLE]}
    mock_http.get(f"{BASE}/api/v1/stories/", json=page)

    simple_output_format = mock_http.import_func("stories", "simple_output_format")
    simple_output_format()

    captured = capsys.readouterr()
    assert "Foo partners with Bar" in captured.out
    assert "Summary:" in captured.out


def test_get_story_by_uri(mock_http, capsys):
    page = {**STORIES_PAGE, "results": [STORY_SIMPLE]}
    mock_http.get(f"{BASE}/api/v1/stories/", json=page)
    mock_http.get_startswith(f"{BASE}/api/v1/stories/https", json=STORY_FULL)

    get_story_by_uri = mock_http.import_func("stories", "get_story_by_uri")
    get_story_by_uri()

    captured = capsys.readouterr()
    assert "Headline: Acme Corp acquires Widget Inc" in captured.out
    assert "Actors:" in captured.out


def test_get_story_by_uri_no_results(mock_http, capsys):
    empty = {**STORIES_PAGE, "count": 0, "results": []}
    mock_http.get(f"{BASE}/api/v1/stories/", json=empty)

    get_story_by_uri = mock_http.import_func("stories", "get_story_by_uri")
    get_story_by_uri()

    captured = capsys.readouterr()
    assert "No stories found" in captured.out
