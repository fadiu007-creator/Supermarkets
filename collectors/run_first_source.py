"""CLI for collecting the first permitted supermarket website source."""
import json
from pathlib import Path
from http_public import collect_public_page


CONFIG = Path(__file__).parents[1] / "config" / "supermarkets.example.json"


def main() -> None:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    target = next(s for s in config["supermarkets"] if s["id"] == "viva-fresh")
    source = next(s for s in target["sources"] if s["type"] == "website")
    record = collect_public_page(target["id"], source["url"])
    print(f"Collected {len(record.content)} bytes from {record.source_url} at {record.collected_at}")


if __name__ == "__main__":
    main()
