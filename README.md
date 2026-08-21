# Kosovo Supermarket Price Tracker

A project for collecting publicly available supermarket offer and product information from selected Kosovo supermarket pages and comparing prices across stores.

## Goals

- Track selected Kosovo supermarkets and their public offers.
- Collect product names, prices, currencies, units, dates, source URLs, and supermarket names.
- Normalize products so equivalent items can be compared.
- Compare prices across supermarkets.
- Keep historical snapshots so price changes can be observed over time.
- Provide a simple API and frontend once the data pipeline is stable.

## Data sources

The initial target is publicly accessible content from supermarket pages, including Facebook pages where appropriate. The implementation must respect applicable laws, platform terms, access controls, rate limits, and access restrictions. It must not bypass login requirements, CAPTCHAs, technical protections, or private content.

Potential supermarkets will be defined in configuration rather than hard-coded throughout the scraper.

## Planned architecture

```text
Public supermarket sources
        |
        v
     Collectors
        |
        v
  Extraction / parsing
        |
        v
 Product normalization
        |
        v
  Price database
        |
        +---- historical snapshots
        |
        v
 Comparison API
        |
        v
   Web frontend
```

## Project workflow

This repository is designed to be developed incrementally.

- `TODO.md` contains the active work queue.
- `FINISHED.md` records completed milestones.
- Each completed milestone should update both files.
- Work should be tested before being marked finished.

## Development principles

1. Prefer official/publicly accessible data sources and APIs when available.
2. Do not bypass authentication, CAPTCHAs, rate limits, or access controls.
3. Store source URLs and collection timestamps with extracted prices.
4. Keep raw source data separate from normalized comparison data.
5. Make source collectors replaceable so a source can change without rewriting the comparison system.
6. Test extraction against saved fixtures before running collectors against live sources.
7. Never commit credentials, cookies, access tokens, or personal data.
8. Keep supermarket-specific configuration separate from application logic.

## Definition of done

The project is finished when configured supermarket sources can be collected reliably, products and prices are normalized, historical data is stored, price comparisons are available through the API/frontend, tests and error handling are in place, and the documentation explains how to run and maintain the system.
