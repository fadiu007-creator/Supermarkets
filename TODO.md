# TODO

Active development roadmap for the Kosovo Supermarket Price Tracker.

## Phase 1 — Foundation

- [x] Create project README
- [x] Create project status/completion log
- [x] Define repository structure
- [x] Define supported supermarket configuration format
- [x] Choose initial supermarket targets and public source candidates
- [x] Define common product/price data model

## Phase 2 — Data collection

- [x] Research permitted public data-source strategy
- [x] Implement a generic collector interface
- [ ] Implement first real supermarket collector
- [ ] Implement additional supermarket collectors one at a time
- [ ] Add request throttling, retries, timeouts, and error handling
- [x] Define collection timestamp/source provenance fields
- [x] Define separation of raw source data and normalized data

## Phase 3 — Product and price extraction

- [x] Implement initial EUR price extraction helper
- [x] Add parser tests
- [x] Define product-name normalization
- [x] Define quantity/unit normalization
- [ ] Extract products from a real permitted supermarket source
- [ ] Extract offer dates from real source material
- [ ] Handle discounted/promotional prices from real source material
- [ ] Match equivalent products across supermarkets

## Phase 4 — Storage and history

- [x] Choose PostgreSQL-compatible relational model
- [x] Create schema for supermarkets
- [x] Create schema for products
- [x] Create schema for price observations
- [x] Create schema for collection runs/errors
- [ ] Implement database persistence
- [ ] Store historical price snapshots
- [ ] Add database migrations

## Phase 5 — Comparison engine

- [x] Add unit-price calculation helper
- [x] Add price difference/percentage helpers
- [x] Add comparison tests
- [ ] Compare real equivalent products across supermarkets
- [ ] Calculate lowest available real price
- [ ] Handle missing products safely in production flow

## Phase 6 — API

- [ ] Create API application
- [ ] Endpoint for supermarkets
- [ ] Endpoint for products
- [ ] Endpoint for current prices
- [ ] Endpoint for price comparisons
- [ ] Endpoint for historical prices
- [ ] Add validation and error responses
- [ ] Add API tests

## Phase 7 — Frontend

- [ ] Create web application
- [ ] Supermarket selector
- [ ] Product search
- [ ] Price comparison table
- [ ] Lowest-price highlighting
- [ ] Product/unit information
- [ ] Price history view
- [ ] Source links and collection timestamps
- [ ] Responsive mobile UI

## Phase 8 — Automation and deployment

- [ ] Add scheduled collection jobs
- [ ] Add logging and monitoring
- [ ] Add production environment configuration
- [ ] Keep secrets out of Git
- [ ] Deploy backend/API
- [ ] Deploy frontend
- [ ] Verify production collection and comparison flow

## Phase 9 — Quality and completion

- [ ] End-to-end test from source collection to frontend comparison
- [ ] Test scraper failures and unavailable sources
- [ ] Review platform terms and applicable requirements for every source
- [ ] Document setup and maintenance
- [ ] Document how to add a new supermarket
- [ ] Document how to resume development from TODO.md
- [ ] Final production verification

## Current task

**Step 11: Implement the first real supermarket collector against a permitted public source.**
