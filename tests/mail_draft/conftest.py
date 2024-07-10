import pytest
import requests
from core.config.config import BASE_URI
from api.endpoints.mail_draft import EndpointEmail
from resources.auth.auth import Auth

@pytest.fixture(scope="function", autouse=True)
def teardown(get_headers):
    print("Setup: Test is starting")
    yield
    print("Teardown: Test has ended. Starting cleanup.")
    delete_created_drafts(get_headers)
    print("Teardown: Cleanup finished")

def delete_created_drafts(get_headers):
    print("Teardown: Preparing to delete drafts")
    auth = Auth()
    headers = auth.auth_valid_credential(get_headers)

    print(f"Teardown: Headers prepared for deletion: {headers}")

    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS}"
    response = requests.get(url, headers=headers)

    print(f"Teardown: Response status code: {response.status_code}, Response: {response.text}")

    if response.status_code == 200:
        drafts = response.json().get('list', [])
        for draft in drafts:
            draft_id = draft['id']
            delete_url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.format(id=draft_id)}"
            delete_response = requests.delete(delete_url, headers=headers)
            print(f"Teardown: Delete draft ID {draft_id} response status code: {delete_response.status_code}")
            if delete_response.status_code == 200:
                print(f"Teardown: Draft ID {draft_id} deleted successfully")
            else:
                print(f"Teardown: Failed to delete draft ID {draft_id}")
    else:
        print(f"Teardown: Failed to retrieve drafts, status code: {response.status_code}, response: {response.text}")

