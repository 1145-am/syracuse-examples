# CLAUDE.md

## Project overview

Example scripts for the [Syracuse Company News API](https://syracuse.1145.am/docs/). Two variants of every example are provided: one using `httpx`, one using `requests`. The top-level `main.py` (httpx) and `main_requests.py` (requests) are self-contained quick-start scripts; the files under `examples/` import shared config from `examples/config.py`.

## Project structure

```
main.py / main_requests.py   # Self-contained quick-start scripts
examples/
  config.py                  # Shared BASE_URL, API_KEY, HEADERS
  httpx/                     # httpx examples (stories, orgs, industries, locations, advanced)
  requests/                  # requests examples (same set)
tests/
  conftest.py                # Autouse env fixture + MockHttp parametrized fixture
  fixtures.py                # Mock response payloads
  test_*.py                  # Each test runs against both httpx and requests backends
```

## Setup

```bash
cp .env.example .env         # Then set SYRACUSE_API_KEY
uv sync
```

## Running examples

```bash
uv run python main.py                          # Quick start (httpx)
uv run python main_requests.py                 # Quick start (requests)
uv run python -m examples.httpx.stories        # Topic-specific example
uv run python -m examples.requests.stories     # Same, with requests
```

## Running tests

```bash
uv run pytest           # All 44 tests
uv run pytest -v        # Verbose output
uv run pytest -k httpx  # Only httpx backend tests
```

Tests use `respx` (httpx) and `responses` (requests) to mock HTTP calls. A parametrized `mock_http` fixture in `conftest.py` runs each test against both backends. No network access or API key required.

## Key conventions

- Python 3.13+, managed with `uv`
- API key loaded from `SYRACUSE_API_KEY` env var (via `python-dotenv`)
- All API requests use `Authorization: Token <key>` header
- Example files under `examples/httpx/` and `examples/requests/` must stay separate and independently runnable, but share config via `examples/config.py`
- Examples must be run as modules (`python -m examples.httpx.stories`) not as scripts, because they import from the `examples` package
- `main.py` and `main_requests.py` are intentionally self-contained (no shared imports) for copy-paste friendliness
- Timeout: 120s for example scripts, 30s for quick-start mains

## API notes

- Base URL: `https://syracuse.1145.am`
- `/api/v1/stories/` requires at least one filter: `org_name`, `industry`, or `location`
- `location` param accepts country names, ISO codes (US, GB), US state codes (NY, CA), region names (Asia, Europe) -- case-insensitive
- `industry` param does semantic vector search -- any descriptive text works
- `/api/v1/location-groups/` returns a flat list (not paginated)
- Story fields: `activity_class`, `uri`, `headline`, `document_extract`, `published_date`, `published_by`, `document_url` (consistent between full and simple output)
- Industry clusters use `topic_id` and `representative_doc` (list of names)
- GeoNames use `geonames_id`
