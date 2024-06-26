import requests
import base64
import responses
import pytest

BASE_URI = 'https://espo.spartan-soft.com/api/v1'
X_Api_Key = 'your_api_key_here'

def get_login(username, password):
    url = f'{BASE_URI}/App/user'
    espo_authorization = encoded(username, password)
    headers = {
        'Espo-Authorization': espo_authorization,
        'X-Api-Key': X_Api_Key,
        'content-type': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    return response

def encoded(username, password):
    credentials = f'{username}:{password}'
    encode = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return encode

@responses.activate
def test_get_login_success():
    responses.add(
        responses.GET,
        'https://espo.spartan-soft.com/api/v1/App/user',
        json={"user": "info"},
        status=200
    )

    username = 'jeyson'
    password = 'Tesing.123!'
    response = get_login(username, password)

    assert response.status_code == 200
    assert response.json() == {"user": "info"}

@responses.activate
def test_get_login_invalid_username():
    responses.add(
        responses.GET,
        'https://espo.spartan-soft.com/api/v1/App/user',
        json={"error": "Unauthorized"},
        status=401
    )

    username = 'invalid_user'
    password = 'Tesing.123!'
    response = get_login(username, password)

    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

@responses.activate
def test_get_login_invalid_password():
    responses.add(
        responses.GET,
        'https://espo.spartan-soft.com/api/v1/App/user',
        json={"error": "Unauthorized"},
        status=401
    )

    username = 'jeyson'
    password = 'invalid_password'
    response = get_login(username, password)

    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

@responses.activate
def test_get_login_invalid_username_and_password():
    responses.add(
        responses.GET,
        'https://espo.spartan-soft.com/api/v1/App/user',
        json={"error": "Unauthorized"},
        status=401
    )

    username = 'invalid_user'
    password = 'invalid_password'
    response = get_login(username, password)

    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

if __name__ == '__main__':
    pytest.main()
