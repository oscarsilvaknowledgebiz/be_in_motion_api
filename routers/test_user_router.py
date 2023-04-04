import json

import requests

def test_fetch_user():
    path = "/user/1234abcd"
    response = requests.get(url="http://localhost:2828" + path)
    response_json = json.loads(response.text)
    print(response_json["msg"])
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == dict