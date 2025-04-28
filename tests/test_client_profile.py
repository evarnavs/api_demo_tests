import os
import requests

BASE_URL = os.getenv("BASE_URL")
EMAIL = os.getenv("EMAIL")


def test_get_client_profile(auth_headers):
    """
    Test retrieving client profile information
    """
    response = requests.get(
        f"{BASE_URL}/api/v1/client/",
        headers=auth_headers
    )
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}: {response.text}"

    json_data = response.json()
    assert "email" in json_data, "Missing 'email' field in profile response"
    assert json_data["email"] == EMAIL, f"Expected email {EMAIL}, got {json_data['email']}"


def test_update_client_profile(auth_headers):
    """
    Test updating client profile information
    """
    payload = {
        "email": EMAIL,
        "name": "Агафон",
        "surname": "Толстой",
        "nickname": "ClientTestUser",
        "sex": "male",
        "yearOfBirth": "1996",
        "urbanRural": "rural"
    }

    response = requests.put(
        f"{BASE_URL}/api/v1/client/",
        headers=auth_headers,
        json=payload
    )

    assert response.status_code in (200, 204), f"Expected 200 or 204, got {response.status_code}: {response.text}"
