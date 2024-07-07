import base64
import pytest
import requests
from config.config import BASE_URI, USERNAME, PASSWORD, EndpointEmail


@pytest.fixture(scope="function", autouse=True)
def teardown():
    print("Setup: Test is starting")
    yield
    print("Teardown: Test has ended. Starting cleanup.")
    delete_created_drafts()
    print("Teardown: Cleanup finished")


def encoded(username, password):
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    print(f"Encoded Credentials: {encoded_credentials}")
    return encoded_credentials


def delete_created_drafts():
    print("Teardown: Preparing to delete drafts")
    headers = {
        'Authorization': f'Basic {encoded(USERNAME, PASSWORD)}',
        'Espo-Authorization': 'YWRtaW46M2EyNDdiMGZiNWZmZDUzNTgxNjdlNjdlNzQwNjFkNWE=',
        'Espo-Authorization-By-Token': 'true',
        'Content-Type': 'application/json'
    }

    print(f"Teardown: Headers prepared for deletion: {headers}")

    url = f"{BASE_URI}{EndpointEmail['GET_EMAIL_WITH_PARAMS']}"
    response = requests.get(url, headers=headers)

    print(f"Teardown: Response status code: {response.status_code}, Response: {response.text}")

    if response.status_code == 200:
        drafts = response.json().get('list', [])
        for draft in drafts:
            draft_id = draft['id']
            delete_url = f"{BASE_URI}/Email/{draft_id}"
            delete_response = requests.delete(delete_url, headers=headers)
            print(f"Teardown: Delete draft ID {draft_id} response status code: {delete_response.status_code}")
            if delete_response.status_code == 200:
                print(f"Teardown: Draft ID {draft_id} deleted successfully")
            else:
                print(f"Teardown: Failed to delete draft ID {draft_id}")
    else:
        print(f"Teardown: Failed to retrieve drafts, status code: {response.status_code}, response: {response.text}")


@pytest.fixture
def get_headers():
    def _get_headers(username, password):
        encoded_credentials = encoded(username, password)
        headers = {
            'Authorization': f'Basic {encoded_credentials}',
            'Espo-Authorization': 'YWRtaW46M2EyNDdiMGZiNWZmZDUzNTgxNjdlNjdlNzQwNjFkNWE=',
            'Espo-Authorization-By-Token': 'true',
            'Content-Type': 'application/json'
        }
        print(f"Generated Headers: {headers}")
        return headers

    return _get_headers
