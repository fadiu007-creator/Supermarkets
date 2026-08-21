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
- Added initial EUR price parsing and normalization tests.
- Added PostgreSQL-compatible schema for supermarkets, products, observations, and collection runs.
- Added unit-price and price-difference calculations and tests.

### Steps 11–14 — Working application foundations
- Added a permitted public HTTP collector and Viva Fresh website runner.
- Added shared source-record model.
- Added local SQLite persistence implementation for development.
- Added a Facebook public-source adapter that accepts content from an explicitly permitted public interface without bypassing access controls.
- Added initial FastAPI application, health endpoint, supermarket/comparison endpoints, dependencies, and API smoke tests.
- Added initial Next.js frontend package, root layout, and comparison landing page.
- Updated TODO to identify the remaining real-data integration work.

## Current state

The repository now contains collection, parsing, normalization, persistence, comparison, API, and frontend foundations. Real supermarket observations still need to be collected through verified permitted sources and wired through the database/API before the application can be considered live production software.

## Verification

Repository changes are considered finished only when successfully committed and recorded here.
