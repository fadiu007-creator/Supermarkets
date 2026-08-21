# Finished Work

Completed milestones for the Kosovo Supermarket Price Tracker.

## Completed

### Steps 1–5 — Foundation

- Created `README.md`.
- Created `TODO.md` and `FINISHED.md`.
- Defined repository structure and responsibilities.
- Defined supermarket/source configuration format.
- Selected five initial Kosovo supermarket targets and documented source candidates.

### Step 6 — Common product and price data model

- Created `docs/PRODUCT_PRICE_MODEL.md`.
- Defined canonical products, price observations, promotions, quantities, provenance, and unit-price rules.
- Chose decimal monetary representation and conservative product matching rules.

### Step 7 — Public-source collection strategy

- Created `docs/SOURCE_COLLECTION.md` and `docs/COLLECTION_POLICY.md`.
- Defined source priority, provenance, rate limiting, failure handling, and safe public-access requirements.
- Facebook is supported only where permitted public access is available; no authentication/CAPTCHA/access-control bypass is planned.

### Step 8 — Generic collection and extraction foundation

- Added `collectors/collector_contract.py` with a reusable source-record contract.
- Added an initial deterministic EUR price parser at `parser/price_parser.py`.
- Added parser tests.

### Step 9 — Normalization and storage foundation

- Added conservative product-name and quantity/unit normalization helpers.
- Added a PostgreSQL-compatible initial schema in `database/schema.sql` for supermarkets, products, price observations, and collection runs.
- Added normalization tests.

### Step 10 — Comparison foundation

- Added unit-price, price-difference, and percentage-difference calculation helpers.
- Added comparison tests.
- Defined the next implementation target as the first real permitted supermarket collector.

## Verification

Each milestone is marked finished only after the corresponding repository changes are created successfully through GitHub.

## Current state

The project has its architecture, configuration, data contract, collection policy, parsing/normalization foundation, database schema, and comparison calculations. The next task is to implement the **first real supermarket collector** against a permitted public source and test the complete source-to-price pipeline.
