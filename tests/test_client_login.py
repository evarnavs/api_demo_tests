import os


def test_client_login_success(client_auth_token, client_user_info):
    expected_email = os.getenv("EMAIL")

    assert client_auth_token is not None
    assert isinstance(client_auth_token, str)

    assert client_user_info["email"] == expected_email
    assert client_user_info["type"] == "client"
    assert client_user_info["nickname"] == "ClientTestUser"
