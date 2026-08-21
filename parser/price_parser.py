"""Deterministic helpers for extracting EUR prices from source text."""

from decimal import Decimal, InvalidOperation
import re

PRICE_RE = re.compile(r"(?<!\d)(\d{1,4}(?:[.,]\d{1,2})?)(?:\s*)(?:€|EUR)\b", re.IGNORECASE)


def parse_eur_prices(text: str) -> list[Decimal]:
    """Extract explicit EUR prices while preserving decimal precision."""
    values: list[Decimal] = []
    for match in PRICE_RE.finditer(text):
        raw = match.group(1).replace(",", ".")
        try:
            values.append(Decimal(raw))
        except InvalidOperation:
            continue
    return values
