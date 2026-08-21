# Product and Price Data Model

## Purpose

Define the canonical representation used by collectors, parsers, storage, comparison, API, and frontend components.

## Product

A product represents a normalized item that can be compared between supermarkets.

Required fields:

- `product_id`: stable internal identifier.
- `canonical_name`: normalized product name.
- `brand`: normalized brand when identifiable.
- `category`: optional normalized category.
- `quantity_value`: numeric quantity when available.
- `quantity_unit`: normalized unit such as `g`, `kg`, `ml`, `l`, `pcs`.
- `barcode`: optional GTIN/EAN when available.

Source-specific names and metadata must not overwrite the canonical product without an explicit normalization/matching decision.

## Price observation

Every collected price is an observation rather than a property permanently attached to a product.

Required fields:

- `observation_id`
- `product_id` (nullable until matching is complete)
- `supermarket_id`
- `source_type`
- `source_url`
- `collected_at`
- `price`
- `currency`

Offer-related fields:

- `regular_price`: optional non-discounted price.
- `sale_price`: optional promotional price.
- `discount_percent`: optional calculated/declared discount.
- `offer_start`: optional date/time.
- `offer_end`: optional date/time.
- `offer_text`: optional original promotional wording.

Extraction fields:

- `raw_product_name`
- `raw_price_text`
- `raw_quantity_text`
- `confidence`
- `raw_record_id` or raw-data reference when available.

## Normalization rules

- Monetary values use decimal arithmetic, not floating-point arithmetic.
- Default currency is EUR unless the source explicitly states another currency.
- Preserve the original price text for auditing.
- Normalize decimal separators and thousands separators according to the source locale.
- Normalize units before calculating unit prices.
- Never assume two similarly named products are equivalent solely from text similarity.
- Product matching should consider brand, product type, quantity, unit, barcode, and relevant variant information.

## Comparison price

For equivalent products with quantities expressed in compatible units:

`unit_price = effective_price / normalized_quantity`

The comparison engine should expose both the advertised/effective package price and normalized unit price where possible.

## Data provenance

Every price shown to a user must be traceable to its supermarket, source type, source URL, collection timestamp, and raw observation. This is required for debugging and historical auditing.

## Example

```json
{
  "product_id": "milk-vita-1l",
  "canonical_name": "Vita UHT Milk",
  "brand": "Vita",
  "quantity_value": 1,
  "quantity_unit": "l",
  "supermarket_id": "example-store",
  "source_type": "website",
  "source_url": "https://example.com/product",
  "collected_at": "2026-08-21T12:00:00Z",
  "price": "1.19",
  "currency": "EUR",
  "regular_price": "1.35",
  "sale_price": "1.19"
}
```
