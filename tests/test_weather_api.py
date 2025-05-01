import sys
import os
import pytest
import requests_mock

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from app import app  # noqa: E402

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_get_weather_success(client):
    with requests_mock.Mocker() as mocker:
        mocker.get(
            "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/San%20Jose/today",
            json={"address": "San Jose", "days": []},
        )
        response = client.get("/weather?location=San%20Jose")
        assert response.status_code == 200
        assert response.json["address"] == "San Jose"

def test_get_weather_missing_location(client):
    response = client.get("/weather")
    assert response.status_code == 400
    assert response.json == {"error": "Location is required"}

def test_get_weather_invalid_endpoint(client):
    response = client.get("/invalid")
    assert response.status_code == 404
    assert response.json == {"error": "Invalid endpoint"}
