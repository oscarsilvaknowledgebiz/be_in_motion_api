import json
import core.schemes.user_schemes
import internal
import requests
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

prefix = "user"


# GET UNIT TEST
def test_user_router_success():
    end_point = "by-id"
    test_id = "ff567cf3-f336-471b-95db-1d1ab9eccfe6"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == dict


def test_user_router_info_error():
    end_point = "by-id"
    test_id = "ff567cf3-f336-471b-95db1d1ab9eccfe6"
    path = f"/{prefix}/{end_point}/{test_id}".format(prefix=prefix, end_point=end_point, test_id=test_id)
    response = client.get(path)
    response_json = response.json()
    assert response.status_code == 400
    assert response_json["msg"] == "error"
    assert response_json["data"] == "This ID is invalid"


# PUT UNIT TEST

def test_put_user_router_success():
    end_point = "info"
    test_id = "ff567cf3-f336-471b-95db-1d1ab9eccfe6"
    path = f"/{prefix}/{end_point}".format(prefix=prefix, end_point=end_point)
    payload = json.dumps({
        "id_user": test_id,
        "name": "testname"
    })
    print(payload)
    response = client.put(path, data=payload)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == dict


def test_put_user_router_error():
    end_point = "info"
    test_id = "ff567cf3-f336-471b-95db1d1ab9eccfe6"
    path = f"/{prefix}/{end_point}".format(prefix=prefix, end_point=end_point)
    payload = json.dumps({
        "id_user": test_id,
        "name": "testname"
    })
    print(payload)
    response = client.put(path, data=payload)
    response_json = response.json()
    assert response.status_code == 400
    assert response_json["msg"] == "error"
    assert type(response_json["data"]) == dict


# POST UNIT TEST

def test_post_user_router_success():
    test_id = "ff567cf3-f336-471b-95db-1d1ab9eccfe6"
    path = f"/{prefix}".format(prefix=prefix)
    payload = json.dumps({
        "id_user": test_id,
        "name": "testname",
        "email": "test@email.kbz",
        "password": "password",
        "gmail_access_token": "token121",
        "exponent_push_token": "token121",
        "picture": "picture.png",
        "phone": "123456789",
        "birth_date": "01-01-2000",
        "is_active": True,
        "is_physiotgerapeut": False,
        "is_admin": False,
        "is_verified": False
    })
    print(payload)
    response = client.post(path, data=payload)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == dict
