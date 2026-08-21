# Project Structure

The repository is organized by responsibility so collectors, parsing, storage, comparison, API, and frontend code can evolve independently.

```text
.
├── README.md
├── TODO.md
├── FINISHED.md
├── config/
│   ├── supermarkets.example.json
│   └── README.md
├── collectors/
│   └── README.md
├── parser/
│   └── README.md
├── normalizer/
│   └── README.md
├── database/
│   └── README.md
├── api/
│   └── README.md
├── frontend/
│   └── README.md
├── tests/
│   ├── fixtures/
│   │   └── README.md
│   └── README.md
└── docs/
    └── PROJECT_STRUCTURE.md
```

## Responsibilities

### `config/`

Supermarket definitions, public source URLs, collector selection, and non-secret runtime settings. Secrets must never be stored here.

### `collectors/`

Source-specific collection adapters. A collector retrieves publicly accessible source material and produces raw observations without applying product matching rules.

### `parser/`

Extraction of product names, prices, currencies, quantities, units, promotion dates, and other fields from raw source material.

### `normalizer/`

Canonical product naming, quantity/unit normalization, and matching equivalent products across supermarkets.

### `database/`

Database schema, migrations, persistence code, and historical price snapshots.

### `api/`

Backend endpoints used by the frontend and other clients.

### `frontend/`

The user-facing price comparison application.

### `tests/`

Unit, parser, collector, integration, and end-to-end tests. `tests/fixtures/` contains sanitized/permitted sample source material used for deterministic tests.

### `docs/`

Architecture and maintenance documentation that is too detailed for the README.

## Data flow

```text
source -> collector -> raw observation -> parser -> normalized product/price -> database -> comparison API -> frontend
```

Collectors must not contain frontend or database-specific logic. This keeps a source-specific implementation replaceable when a supermarket changes its public website or publishing format.
