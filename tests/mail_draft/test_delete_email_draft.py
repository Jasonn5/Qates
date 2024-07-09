import pytest
import requests
from config.config import BASE_URI, USERNAME, PASSWORD
from api_endpoints.mail_draft_endpoints import EndpointEmail


@pytest.fixture(scope="function")
def setup_email_draft(get_headers):
    url = f"{BASE_URI}{EndpointEmail.POST_EMAIL_DRAFT.value}"
    headers = get_headers(USERNAME, PASSWORD)
    payload_success = {
        "subject": "Test Draft",
        "body": "This is a test draft",
        "from": "test@example.com",
        "to": ["recipient@example.com"]
    }
    response = requests.post(url, headers=headers, json=payload_success)

    if response.status_code != 201:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response content: {response.text}")
        pytest.fail(f"Setup failed: Unable to create email draft. Status code: {response.status_code}")

    draft_id = response.json().get('id')
    yield draft_id
    delete_draft(draft_id)


def delete_draft(draft_id):
    headers = {
        'Authorization': f'Basic {encoded(USERNAME, PASSWORD)}',
        'Content-Type': 'application/json'
    }
    delete_url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    requests.delete(delete_url, headers=headers)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_success(get_headers, setup_email_draft):
    url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=setup_email_draft)}"
    headers = get_headers(USERNAME, PASSWORD)
    response = requests.delete(url, headers=headers)
    assert response.status_code == 200


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_no_auth_header(setup_email_draft):
    url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=setup_email_draft)}"
    response = requests.delete(url)
    assert response.status_code == 401


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_invalid_auth_token(setup_email_draft):
    url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=setup_email_draft)}"
    headers = {
        'Authorization': 'Basic invalidtoken',
        'Content-Type': 'application/json'
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 401
