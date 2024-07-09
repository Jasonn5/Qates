import pytest
import requests
from config.config import BASE_URI, USERNAME, PASSWORD
from api_endpoints.mail_draft_endpoints import EndpointEmail
from utils.load_resources import load_payload, PayloadPaths

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_success(get_headers):
    url = f"{BASE_URI}{EndpointEmail.POST_EMAIL_DRAFT.value}"
    headers = get_headers(USERNAME, PASSWORD)
    print(f"Request Headers: {headers}")
    payload_success = load_payload(PayloadPaths.EMAIL_DRAFT_SUCCESS)
    response = requests.post(url, headers=headers, json=payload_success)
    print(f"Response: {response.text}")
    assert response.status_code == 201

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_missing_fields(get_headers):
    url = f"{BASE_URI}{EndpointEmail.POST_EMAIL_DRAFT.value}"
    headers = get_headers(USERNAME, PASSWORD)
    print(f"Request Headers: {headers}")
    response = requests.post(url, headers=headers, json={})
    print(f"Response: {response.text}")
    assert response.status_code == 400

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_invalid_email_format(get_headers):
    url = f"{BASE_URI}{EndpointEmail.POST_EMAIL_DRAFT.value}"
    headers = get_headers(USERNAME, PASSWORD)
    print(f"Request Headers: {headers}")
    payload_invalid_email_format = load_payload(PayloadPaths.EMAIL_DRAFT_INVALID_EMAIL_FORMAT)
    response = requests.post(url, headers=headers, json=payload_invalid_email_format)
    print(f"Response: {response.text}")
    assert response.status_code == 400