from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_comparisons_endpoint():
    response = client.get("/api/v1/comparisons")
    assert response.status_code == 200
    assert "items" in response.json()
