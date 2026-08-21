"""Minimal comparison API foundation."""
from fastapi import FastAPI

app = FastAPI(title="Kosovo Supermarket Price Tracker API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/v1/supermarkets")
def supermarkets():
    return {"items": []}


@app.get("/api/v1/comparisons")
def comparisons():
    return {"items": []}
