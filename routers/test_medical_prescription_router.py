import json
import internal
import requests
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

prefix = "medical-prescription"


def test_medical_prescription_success():
    end_point = "by-id"
    test_id = "ff567cf3-f336-471b-95db-1d1ab9eccfe6"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == dict


def test_medical_prescription_error():
    end_point = "by-id"
    test_id = "ff567cf3-f336-471b-95db1d1ab9eccfe6"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 400
    assert response_json["msg"] == "error"
    assert response_json["data"] == "This ID is invalid"
