from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/",
        json={
            "name": "Ali",
            "age": 30,
            "email": "ali@gmail.com"
        }
    )
    # ✅ Check response status
    assert response.status_code == 201

    # ✅ Parse response data
    data = response.json()

    # ✅ Validate returned fields
    assert data["name"] == "Ali"
    assert data["age"] == 30
    assert data["email"] == "ali@gmail.com"