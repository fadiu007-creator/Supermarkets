"""Facebook source adapter placeholder.

This module intentionally does not automate a logged-in account or bypass
Facebook access controls. It accepts content obtained through an explicitly
permitted public interface and converts it into SourceRecord objects.
"""
from datetime import datetime, timezone
from collectors.source_record import SourceRecord


def from_public_content(supermarket_id: str, page_url: str, content: str) -> SourceRecord:
    return SourceRecord(
        supermarket_id=supermarket_id,
        source_type="facebook_public",
        source_url=page_url,
        collected_at=datetime.now(timezone.utc).isoformat(),
        content=content,
    )
