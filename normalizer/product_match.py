import re
import unicodedata


def normalize_name(name: str) -> str:
    value = unicodedata.normalize("NFKC", name).lower()
    value = value.replace("×", "x")
    value = re.sub(r"[^\w\s.]", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def comparable_key(name: str, brand: str | None = None, quantity_value: str | None = None, quantity_unit: str | None = None) -> str:
    parts = [normalize_name(name)]
    if brand:
        parts.append(normalize_name(brand))
    if quantity_value and quantity_unit:
        parts.append(f"{quantity_value}{normalize_name(quantity_unit)}")
    return "|".join(parts)


def same_product(a: dict, b: dict) -> bool:
    """Conservative match: normalized identity plus compatible quantity/unit."""
    return comparable_key(a.get("name", ""), a.get("brand"), a.get("quantity_value"), a.get("quantity_unit")) == comparable_key(b.get("name", ""), b.get("brand"), b.get("quantity_value"), b.get("quantity_unit"))
