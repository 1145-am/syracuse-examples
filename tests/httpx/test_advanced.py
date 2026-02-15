"""Tests for examples/httpx/advanced.py."""

import respx
from httpx import Response

from tests.fixtures import STORIES_PAGE, STORIES_PAGE_LAST


@respx.mock
def test_combine_filters(capsys):
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=STORIES_PAGE)
    )

    from examples.httpx.advanced import combine_filters

    combine_filters()

    captured = capsys.readouterr()
    assert "Combined filters" in captured.out
    assert "Found 42 stories" in captured.out


@respx.mock
def test_paginate_results(capsys):
    route = respx.get("https://syracuse.1145.am/api/v1/stories/")
    route.side_effect = [
        Response(200, json=STORIES_PAGE),
        Response(200, json=STORIES_PAGE),
        Response(200, json=STORIES_PAGE_LAST),
    ]

    from examples.httpx.advanced import paginate_results

    paginate_results()

    captured = capsys.readouterr()
    assert "Page 1:" in captured.out
    assert "Page 2:" in captured.out
    assert "Page 3:" in captured.out


@respx.mock
def test_paginate_results_stops_at_last_page(capsys):
    page = {**STORIES_PAGE, "next": None}
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=page)
    )

    from examples.httpx.advanced import paginate_results

    paginate_results()

    captured = capsys.readouterr()
    assert "Page 1:" in captured.out
    assert "Page 2:" not in captured.out


@respx.mock
def test_with_and_without_similar(capsys):
    combined = {**STORIES_PAGE, "count": 30}
    uncombined = {**STORIES_PAGE, "count": 50}

    route = respx.get("https://syracuse.1145.am/api/v1/stories/")
    route.side_effect = [
        Response(200, json=combined),
        Response(200, json=uncombined),
    ]

    from examples.httpx.advanced import with_and_without_similar

    with_and_without_similar()

    captured = capsys.readouterr()
    assert "30 stories" in captured.out
    assert "50 stories" in captured.out


@respx.mock
def test_multiple_industries(capsys):
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=STORIES_PAGE)
    )

    from examples.httpx.advanced import multiple_industries

    multiple_industries()

    captured = capsys.readouterr()
    assert "Multiple industries" in captured.out
    assert "Found 42 stories" in captured.out


@respx.mock
def test_multiple_locations(capsys):
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=STORIES_PAGE)
    )

    from examples.httpx.advanced import multiple_locations

    multiple_locations()

    captured = capsys.readouterr()
    assert "Multiple locations" in captured.out
    assert "Found 42 stories" in captured.out
