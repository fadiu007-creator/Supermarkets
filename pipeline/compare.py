from decimal import Decimal


def compare_prices(rows):
    """Return normalized comparison rows ordered by effective price.

    Each row must contain product_id, supermarket_id and price. Prices are
    converted to Decimal to avoid floating-point money errors.
    """
    grouped = {}
    for row in rows:
        item = dict(row)
        item["price"] = Decimal(str(item["price"]))
        grouped.setdefault(item["product_id"], []).append(item)

    result = []
    for product_id, items in grouped.items():
        items.sort(key=lambda x: x["price"])
        lowest = items[0]["price"]
        for item in items:
            item["difference"] = item["price"] - lowest
            item["is_lowest"] = item["price"] == lowest
        result.append({"product_id": product_id, "prices": items})
    return result
