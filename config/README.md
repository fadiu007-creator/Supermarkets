# Configuration

Supermarket-specific settings belong in this directory instead of being hard-coded into collectors.

## Rules

- Do not store passwords, session cookies, access tokens, API keys, or other secrets here.
- Keep public source URLs explicit and reviewable.
- Give each supermarket a stable machine-readable ID.
- Select a collector by name so the collector implementation can change independently of configuration.
- Mark a source as `enabled: false` when it is unavailable or has not yet been reviewed for collection.
- Prefer official websites, online brochures, and official APIs/feeds when available.

`supermarkets.example.json` is a committed example/configuration baseline. Production deployments may use an environment-specific configuration file that is not committed.
