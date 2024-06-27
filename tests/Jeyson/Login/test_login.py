import requests
import base64
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

@pytest.fixture
def mock_requests_get(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        if args[0] == f'{BASE_URI}/App/user':
            if kwargs['headers']['Espo-Authorization'] == encoded('jeyson', 'Tesing.123!'):
                return MockResponse({"user": "info"}, 200)
            else:
                return MockResponse({"error": "Unauthorized"}, 401)

    monkeypatch.setattr(requests, "get", mock_get)

def test_get_login_success(mock_requests_get):
    username = 'jeyson'
    password = 'Tesing.123!'
    response = get_login(username, password)

    assert response.status_code == 200
    assert response.json() == {"user": "info"}

def test_get_login_invalid_username(mock_requests_get):
    username = 'invalid_user'
    password = 'Tesing.123!'
    response = get_login(username, password)

    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

def test_get_login_invalid_password(mock_requests_get):
    username = 'jeyson'
    password = 'invalid_password'
    response = get_login(username, password)

    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

def test_get_login_invalid_username_and_password(mock_requests_get):
    username = 'invalid_user'
    password = 'invalid_password'
    response = get_login(username, password)

    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}