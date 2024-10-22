from fastapi.testclient import TestClient
from app.main import app 
from app.schemas.tool import ToolCreate
from app.core.config import settings


client = TestClient(app)

def test_get_stats_success():
    # Get a valid token (you'll need to implement this based on your authentication system)
    valid_token = get_valid_token()

    # Make the request
    response = client.get("/api/stats", headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200

def get_valid_token():
    return settings.API_TOKEN