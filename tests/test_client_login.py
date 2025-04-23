def test_client_login_success(client_auth_token, client_user_info):
    assert client_auth_token is not None
    assert isinstance(client_auth_token, str)
    assert len(client_auth_token) > 20  # Rough check that it's a real JWT

    assert client_user_info["email"] == "cometechu+6@gmail.com"
    assert client_user_info["type"] == "client"
    assert client_user_info["nickname"] == "ClientTestUser"
