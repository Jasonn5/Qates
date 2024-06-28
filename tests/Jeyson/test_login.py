import requests
import base64
import pytest

BASE_URI = 'https://espo.spartan-soft.com/api/v1'

def get_login(username, password):
    url = f'{BASE_URI}/App/user'
    espo_authorization = encoded(username, password)
    headers = {
        'Espo-Authorization': espo_authorization
    }

    response = requests.get(url, headers=headers)
    return response

def encoded(username, password):
    credentials = f'{username}:{password}'
    encode = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return encode

@pytest.fixture
def get_headers():
    def _get_headers(username, password):
        espo_authorization = encoded(username, password)
        return {
            'Espo-Authorization': espo_authorization
        }

    return _get_headers

def get_auth_headers(username, password):
    espo_authorization = encoded(username, password)
    return {
        'Espo-Authorization': espo_authorization
    }


def test_get_login_success(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("jeyson", "Testing.123!"))
    print(response)
    assert response.status_code == 200


def test_get_login_invalid_username(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("invalid_user", "Testing.123!"))
    assert response.status_code == 401


def test_get_login_invalid_password(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("jeyson", "invalid_password"))
    assert response.status_code == 401


def test_get_login_invalid_username_and_password(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("invalid_user", "invalid_password"))
    assert response.status_code == 401


def test_login_empty_fields(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("", ""))
    assert response.status_code == 401


def test_login_empty_user(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("", "Testing.123!"))
    assert response.status_code == 401


def test_login_empty_password(get_headers):
    response = requests.get(f'{BASE_URI}/App/user', headers=get_headers("jeyson", ""))
    assert response.status_code == 401