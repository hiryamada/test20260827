import pytest
from fastapi.testclient import TestClient
from test20260827.main import app, WEATHER_CONDITIONS

client = TestClient(app)


def test_get_weather_tokyo():
    response = client.get("/weather/tokyo")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "tokyo"
    assert data["condition"] in WEATHER_CONDITIONS
    assert isinstance(data["max_temp"], int)
    assert isinstance(data["min_temp"], int)
    assert data["max_temp"] > data["min_temp"]


def test_get_weather_other_city():
    response = client.get("/weather/osaka")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "osaka"
    assert data["condition"] in WEATHER_CONDITIONS
    assert data["max_temp"] > data["min_temp"]


def test_weather_response_structure():
    response = client.get("/weather/tokyo")
    data = response.json()
    assert set(data.keys()) == {"city", "condition", "max_temp", "min_temp"}
