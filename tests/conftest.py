"""Shared test configuration."""

import importlib

import pytest


class MockHttp:
    """Uniform interface over respx and responses mocking."""

    def __init__(self, backend, *, respx_mod=None, responses_ctx=None):
        self.backend = backend
        self._respx = respx_mod
        self._responses = responses_ctx

    def get(self, url, *, json):
        if self.backend == "httpx":
            from httpx import Response

            self._respx.get(url).mock(return_value=Response(200, json=json))
        else:
            self._responses.add(self._responses.GET, url, json=json)

    def get_sequence(self, url, *, jsons):
        if self.backend == "httpx":
            from httpx import Response

            route = self._respx.get(url)
            route.side_effect = [Response(200, json=j) for j in jsons]
        else:
            for j in jsons:
                self._responses.add(self._responses.GET, url, json=j)

    def get_startswith(self, url_prefix, *, json):
        if self.backend == "httpx":
            from httpx import Response

            self._respx.get(url__startswith=url_prefix).mock(
                return_value=Response(200, json=json)
            )
        else:
            import re

            self._responses.add(
                self._responses.GET,
                re.compile(re.escape(url_prefix)),
                json=json,
            )

    def import_func(self, module_name, func_name):
        pkg = "httpx" if self.backend == "httpx" else "requests"
        mod = importlib.import_module(f"examples.{pkg}.{module_name}")
        return getattr(mod, func_name)


@pytest.fixture(autouse=True)
def set_api_key(monkeypatch):
    """Set a fake API key so example modules can be imported."""
    monkeypatch.setenv("SYRACUSE_API_KEY", "test-key-000")


@pytest.fixture(params=["httpx", "requests"])
def mock_http(request):
    if request.param == "httpx":
        import respx as respx_mod

        with respx_mod.mock:
            yield MockHttp("httpx", respx_mod=respx_mod)
    else:
        import responses

        with responses.RequestsMock() as rsps:
            yield MockHttp("requests", responses_ctx=rsps)
