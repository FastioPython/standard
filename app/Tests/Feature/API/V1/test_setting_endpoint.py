from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_settings():
    response = client.get("/v1/settings")
    assert response.status_code == 200