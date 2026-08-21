# Finished Work

Completed milestones for the Kosovo Supermarket Price Tracker.

## Completed

### Steps 1–5 — Foundation
- Created README, TODO, and FINISHED tracking files.
- Defined repository structure and supermarket/source configuration.
- Selected initial Kosovo supermarket targets and documented source candidates.

### Steps 6–10 — Data architecture
- Defined canonical product and price observation model.
- Defined public-source collection policy and provenance requirements.
- Added EUR price parsing and normalization tests.
- Added PostgreSQL-compatible schema for supermarkets, products, observations, and collection runs.
- Added unit-price and price-difference calculations and tests.

### Steps 11–14 — Application foundations
- Added permitted public HTTP collector and Viva Fresh website runner.
- Added shared source-record model and local SQLite persistence.
- Added Facebook public-source adapter contract without access-control bypass.
- Added FastAPI foundation and API smoke tests.
- Added Next.js frontend foundation.

### Steps 15–20 — Implementation batch
- Added dedicated Viva Fresh online-shop collector pointing at the official public online shop.
- Added product-price candidate extraction for EUR-denominated text.
- Added conservative normalized product matching using name/brand/quantity/unit.
- Added comparison service returning lowest price and price differences.
- Added a first comparison UI with supermarket filtering and lowest-price indication.
- Updated the roadmap to distinguish implemented code from verified live data.

## Important status note

Steps 15–20 are implemented as application foundations/prototypes, but **real supermarket observations have not been falsely marked as complete**. The next step is to run/verify a permitted live source, persist real observations, and then wire the API and frontend to those observations.

## Current state

The repository contains collection, Facebook-source integration contract, parsing, normalization, persistence, comparison, API, and frontend foundations. It is not yet a deployed production price tracker.

## Verification

Repository changes are considered finished only when successfully committed and recorded here.
