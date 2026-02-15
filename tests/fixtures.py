"""Shared mock response payloads for tests."""

STORY_FULL = {
    "activity_class": "CorporateFinanceActivity",
    "headline": "Acme Corp acquires Widget Inc for $1B",
    "published_date": "2026-02-14T12:00:00Z",
    "published_by": "Test News",
    "document_extract": "Acme Corp announced the acquisition...",
    "document_url": "https://example.com/article",
    "uri": "https://1145.am/db/12345/Acme_Widget",
    "actors_by_role": {"buyer": ["Acme Corp"], "target": ["Widget Inc"]},
}

STORY_SIMPLE = {
    "activity_class": "PartnershipActivity",
    "uri": "https://1145.am/db/67890/Foo_Bar_Partnership",
    "headline": "Foo partners with Bar on AI initiative",
    "published_date": "2026-02-13T08:00:00Z",
    "published_by": "Tech Daily",
    "document_extract": "Foo and Bar have signed an agreement to collaborate on AI.",
    "document_url": "https://example.com/foo-bar",
}

STORIES_PAGE = {
    "count": 42,
    "next": "https://syracuse.1145.am/api/v1/stories/?page=2",
    "previous": None,
    "results": [STORY_FULL, STORY_SIMPLE],
}

STORIES_PAGE_LAST = {
    "count": 42,
    "next": None,
    "previous": "https://syracuse.1145.am/api/v1/stories/?page=1",
    "results": [STORY_FULL],
}

INDUSTRY_CLUSTER = {
    "uri": "https://1145.am/db/industry/476_high_tech",
    "representation": ["", "high-tech", "technology"],
    "representative_doc": ["High-Tech", "High Tech", "Technology"],
    "topic_id": 476,
    "child_left": None,
    "child_right": None,
    "parent_left": None,
    "parent_right": None,
    "child_left_api_url": None,
    "child_right_api_url": None,
    "parent_left_api_url": None,
    "parent_right_api_url": None,
}

INDUSTRY_CLUSTERS_PAGE = {
    "count": 5996,
    "next": "https://syracuse.1145.am/api/v1/industry-clusters/?page=2",
    "previous": None,
    "results": [INDUSTRY_CLUSTER],
}

GEONAME = {
    "geonames_id": 5128581,
    "uri": "https://1145.am/db/geonames_location/5128581",
    "name": "New York City",
    "geonames_url": "https://sws.geonames.org/5128581",
    "country_code": "US",
    "admin1_code": "NY",
    "country_list": None,
    "location_api_urls": [],
}

GEONAMES_PAGE = {
    "count": 37736,
    "next": "https://syracuse.1145.am/api/v1/geonames/?page=2",
    "previous": None,
    "results": [GEONAME],
}

LOCATION_GROUP = {
    "id": "Americas",
    "parent": None,
    "name": "Americas",
    "children": [
        "https://syracuse.1145.am/api/v1/location-groups/Northern%20America/",
        "https://syracuse.1145.am/api/v1/location-groups/Latin%20America%20and%20the%20Caribbean/",
    ],
}

LOCATION_GROUPS_LIST = [
    LOCATION_GROUP,
    {
        "id": "Asia",
        "parent": None,
        "name": "Asia",
        "children": ["https://syracuse.1145.am/api/v1/location-groups/Eastern%20Asia/"],
    },
]
