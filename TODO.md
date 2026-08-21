# TODO

Active development roadmap for the Kosovo Supermarket Price Tracker.

## Phase 1 — Foundation

- [x] Create project README
- [ ] Create project status/completion log
- [ ] Define repository structure
- [ ] Define supported supermarket configuration format
- [ ] Choose initial supermarkets and public source URLs
- [ ] Define common product/price data model

## Phase 2 — Data collection

- [ ] Research permitted public data sources for each supermarket
- [ ] Implement a generic collector interface
- [ ] Implement first supermarket collector
- [ ] Implement additional supermarket collectors one at a time
- [ ] Add request throttling, retries, timeouts, and error handling
- [ ] Store collection timestamp and source URL for every observation
- [ ] Keep raw collected data separate from normalized data

## Phase 3 — Product and price extraction

- [ ] Extract product names
- [ ] Extract prices and currencies
- [ ] Extract units/weights/quantities where available
- [ ] Extract offer dates where available
- [ ] Handle discounted/promotional prices explicitly
- [ ] Build parser test fixtures from permitted public examples
- [ ] Normalize product names, units, and quantities
- [ ] Match equivalent products across supermarkets

## Phase 4 — Storage and history

- [ ] Choose database
- [ ] Create schema for supermarkets
- [ ] Create schema for products
- [ ] Create schema for price observations
- [ ] Create schema for collection runs/errors
- [ ] Store historical price snapshots
- [ ] Add database migrations

## Phase 5 — Comparison engine

- [ ] Compare equivalent products across supermarkets
- [ ] Calculate lowest available price
- [ ] Calculate price differences and percentages
- [ ] Support unit-price comparisons where quantities differ
- [ ] Handle missing products safely
- [ ] Add comparison tests

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
- [ ] Move completed work into FINISHED.md
- [ ] Final production verification

## Current task

**Step 2: Create the project completion/status log (`FINISHED.md`).**
