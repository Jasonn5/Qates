import base64
import pytest
import requests
from config.config import BASE_URI, USERNAME, PASSWORD
from api_endpoints.mail_draft_endpoints import EndpointEmail

def encoded(username, password):
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    print(f"Encoded Credentials: {encoded_credentials}")
    return encoded_credentials

@pytest.fixture
def get_headers():
    def _get_headers(username, password):
        encoded_credentials = encoded(username, password)
        headers = {
            'Authorization': f'Basic {encoded_credentials}',
            'Content-Type': 'application/json'
        }
        print(f"Generated Headers: {headers}")
        return headers

    return _get_headers

@pytest.fixture(scope="function", autouse=True)
def teardown():
    print("Setup: Test is starting")
    yield
    print("Teardown: Test has ended. Starting cleanup.")
    delete_created_drafts()
    print("Teardown: Cleanup finished")

def delete_created_drafts():
    headers = {
        'Authorization': f'Basic {encoded(USERNAME, PASSWORD)}',
        'Content-Type': 'application/json'
    }
    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS.value}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        drafts = response.json().get('list', [])
        for draft in drafts:
            draft_id = draft['id']
            delete_url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
            requests.delete(delete_url, headers=headers)
