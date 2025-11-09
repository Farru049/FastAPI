from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    """✅ Test user creation"""
    response = client.post(
        "/users/",
        json={
            "name": "Ali",
            "age": 30,
            "email": "far3@gmail.com"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Ali"
    assert data["age"] == 30
    assert data["email"] == "far3@gmail.com"


def test_create_user_duplicate_email():
    """❌ Creating the same email again should fail"""
    response = client.post(
        "/users/",
        json={
            "name": "Ali",
            "age": 30,
            "email": "ali123@gmail.com"  # duplicate
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_get_all_users():
    """✅ Fetch all users"""
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1  # At least one user created


def test_get_single_user():
    """✅ Fetch user by ID"""
    # Get first user from list
    users = client.get("/users/").json()
    first_user_id = users[0]["id"]

    response = client.get(f"/users/{first_user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == first_user_id
    assert "name" in data


def test_update_user():
    """✅ Update existing user"""
    users = client.get("/users/").json()
    user_id = users[0]["id"]

    response = client.put(
        f"/users/{user_id}",
        json={
            "name": "Ali Updated",
            "age": 31,
            "email": "aliupdated@gmail.com"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Ali Updated"
    assert data["age"] == 31
    assert data["email"] == "aliupdated@gmail.com"


def test_delete_user():
    """✅ Delete user"""
    users = client.get("/users/").json()
    user_id = users[0]["id"]

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"
