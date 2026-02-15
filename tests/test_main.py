"""Tests for main.py and main_requests.py."""

import respx
from httpx import Response

from tests.fixtures import STORIES_PAGE


@respx.mock
def test_main_httpx(capsys):
    respx.get("https://syracuse.1145.am/api/v1/stories/").mock(
        return_value=Response(200, json=STORIES_PAGE)
    )

    import main
    from importlib import reload

    reload(main)
    main.main()

    captured = capsys.readouterr()
    assert "Total results: 42" in captured.out
    assert "Acme Corp acquires Widget Inc" in captured.out


def test_main_requests(capsys):
    import responses as responses_mock

    with responses_mock.RequestsMock() as rsps:
        rsps.add(
            rsps.GET,
            "https://syracuse.1145.am/api/v1/stories/",
            json=STORIES_PAGE,
            status=200,
        )

        import main_requests
        from importlib import reload

        reload(main_requests)
        main_requests.main()

    captured = capsys.readouterr()
    assert "Total results: 42" in captured.out
    assert "Acme Corp acquires Widget Inc" in captured.out
