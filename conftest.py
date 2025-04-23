import pytest
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def load_credentials():
    return {
        "email": os.getenv("EMAIL"),
        "password": os.getenv("PASSWORD")
    }

@pytest.fixture(scope="session")
def client_login_response():
    creds = load_credentials()

    url = "https://staging.usupport.online/api/v1/user/login"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://staging.usupport.online",
        "referer": "https://staging.usupport.online/client/login",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/134.0.0.0 Safari/537.36"
        ),
        "x-country-alpha-2": "KZ",
        "x-language-alpha-2": "en",
        "x-location": "Asia/Yerevan, AM"
    }

    payload = {
        "userType": "client",
        "email": creds["email"],
        "password": creds["password"]
    }

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 200, f"Login failed: {response.text}"

    json_data = response.json()
    assert "token" in json_data and "token" in json_data["token"], "JWT not found"
    return json_data


@pytest.fixture(scope="session")
def client_auth_token(client_login_response):
    return client_login_response["token"]["token"]


@pytest.fixture
def auth_headers(client_auth_token):
    return {
        "Authorization": f"Bearer {client_auth_token}",
        "x-country-alpha-2": "KZ",
        "x-language-alpha-2": "en",
        "x-location": "Asia/Yerevan, AM",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


@pytest.fixture(scope="session")
def client_user_info(client_login_response):
    return client_login_response["user"]
