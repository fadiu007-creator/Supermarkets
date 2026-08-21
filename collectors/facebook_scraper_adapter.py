"""Adapter for the kevinzg/facebook-scraper package.

This uses the package's public-page mode. It does not provide Facebook
credentials or browser cookies and must not be used to bypass access controls.
"""
from __future__ import annotations

from typing import Any, Iterator


def get_public_posts(page_name: str, pages: int = 1) -> Iterator[dict[str, Any]]:
    try:
        from facebook_scraper import get_posts
    except ImportError as exc:
        raise RuntimeError(
            "facebook-scraper is not installed. Install it with: pip install facebook-scraper"
        ) from exc

    yield from get_posts(page_name, pages=pages)
