# Live data pipeline

The pipeline converts permitted public source content into normalized price observations.

1. collect source content
2. parse product/price records
3. normalize names and quantities
4. persist observations
5. expose comparison data through the API

The first production target is the public Viva Fresh online shop. The site currently exposes product categories and catalog content publicly. The collector must still be tested against the live response before observations are considered production data.

Facebook remains a separate source adapter and is only used when public/permitted content is available.
