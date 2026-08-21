# Facebook Scraper Status

## Kipper public-page test

Tested locally with `facebook-scraper` against `kipperkosova` using public-page mode and `pages=5`.

Result: **0 posts returned**.

The package imports and executes successfully after installing `lxml_html_clean`, so this is no longer a dependency/import failure.

## Conclusion

`facebook-scraper` cannot currently be treated as a working Kipper collector based on this test. We should not label the Facebook pipeline production-ready or fabricate post data.

## Next investigation

- Inspect the library's current Facebook request/response behavior.
- Check whether current Facebook public-page markup/API changes are incompatible with the package.
- Evaluate an official Meta API route or another permitted acquisition method.
- Keep the collector interface independent so the acquisition implementation can be replaced without changing parsing, normalization, storage, or comparison layers.
