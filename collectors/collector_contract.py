"""Common collector contracts for permitted public supermarket sources."""

from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Protocol

SourceType = Literal["website", "facebook", "api", "flyer", "other"]


@dataclass(frozen=True)
class SourceRecord:
    supermarket_id: str
    source_type: SourceType
    source_url: str
    collected_at: datetime
    external_id: str | None
    title: str | None
    text: str | None
    media_url: str | None


class Collector(Protocol):
    def collect(self) -> list[SourceRecord]:
        """Return records from an allowed public source."""
        ...
