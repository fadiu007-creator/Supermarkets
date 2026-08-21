# Facebook scraper integration

The project now has an adapter for `kevinzg/facebook-scraper`.

## Local smoke test

```bash
python -m pip install -r requirements.txt
python collectors/test_kipper_public.py
```

The test uses `kipperkosova` in public-page mode and does not pass Facebook credentials or browser cookies.

## Important

The repository must not be used to bypass Facebook authentication, CAPTCHAs, rate limits, access controls, or other technical restrictions. A successful test must be verified against the current Facebook behavior before we treat the collector as production-ready.

## Next verification

1. Run the Kipper smoke test in an environment with outbound internet access.
2. Record whether posts are actually returned.
3. If posts are returned, feed their text into the existing price parser.
4. Persist real observations in the database.
5. Repeat for Viva Fresh, Meridian Express, and ETC only after each page is individually verified.
