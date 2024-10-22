import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings


client = TestClient(app)

@pytest.fixture
def valid_token():
    return settings.API_TOKEN

def test_process_user_query_success(valid_token):
    query_text = "What is the capital of France?"
    headers = {"Authorization": f"Bearer {valid_token}"}
    response = client.post("/api/query", json={"text": query_text}, headers=headers)

    assert response.status_code == 200
    result = response.json()
    assert result["query"] == query_text
    assert "results" in result
    assert isinstance(result["results"], list)

def test_process_user_query_unauthorized():
    query_text = "What is the capital of France?"
    response = client.post("/api/query", json={"text": query_text})

    assert response.status_code == 403
    assert "detail" in response.json()

def test_process_user_query_invalid_input(valid_token):
    headers = {"Authorization": f"Bearer {valid_token}"}
    response = client.post("/api/query", json={}, headers=headers)

    assert response.status_code == 422
    assert "detail" in response.json()

