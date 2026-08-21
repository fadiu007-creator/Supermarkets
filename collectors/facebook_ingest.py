"""Ingest Facebook page content supplied by a permitted public-access mechanism.

The collector deliberately accepts already-obtained page content. It does not
log in to Facebook, use stored cookies, bypass CAPTCHAs, or evade access controls.
"""
from dataclasses import dataclass
from datetime import datetime, timezone
import re

PRICE_RE = re.compile(r"(?<!\d)(\d{1,4}(?:[.,]\d{1,2})?)\s*(?:€|EUR)(?!\w)", re.I)

@dataclass
class FacebookPost:
    supermarket_id: str
    page_url: str
    post_url: str | None
    published_at: str | None
    text: str
    prices: list[str]


def parse_public_post(supermarket_id: str, page_url: str, text: str, post_url: str | None = None, published_at: str | None = None) -> FacebookPost:
    prices = [m.group(1).replace(',', '.') for m in PRICE_RE.finditer(text)]
    return FacebookPost(supermarket_id, page_url, post_url, published_at, text, prices)


def collected_at() -> str:
    return datetime.now(timezone.utc).isoformat()
