import pytest
import requests
from config.config import BASE_URI, USERNAME, PASSWORD
from api_endpoints.mail_draft_endpoints import EndpointEmail

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_success(get_headers):
    url = f"{BASE_URI}{EndpointEmail.POST_EMAIL_DRAFT.value}"
    headers = get_headers(USERNAME, PASSWORD)
    payload_success = {
        "subject": "Test Draft",
        "body": "This is a test draft",
        "from": "test@example.com",
        "to": ["recipient@example.com"]
    }
    response = requests.post(url, headers=headers, json=payload_success)
    assert response.status_code == 201
    return response.json()['id']

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_success(get_headers):
    draft_id = test_create_email_draft_success(get_headers)
    url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    headers = get_headers(USERNAME, PASSWORD)
    response = requests.delete(url, headers=headers)
    assert response.status_code == 200

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_no_auth_header(get_headers):
    draft_id = test_create_email_draft_success(get_headers)
    url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 401

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_email_draft_invalid_auth_token(get_headers):
    draft_id = test_create_email_draft_success(get_headers)
    url = f"{BASE_URI}{EndpointEmail.DELETE_EMAIL_DRAFT.value.format(id=draft_id)}"
    headers = {
        'Authorization': 'Basic invalid_token',
        'Content-Type': 'application/json'
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 401
