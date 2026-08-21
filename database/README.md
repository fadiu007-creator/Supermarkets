# Database

The database layer stores normalized supermarkets, products, price observations, and collection runs.

The database schema is defined in `schema.sql`. Production implementation will use migrations and parameterized queries. Monetary values should be stored as fixed-precision decimals.
