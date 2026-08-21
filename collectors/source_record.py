from dataclasses import dataclass

@dataclass
class SourceRecord:
    supermarket_id: str
    source_type: str
    source_url: str
    collected_at: str
    content: str
