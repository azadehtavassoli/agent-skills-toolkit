import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.settings import get_settings

@pytest.fixture
def client():
    return TestClient(app)

def test_sample_endpoint(client):
    resp = client.post("/api/sample", json={"input_value": "test"})
    assert resp.status_code == 200
    assert "processed" in resp.json().get("message")
