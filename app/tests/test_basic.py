from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_error_500():
    r = client.get("/error")
    assert r.status_code == 500

def test_metrics_exposed():
    r = client.get("/metrics")
    assert r.status_code == 200
    assert "http_requests_total" in r.text
