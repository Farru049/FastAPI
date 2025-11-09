from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_product_creation():
    response = client.post(
        "/products/",
        json = {
            "name": "Test Product",
            "price": 20.44,
            "description": "Random Description"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 20.44
    assert data["description"] == "Random Description"