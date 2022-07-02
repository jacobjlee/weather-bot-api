import json
import random

from requests import Response
from fastapi.testclient import TestClient

from src.tests import app


client = TestClient(app)


def test_summary_without_parameters():
    """Test get 422 if there are no parameters."""
    # given (none)

    # when
    response: Response = client.get("/summary")
    results: json = response.json()

    # then
    assert response.status_code == 422
    assert results["detail"][0]['msg'] == "field required"
    assert results["detail"][1]['msg'] == "field required"


def test_summary_missing_lon_parameter():
    """Test get 422 if one parameter is missing."""
    # given
    params: dict = dict(lat=1)

    # when
    response: Response = client.get("/summary", params=params)
    results: json = response.json()

    # then
    assert response.status_code == 422
    assert results["detail"][0]['msg'] == "field required"


def test_summary_missing_lat_parameter():
    # given
    params: dict = dict(lon=1)

    # when
    response: Response = client.get("/summary", params=params)
    results: json = response.json()

    # then
    assert response.status_code == 422
    assert results["detail"][0]['msg'] == "field required"


def test_summary_invalid_lat_parameter():
    # given
    params: dict = dict(lat=random.uniform(-100, -91), lon=1)
    # when
    response: Response = client.get("/summary", params=params)
    # then
    assert response.status_code == 422

    # given
    params: dict = dict(lat=random.uniform(91, 100), lon=1)
    # when
    response: Response = client.get("/summary", params=params)
    # then
    assert response.status_code == 422


def test_summary_invalid_lon_parameter():
    # given
    params: dict = dict(lat=1, lon=random.uniform(-190, -181))
    # when
    response: Response = client.get("/summary", params=params)
    # then
    assert response.status_code == 422

    # given
    params: dict = dict(lat=1, lon=random.uniform(181, 190))
    # when
    response: Response = client.get("/summary", params=params)
    # then
    assert response.status_code == 422

