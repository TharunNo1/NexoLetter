from app.api.dependencies import get_user_service
import pytest
from unittest.mock import MagicMock
from fastapi.testclient import TestClient
from app.main import app
from app.api.dependencies import UserServiceDep

client = TestClient(app)

@pytest.fixture
def mock_user_service():
    service = MagicMock()
    service.create_user.return_value = {
        "id": 1,
        "email": "nexo@example.com",
        "username": "nexo_user"
    }
    return service

def test_create_user_success(mock_user_service):
    # Override the dependency
    app.dependency_overrides[get_user_service] = lambda: mock_user_service
    
    payload = {"email": "nexo@example.com", "username": "nexo_user", "password": "password123"}
    response = client.post("/api/v1/users/add", json=payload)
    
    assert response.status_code == 200
    assert response.json()["email"] == "nexo@example.com"
    mock_user_service.create_user.assert_called_once()
    
    # Clean up overrides
    app.dependency_overrides.clear()
