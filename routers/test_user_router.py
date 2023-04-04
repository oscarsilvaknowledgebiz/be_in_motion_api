import json
import internal
import requests

def test_fetch_user_id():
    second_validate = internal.validate_uuid.is_uuid_valid("123")
    validate = internal.validate_uuid.is_uuid_valid("1f58ff58-daa1-4e35-8910-5293d7667d40")
    assert validate == True
    assert second_validate == False


#def test_fetch_user():
#    path = "/user/1234abcd"
#    response = requests.get(url="http://localhost:2828" + path)
#    response_json = json.loads(response.text)
#    print(response_json["msg"])
#    assert response.status_code == 200
#    assert response_json["msg"] == "success"
#    assert type(response_json["data"]) == dict