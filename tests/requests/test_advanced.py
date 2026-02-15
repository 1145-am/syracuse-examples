"""Tests for examples/requests/advanced.py."""

import responses as responses_mock

from tests.fixtures import STORIES_PAGE, STORIES_PAGE_LAST

BASE = "https://syracuse.1145.am"


@responses_mock.activate
def test_combine_filters(capsys):
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    from examples.requests.advanced import combine_filters

    combine_filters()

    captured = capsys.readouterr()
    assert "Combined filters" in captured.out
    assert "Found 42 stories" in captured.out


@responses_mock.activate
def test_paginate_results(capsys):
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=STORIES_PAGE)
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=STORIES_PAGE)
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=STORIES_PAGE_LAST)

    from examples.requests.advanced import paginate_results

    paginate_results()

    captured = capsys.readouterr()
    assert "Page 1:" in captured.out
    assert "Page 2:" in captured.out
    assert "Page 3:" in captured.out


@responses_mock.activate
def test_paginate_results_stops_at_last_page(capsys):
    page = {**STORIES_PAGE, "next": None}
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=page)

    from examples.requests.advanced import paginate_results

    paginate_results()

    captured = capsys.readouterr()
    assert "Page 1:" in captured.out
    assert "Page 2:" not in captured.out


@responses_mock.activate
def test_with_and_without_similar(capsys):
    combined = {**STORIES_PAGE, "count": 30}
    uncombined = {**STORIES_PAGE, "count": 50}
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=combined)
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=uncombined)

    from examples.requests.advanced import with_and_without_similar

    with_and_without_similar()

    captured = capsys.readouterr()
    assert "30 stories" in captured.out
    assert "50 stories" in captured.out


@responses_mock.activate
def test_multiple_industries(capsys):
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    from examples.requests.advanced import multiple_industries

    multiple_industries()

    captured = capsys.readouterr()
    assert "Multiple industries" in captured.out
    assert "Found 42 stories" in captured.out


@responses_mock.activate
def test_multiple_locations(capsys):
    responses_mock.add(responses_mock.GET, f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    from examples.requests.advanced import multiple_locations

    multiple_locations()

    captured = capsys.readouterr()
    assert "Multiple locations" in captured.out
    assert "Found 42 stories" in captured.out
