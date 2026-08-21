"""Price comparison calculations."""

from decimal import Decimal


def unit_price(price: Decimal, quantity: Decimal) -> Decimal:
    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")
    return price / quantity


def price_difference(a: Decimal, b: Decimal) -> Decimal:
    return a - b


def percent_difference(a: Decimal, b: Decimal) -> Decimal | None:
    """Return percentage difference from b to a; None when b is zero."""
    if b == 0:
        return None
    return ((a - b) / b) * Decimal("100")
