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

def test_get_login_success():
    username = 'jeyson'
    password = 'Tesing.123!'
    response = get_login(username, password)
    
    assert response.status_code == 200
    assert 'user' in response.json()

def test_get_login_invalid_username():
    username = 'invalid_user'
    password = 'Tesing.123!'
    response = get_login(username, password)
    
    assert response.status_code == 401
    assert response.json().get('error') == 'Unauthorized'

def test_get_login_invalid_password():
    username = 'jeyson'
    password = 'invalid_password'
    response = get_login(username, password)
    
    assert response.status_code == 401
    assert response.json().get('error') == 'Unauthorized'

def test_get_login_invalid_username_and_password():
    username = 'invalid_user'
    password = 'invalid_password'
    response = get_login(username, password)
    
    assert response.status_code == 401
    assert response.json().get('error') == 'Unauthorized'

if __name__ == '__main__':
    pytest.main()