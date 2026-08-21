"""SQLite persistence for local development; schema is PostgreSQL-compatible."""
import sqlite3
from pathlib import Path


def connect(path: str = "data/supermarkets.db"):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(path)


def init_db(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS supermarkets (
      id TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      enabled INTEGER NOT NULL DEFAULT 1
    );
    CREATE TABLE IF NOT EXISTS products (
      id TEXT PRIMARY KEY,
      canonical_name TEXT NOT NULL,
      brand TEXT,
      quantity_value REAL,
      quantity_unit TEXT,
      barcode TEXT
    );
    CREATE TABLE IF NOT EXISTS price_observations (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      product_id TEXT,
      supermarket_id TEXT NOT NULL,
      source_type TEXT NOT NULL,
      source_url TEXT NOT NULL,
      collected_at TEXT NOT NULL,
      price TEXT NOT NULL,
      currency TEXT NOT NULL DEFAULT 'EUR',
      regular_price TEXT,
      sale_price TEXT,
      offer_text TEXT,
      raw_product_name TEXT,
      raw_price_text TEXT
    );
    CREATE TABLE IF NOT EXISTS collection_runs (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      supermarket_id TEXT NOT NULL,
      source_url TEXT NOT NULL,
      started_at TEXT NOT NULL,
      finished_at TEXT,
      status TEXT NOT NULL,
      error TEXT
    );
    """)
    conn.commit()
