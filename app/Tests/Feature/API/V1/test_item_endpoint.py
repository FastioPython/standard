from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_item_list():
    response = client.get("/v1/items")
    assert response.status_code == 200
