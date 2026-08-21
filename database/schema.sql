-- Initial relational model. PostgreSQL-compatible.

CREATE TABLE supermarkets (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    country_code TEXT NOT NULL DEFAULT 'XK',
    enabled BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE products (
    id TEXT PRIMARY KEY,
    canonical_name TEXT NOT NULL,
    brand TEXT,
    category TEXT,
    quantity_value NUMERIC,
    quantity_unit TEXT,
    barcode TEXT
);

CREATE TABLE price_observations (
    id BIGSERIAL PRIMARY KEY,
    product_id TEXT REFERENCES products(id),
    supermarket_id TEXT NOT NULL REFERENCES supermarkets(id),
    source_type TEXT NOT NULL,
    source_url TEXT NOT NULL,
    collected_at TIMESTAMPTZ NOT NULL,
    price NUMERIC(12,2) NOT NULL,
    currency TEXT NOT NULL DEFAULT 'EUR',
    regular_price NUMERIC(12,2),
    sale_price NUMERIC(12,2),
    discount_percent NUMERIC(6,2),
    offer_start TIMESTAMPTZ,
    offer_end TIMESTAMPTZ,
    offer_text TEXT,
    raw_product_name TEXT,
    raw_price_text TEXT,
    raw_quantity_text TEXT,
    confidence NUMERIC(5,4),
    raw_record_id TEXT
);

CREATE TABLE collection_runs (
    id BIGSERIAL PRIMARY KEY,
    supermarket_id TEXT NOT NULL REFERENCES supermarkets(id),
    source_type TEXT NOT NULL,
    source_url TEXT NOT NULL,
    started_at TIMESTAMPTZ NOT NULL,
    finished_at TIMESTAMPTZ,
    status TEXT NOT NULL,
    records_collected INTEGER NOT NULL DEFAULT 0,
    error_message TEXT
);

CREATE INDEX price_observations_product_idx ON price_observations(product_id);
CREATE INDEX price_observations_supermarket_idx ON price_observations(supermarket_id);
CREATE INDEX price_observations_collected_idx ON price_observations(collected_at);
