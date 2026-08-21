# Source Collection Strategy

## Scope

Collectors may retrieve publicly accessible supermarket offer/product information through permitted sources. The project does not bypass authentication, CAPTCHAs, access controls, robots/access restrictions, rate limits, or other technical protections.

## Source priority

1. Official supermarket website or official online store.
2. Official public promotional/leaflet material.
3. Official public social-media content where access is permitted and technically available.

Facebook is therefore a supported source type, but the collector must fail gracefully if content is unavailable without login or if platform restrictions prevent collection.

## Generic collector contract

Each collector should return normalized `SourceRecord` objects containing:

- source URL
- source type
- supermarket ID
- collected timestamp
- source item/post identifier when available
- raw text/content reference
- media reference when permitted

Collectors should not contain product-matching logic.

## Reliability

- Use conservative request rates.
- Configure connection and read timeouts.
- Retry only transient failures with bounded backoff.
- Record HTTP status/error information without storing credentials or sensitive data.
- Make collection idempotent when possible.
- Save raw permitted source data/fixtures separately from normalized database records.

## Facebook-specific design

The first implementation should use permitted public-access mechanisms rather than attempting to automate a logged-in personal account. If a page cannot be collected through a permitted public interface, mark that source unavailable and continue with official websites or other permitted sources.

## Five initial targets

- Viva Fresh Store
- Kipper Market Kosova
- Meridian Express
- ETC / Elkos Trading Center
- Interex (disabled pending source verification)
