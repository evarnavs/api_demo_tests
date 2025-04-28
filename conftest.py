import pytest
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read environment variables
BASE_URL = os.getenv("BASE_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Validate required environment variables
missing = []

if not BASE_URL:
    missing.append("BASE_URL")
if not EMAIL:
    missing.append("EMAIL")
if not PASSWORD:
    missing.append("PASSWORD")

if missing:
    raise ValueError(f"❌ Missing environment variables: {', '.join(missing)}. Set them in .env or GitHub Secrets.")


def load_credentials():
    """
    Load user credentials from environment variables
    """
    return {"email": EMAIL, "password": PASSWORD}


@pytest.fixture(scope="session")
def client_login_response():
    """
    Perform client login and return the full JSON response
    """
    creds = load_credentials()

    url = f"{BASE_URL}/api/v1/user/login"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
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
    assert "token" in json_data and "token" in json_data["token"], "JWT token missing in login response."

    return json_data


@pytest.fixture(scope="session")
def client_auth_token(client_login_response):
    """
    Extract client authentication token (JWT) from login response
    """
    return client_login_response["token"]["token"]


@pytest.fixture
def auth_headers(client_auth_token):
    """
    Provide headers with Authorization token for API requests
    """
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
    """
    Return full user information from login response
    """
    return client_login_response["user"]
