# Collection Policy

This project is designed around permitted public data collection.

## Requirements

- Collect only information that is publicly accessible through an allowed source/interface.
- Prefer official websites, online stores, flyers, and official APIs where available.
- Do not bypass authentication, CAPTCHAs, paywalls, access controls, or technical protections.
- Respect applicable platform terms, rate limits, and access restrictions.
- Do not store passwords, session cookies, access tokens, or other credentials in the repository.
- Do not collect unnecessary personal information from social-media content.
- Keep source URLs and timestamps for provenance.

## Failure behavior

If a source requires a login or blocks automated access, the collector should record the source as unavailable and continue rather than attempting to circumvent the restriction.
