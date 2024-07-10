import pytest
import base64
import requests
from core.config.config import BASE_URI
from resources.auth.auth import Auth

@pytest.fixture
def email_insert_image_payload():
    return {"emailId": "validEmailId", "imageData": "base64ImageData"}

@pytest.fixture
def invalid_email_id_payload():
    return {"emailId": "invalidEmailId", "imageData": "base64ImageData"}

@pytest.fixture
def large_image_payload():
    return {"emailId": "validEmailId", "imageData": "largeBase64ImageData"}

@pytest.fixture
def empty_body_payload():
    return {}

@pytest.fixture
def valid_email_payload():
    return {"emailId": "validEmailId", "imageData": "base64ImageData"}

@pytest.fixture
def teardown_email(get_headers):
    created_emails = []

    yield created_emails

    for email_id in created_emails:
        url = f"https://espo.spartan-soft.com/api/v1/Email/{email_id}"
        headers = Auth().auth_valid_credential(get_headers)
        response = requests.delete(url, headers=headers)
        assert response.status_code == 200, f"Failed to delete email {email_id}"

@pytest.fixture
def valid_email_payload():
    return {
        "emailId": "validEmailId",
        "imageData": "base64ImageData"
    }

@pytest.fixture
def large_image_payload():
    return {
        "emailId": "validEmailId",
        "imageData": "largeBase64ImageData"  # Simulated large image data
    }
@pytest.fixture
def create_important_email(get_headers):
    created_emails = []

    def _create_important_email():
        url = f"{BASE_URI}/Email"
        headers = get_headers()
        payload = {"emailId": "importantEmailId", "isImportant": True}
        response = requests.post(url, headers=headers, json=payload)
        assert response.status_code == 200, "Failed to create important email"
        email_id = response.json().get('id')
        created_emails.append(email_id)
        return email_id

    yield _create_important_email

    # Teardown: Eliminar correos importantes creados
    for email_id in created_emails:
        url = f"{BASE_URI}/Email/inbox/important/{email_id}"
        headers = get_headers()
        response = requests.delete(url, headers=headers)
        assert response.status_code == 200, f"Failed to delete important email {email_id}"

