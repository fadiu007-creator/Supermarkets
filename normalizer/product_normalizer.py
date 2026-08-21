"""Conservative product normalization helpers."""

import re
import unicodedata


def normalize_product_name(name: str) -> str:
    """Normalize whitespace/case/Unicode without claiming product equivalence."""
    value = unicodedata.normalize("NFKC", name).strip().casefold()
    value = re.sub(r"\s+", " ", value)
    return value


def normalize_quantity(value: str, unit: str) -> tuple[float, str]:
    """Normalize common mass/volume units to kg/l and pieces to pcs."""
    amount = float(value.replace(",", "."))
    unit = unit.strip().casefold()
    conversions = {
        "g": (amount / 1000, "kg"),
        "kg": (amount, "kg"),
        "ml": (amount / 1000, "l"),
        "l": (amount, "l"),
        "pcs": (amount, "pcs"),
        "pc": (amount, "pcs"),
        "copë": (amount, "pcs"),
    }
    if unit not in conversions:
        raise ValueError(f"Unsupported quantity unit: {unit}")
    return conversions[unit]
