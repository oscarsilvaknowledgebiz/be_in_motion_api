import json
import internal
import requests

def test_medical_prescription():
    path = "/medical-prescription/by-id/ff567cf3-f336-471b-95db-1d1ab9eccfe6"
    response = requests.get(url="http://localhost:2828" + path)
    response_json = json.loads(response.text)
    print(response_json["msg"])
    assert response.status_code == 200
    assert response_json["msg"] == "success"
    assert type(response_json["data"]) == dict

