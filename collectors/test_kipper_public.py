"""Manual smoke test for Kipper's public Facebook page.

Run locally after installing the dependency:
    pip install facebook-scraper
    python collectors/test_kipper_public.py

This test intentionally makes no attempt to supply credentials or cookies.
"""
from facebook_scraper_adapter import get_public_posts


if __name__ == "__main__":
    posts = get_public_posts("kipperkosova", pages=1)
    count = 0
    for post in posts:
        count += 1
        print({
            "post_id": post.get("post_id"),
            "time": post.get("time"),
            "post_url": post.get("post_url"),
            "text": post.get("text", "")[:1000],
        })
    print(f"Retrieved {count} public posts")
