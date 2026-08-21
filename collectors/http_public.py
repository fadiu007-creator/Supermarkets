"""Small HTTP collector for permitted public web pages."""
from dataclasses import dataclass
from datetime import datetime, timezone
import requests


@dataclass
class SourceRecord:
    supermarket_id: str
    source_type: str
    source_url: str
    collected_at: str
    content: str


def collect_public_page(supermarket_id: str, source_url: str, timeout: int = 20) -> SourceRecord:
    response = requests.get(
        source_url,
        timeout=timeout,
        headers={"User-Agent": "KosovoSupermarketPriceTracker/0.1 (+public-data-research)"},
    )
    response.raise_for_status()
    return SourceRecord(
        supermarket_id=supermarket_id,
        source_type="website",
        source_url=source_url,
        collected_at=datetime.now(timezone.utc).isoformat(),
        content=response.text,
    )
