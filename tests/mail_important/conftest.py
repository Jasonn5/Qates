import pytest
import base64
import requests
from config.config import USERNAME, PASSWORD

@pytest.fixture
def teardown_email():
    created_emails = []

    yield created_emails

    for email_id in created_emails:
        url = f"https://espo.spartan-soft.com/api/v1/Email/{email_id}"
        headers = get_headers()(USERNAME, PASSWORD)
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

