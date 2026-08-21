import re
from decimal import Decimal
from typing import Optional

PRICE_RE = re.compile(r"(?P<value>\d{1,4}(?:[.,]\d{1,2})?)\s*(?:€|EUR)", re.I)


def parse_eur_price(text: str) -> Optional[Decimal]:
    match = PRICE_RE.search(text)
    if not match:
        return None
    return Decimal(match.group("value").replace(",", "."))


def extract_candidate_products(text: str):
    """Return simple text lines containing an EUR price.

    This intentionally keeps extraction conservative; product matching happens
    later in the normalization layer.
    """
    candidates = []
    for line in text.splitlines():
        price = parse_eur_price(line)
        if price is not None:
            name = re.sub(PRICE_RE, "", line).strip(" -–—:|")
            if name:
                candidates.append({"raw_product_name": name, "price": str(price), "currency": "EUR"})
    return candidates
