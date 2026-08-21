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
- [x] Implement a generic public website collector
- [x] Implement Viva Fresh public online collector foundation
- [x] Add shared source-record model
- [x] Add Facebook public-source adapter contract
- [x] Add request timeout/error propagation
- [ ] Verify live source extraction and save real observations
- [ ] Implement additional supermarket collectors one at a time
- [ ] Add production-grade throttling/retries

## Phase 3 — Product and price extraction
- [x] Implement EUR price extraction helper
- [x] Add product-price candidate extraction
- [x] Add parser tests
- [x] Define product-name normalization
- [x] Define conservative product matching
- [ ] Extract products from real permitted supermarket HTML/API data
- [ ] Extract offer dates from real source material
- [ ] Handle discounted/promotional prices from real source material
- [ ] Match equivalent real products across supermarkets

## Phase 4 — Storage and history
- [x] Define PostgreSQL-compatible schema
- [x] Implement local SQLite persistence for development
- [x] Create tables for supermarkets/products/observations/runs
- [ ] Connect collector output to persistence end-to-end
- [ ] Store historical price snapshots
- [ ] Add production database migrations

## Phase 5 — Comparison engine
- [x] Add unit-price calculation helper
- [x] Add price difference/percentage helpers
- [x] Add cross-supermarket matching helper
- [x] Add comparison service
- [ ] Compare real equivalent products across supermarkets
- [ ] Calculate lowest available real price from database
- [ ] Handle missing products safely in production flow

## Phase 6 — API
- [x] Create API application foundation
- [x] Add health endpoint
- [x] Add initial supermarkets endpoint
- [x] Add initial comparisons endpoint
- [x] Add API smoke tests
- [ ] Connect endpoints to database
- [ ] Add real product/price endpoints
- [ ] Add validation and production error responses

## Phase 7 — Frontend
- [x] Create Next.js frontend foundation
- [x] Add initial comparison UI
- [x] Add supermarket search/filter UI
- [x] Add lowest-price indication to comparison prototype
- [ ] Replace demo data with API data
- [ ] Product search
- [ ] Supermarket selector
- [ ] Price history view
- [ ] Source links and collection timestamps
- [ ] Responsive production UI

## Phase 8 — Automation and deployment
- [ ] Add scheduled collection jobs
- [ ] Add logging and monitoring
- [ ] Add production environment configuration
- [ ] Keep secrets out of Git
- [ ] Deploy API
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

**Step 21: Connect a real permitted source to persistence, verify extracted observations, then connect the API/frontend to real database data.**
