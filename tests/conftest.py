"""Shared test configuration."""

import pytest


@pytest.fixture(autouse=True)
def set_api_key(monkeypatch):
    """Set a fake API key so example modules can be imported."""
    monkeypatch.setenv("SYRACUSE_API_KEY", "test-key-000")
