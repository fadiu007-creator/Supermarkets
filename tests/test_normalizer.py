from decimal import Decimal

import pytest

from normalizer.comparison import percent_difference, unit_price
from normalizer.product_normalizer import normalize_product_name, normalize_quantity


def test_product_name_normalization():
    assert normalize_product_name("  VITA   Milk ") == "vita milk"


def test_quantity_normalization():
    assert normalize_quantity("500", "g") == (0.5, "kg")
    assert normalize_quantity("1", "L") == (1.0, "l")


def test_unit_price():
    assert unit_price(Decimal("2.00"), Decimal("0.5")) == Decimal("4")


def test_percent_difference_zero_reference():
    assert percent_difference(Decimal("2"), Decimal("0")) is None


def test_invalid_quantity():
    with pytest.raises(ValueError):
        normalize_quantity("1", "unknown")
