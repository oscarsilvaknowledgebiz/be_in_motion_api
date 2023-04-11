import json
import internal
import requests
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

prefix = "user-constitution"


def test_user_constitution_success():
    test_id = "ff567cf3-f336-471b-95db-1d1ab9eccfe6"
    path = f"/{prefix}/{test_id}".format(prefix=prefix, test_id=test_id)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == dict


def test_user_constitution_error():
    test_id = "ff567cf3-f336-471b-95db1d1ab9eccfe6"
    path = f"/{prefix}/{test_id}".format(prefix=prefix, test_id=test_id)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 400
    assert response_json["msg"] == "error"
    assert response_json["data"] == "This ID is invalid"
