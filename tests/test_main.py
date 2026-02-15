"""Tests for main.py and main_requests.py."""

from importlib import reload

from tests.fixtures import STORIES_PAGE

BASE = "https://syracuse.1145.am"


def test_main(mock_http, capsys):
    mock_http.get(f"{BASE}/api/v1/stories/", json=STORIES_PAGE)

    if mock_http.backend == "httpx":
        import main

        reload(main)
        main.main()
    else:
        import main_requests

        reload(main_requests)
        main_requests.main()

    captured = capsys.readouterr()
    assert "Total results: 42" in captured.out
    assert "Acme Corp acquires Widget Inc" in captured.out
