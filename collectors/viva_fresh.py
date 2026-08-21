"""Viva Fresh online-shop collector.

The official Viva Fresh online shop exposes product/catalog pages publicly.
This collector is intentionally conservative: it fetches public HTML only and
leaves JavaScript/API discovery for a later, explicitly permitted integration.
"""
from collectors.http_public import collect_public_page

VIVA_ONLINE = "https://online.vivafresh.shop/"


def collect() -> object:
    return collect_public_page("viva-fresh", VIVA_ONLINE)
