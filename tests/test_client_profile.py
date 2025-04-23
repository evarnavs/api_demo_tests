import requests

def test_get_client_profile(auth_headers):
    response = requests.get(
        "https://staging.usupport.online/api/v1/client/",
        headers=auth_headers
    )
    assert response.status_code == 200
    json_data = response.json()
    assert "email" in json_data
    assert json_data["email"] == "cometechu+6@gmail.com"


def test_update_client_profile(auth_headers):
    payload = {
        "email": "cometechu+6@gmail.com",
        "name": "Агафон",
        "surname": "Толстой",
        "nickname": "ClientTestUser",
        "sex": "male",
        "yearOfBirth": "1996",
        "urbanRural": "rural"
    }
    response = requests.put(
        "https://staging.usupport.online/api/v1/client/",
        headers=auth_headers,
        json=payload
    )
    print("RESPONSE:", response.status_code, response.text)
    assert response.status_code in (200, 204)
