import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "agent": "matchday_agent",
        "version": "1.0.0"
    }

def test_chat_endpoint_missing_message():
    response = client.post("/api/chat", json={})
    assert response.status_code == 422 # Validation error

def test_get_session_not_found():
    response = client.get("/api/sessions/nonexistent_session")
    assert response.status_code == 404
