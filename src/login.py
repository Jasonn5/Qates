import requests
import base64

BASE_URL = 'https://espo.spartan-soft.com/api/v1'
API_ENDPOINT = '/App/user'

def get_auth_token(username, password):
    credentials = f"{username}:{password}"
    token = base64.b64encode(credentials.encode()).decode()
    return token

def login(username, password):
    url = f"{BASE_URL}{API_ENDPOINT}"
    token = get_auth_token(username, password)
    headers = {
        'Authorization': f'Basic {token}',
        'Content-Type': 'application/json',
        'Cookie': 'auth-token-secret=068858cae2765fdb68d845634fbf3746'
    }
    response = requests.get(url, headers=headers)
    return response

if __name__ == "__main__":
    username = 'admin'
    password = 'admin'
    response = login(username, password)
    print(response.text)