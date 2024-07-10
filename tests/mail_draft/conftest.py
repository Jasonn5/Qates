import base64

import pytest
import requests

from core.assertions import headers
from core.config.config import BASE_URI
from api.endpoints.mail_draft import EndpointEmail
from resources.auth.auth import Auth
from core.utils.load_resources import load_payload, PayloadPaths


@pytest.fixture(scope="function", autouse=True)
def teardown(request, get_headers):
    if 'test_post_email_draft' in request.node.nodeid:
        print("Setup: Test is starting")
        yield
        print("Teardown: Test has ended. Starting cleanup.")
        delete_created_drafts(get_headers)
        print("Teardown: Cleanup finished")
    else:
        yield

def delete_created_drafts(get_headers):
    print("Teardown: Preparing to delete drafts")
    auth = Auth()
    headers = auth.auth_valid_credential(get_headers)

    print(f"Teardown: Headers prepared for deletion: {headers}")

    url = f"{BASE_URI}{EndpointEmail.GET_EMAIL_WITH_PARAMS}"
    response = requests.get(url, headers=headers)

    print(f"Teardown: Response status code: {response.status_code}, Response: {response.text}")

    drafts = response.json().get('list', []) if response.status_code == 200 else []

    for draft in drafts:
        draft_id = draft['id']
        delete_url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.format(id=draft_id)}"
        delete_response = requests.delete(delete_url, headers=headers)
        print(f"Teardown: Delete draft ID {draft_id} response status code: {delete_response.status_code}")
        if delete_response.status_code in [200, 204, 404]:
            print(f"Teardown: Draft ID {draft_id} deleted successfully or already deleted")
        else:
            print(f"Teardown: Failed to delete draft ID {draft_id}, status code: {delete_response.status_code}")

@pytest.fixture
def create_email_draft(get_headers):
    created_drafts = []

    def _create_email_draft():
        url = f"{BASE_URI}{EndpointEmail.POST_EMAIL_DRAFT.value}"
        headers = get_headers(USERNAME, PASSWORD)
        payload = load_payload(PayloadPaths.EMAIL_DRAFT_SUCCESS)
        response = requests.post(url, headers=headers, json=payload)
        assert response.status_code == 201, "Failed to create email draft"
        draft_id = response.json().get('id')
        created_drafts.append(draft_id)
        return draft_id

    yield _create_email_draft

    # Ensure drafts created by the test are deleted
    for draft_id in created_drafts:
        delete_url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.format(id=draft_id)}"
        delete_response = requests.delete(delete_url, headers=headers)
        if delete_response.status_code in [200, 204, 404]:
            print(f"Teardown: Draft ID {draft_id} deleted successfully")
        else:
            print(f"Teardown: Failed to delete draft ID {draft_id}, status code: {delete_response.status_code}")

@pytest.fixture
def get_headers():
    def _get_headers(username=USERNAME, password=PASSWORD):
        auth = base64.b64encode(f"{username}:{password}".encode()).decode()
        return {
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/json"
        }
    return _get_headers

USERNAME = 'admin'
PASSWORD = 'admin'

