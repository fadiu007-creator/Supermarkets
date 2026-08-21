# Implementation Roadmap

## Step 6 — Data model

Define canonical products and price observations with provenance and unit-price support.

## Step 7 — Source research and collection

Verify permitted sources and implement a generic collector contract. Build the first real collector against the most reliable official source.

## Step 8 — Extraction and normalization

Extract product names, prices, quantities, offers, and dates. Normalize units and names and preserve raw source values.

## Step 9 — Storage and history

Use a relational database with migrations. Store supermarkets, products, price observations, collection runs, and historical snapshots.

## Step 10 — Comparison engine

Match equivalent products, calculate effective and unit prices, identify the cheapest supermarket, and expose differences with provenance.

## Later

API → frontend → scheduling → monitoring → deployment → end-to-end verification.
