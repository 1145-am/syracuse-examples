# Syracuse API Examples

Example scripts for the [Syracuse Company News API](https://syracuse.1145.am/docs/).

Syracuse is a structured news API that tracks company activities — M&A, partnerships, leadership changes, product launches, and more — across industries and geographies worldwide.

## Setup

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).

```bash
# Clone the repo
git clone <repo-url>
cd syracuse-examples

# Copy the env file and add your API key
cp .env.example .env
# Edit .env and set SYRACUSE_API_KEY=your-key-here

# Install dependencies
uv sync
```

### Getting an API key

```bash
curl -X POST https://syracuse.1145.am/api/v1/register-and-get-key/ \
  -H "Content-Type: application/json" \
  -d '{"email": "you@example.com"}'
```

This returns a JSON response with your API token. Verify your email to increase your rate limit from 30 to 300 queries/month.

## Quick try with curl

Don't want to clone the repo? Try the API directly (pipe to `jq .` for pretty-printing, or drop it for raw JSON):

```bash
# Fetch recent technology stories
curl -s 'https://syracuse.1145.am/api/v1/stories/?industry=Technology&days_ago=7' \
  -H 'Authorization: Token YOUR_API_KEY' | jq .

# Search for stories about a specific company
curl -s 'https://syracuse.1145.am/api/v1/stories/organization/?org_name=Microsoft' \
  -H 'Authorization: Token YOUR_API_KEY' | jq .

# Browse available industry clusters
curl -s 'https://syracuse.1145.am/api/v1/industry-clusters/?search=technology' \
  -H 'Authorization: Token YOUR_API_KEY' | jq .

# Filter by industry and location together
curl -s 'https://syracuse.1145.am/api/v1/stories/industry-location/?industry=Technology&location=US' \
  -H 'Authorization: Token YOUR_API_KEY' | jq .
```

## Quick start

```bash
uv run python main.py             # httpx
uv run python main_requests.py    # requests
```

## Examples

Examples are provided in two variants — pick whichever HTTP library you prefer:

### httpx

```bash
uv run python -m examples.httpx.stories
uv run python -m examples.httpx.organizations
uv run python -m examples.httpx.industries
uv run python -m examples.httpx.locations
uv run python -m examples.httpx.advanced
```

### requests

```bash
uv run python -m examples.requests.stories
uv run python -m examples.requests.organizations
uv run python -m examples.requests.industries
uv run python -m examples.requests.locations
uv run python -m examples.requests.advanced
```

### What each example covers

| File | Description |
|------|-------------|
| `stories.py` | List stories, filter by activity type, change output format, fetch by URI |
| `organizations.py` | Search stories by company name |
| `industries.py` | Browse industry clusters, filter stories by industry |
| `locations.py` | Browse GeoNames/location groups, filter stories by location |
| `advanced.py` | Combine filters, pagination, multiple industries/locations |

## Authentication

All requests require a `Token` auth header:

```
Authorization: Token your-api-key-here
```

## Activity types

The API tracks these company activity types:

- **CorporateFinanceActivity** — M&A, investments, stock acquisitions
- **PartnershipActivity** — partnerships, customer/supplier relationships
- **RoleActivity** — senior personnel changes
- **LocationActivity** — office/facility openings and closures
- **ProductActivity** — product launches
- **AnalystRatingActivity** — analyst updates
- **EquityActionsActivity** — stock repurchases, dividends
- **FinancialReportingActivity** — earnings announcements
- **FinancialsActivity** — revenue, EBITDA
- **IncidentActivity** — safety or adverse events
- **LegalActivity** — lawsuits, SEC investigations
- **MarketingActivity** — advertising campaigns
- **OperationsActivity** — operational developments
- **RecognitionActivity** — awards, achievements
- **RegulatoryActivity** — permits, regulatory filings
- **IndustrySectorUpdate** — industry-wide news

## Links

- [API Documentation](https://syracuse.1145.am/docs/)
- [API Schema](https://syracuse.1145.am/api/schema/)
