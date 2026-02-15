"""Tests for examples/{httpx,requests}/advanced.py."""

from tests.fixtures import STORIES_PAGE, STORIES_PAGE_LAST

BASE = "https://syracuse.1145.am"


def test_combine_filters(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    combine_filters = mock_http.import_func("advanced", "combine_filters")
    combine_filters()

    captured = capsys.readouterr()
    assert "Combined filters" in captured.out
    assert "Found 42 stories" in captured.out


def test_paginate_results(mock_http, capsys):
    mock_http.get_sequence(
        f"{BASE}/api/v1/stories/",
        jsons=[STORIES_PAGE, STORIES_PAGE, STORIES_PAGE_LAST],
    )

    paginate_results = mock_http.import_func("advanced", "paginate_results")
    paginate_results()

    captured = capsys.readouterr()
    assert "Page 1:" in captured.out
    assert "Page 2:" in captured.out
    assert "Page 3:" in captured.out


def test_paginate_results_stops_at_last_page(mock_http, capsys):
    page = {**STORIES_PAGE, "next": None}
    mock_http.get(f"{BASE}/api/v1/stories/", json=page)

    paginate_results = mock_http.import_func("advanced", "paginate_results")
    paginate_results()

    captured = capsys.readouterr()
    assert "Page 1:" in captured.out
    assert "Page 2:" not in captured.out


def test_with_and_without_similar(mock_http, capsys):
    combined = {**STORIES_PAGE, "count": 30}
    uncombined = {**STORIES_PAGE, "count": 50}
    mock_http.get_sequence(
        f"{BASE}/api/v1/stories/",
        jsons=[combined, uncombined],
    )

    with_and_without_similar = mock_http.import_func("advanced", "with_and_without_similar")
    with_and_without_similar()

    captured = capsys.readouterr()
    assert "30 stories" in captured.out
    assert "50 stories" in captured.out


def test_multiple_industries(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    multiple_industries = mock_http.import_func("advanced", "multiple_industries")
    multiple_industries()

    captured = capsys.readouterr()
    assert "Multiple industries" in captured.out
    assert "Found 42 stories" in captured.out


def test_multiple_locations(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    multiple_locations = mock_http.import_func("advanced", "multiple_locations")
    multiple_locations()

    captured = capsys.readouterr()
    assert "Multiple locations" in captured.out
    assert "Found 42 stories" in captured.out
