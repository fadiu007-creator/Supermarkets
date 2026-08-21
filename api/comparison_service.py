from decimal import Decimal


def compare_prices(observations):
    """Return lowest price and ordered supermarket observations."""
    rows = sorted(observations, key=lambda x: Decimal(str(x["price"])))
    if not rows:
        return {"items": [], "lowest": None}
    lowest = Decimal(str(rows[0]["price"]))
    items = []
    for row in rows:
        price = Decimal(str(row["price"]))
        items.append({**row, "difference": str(price - lowest), "difference_percent": str(((price - lowest) / lowest * 100).quantize(Decimal("0.01"))) if lowest else None})
    return {"items": items, "lowest": items[0]}
