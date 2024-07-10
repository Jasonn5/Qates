import pytest
import base64
import requests
from core.config.config import BASE_URI
from resources.auth.auth import Auth
from api.endpoints.mail_important import EndpointCorreoImportant

@pytest.fixture(scope="function")
def email_insert_image_payload(load_image_data):
    return {"emailId": "validEmailId", "imageData": load_image_data}

@pytest.fixture(scope="function")
def invalid_email_id_payload(load_image_data):
    return {"emailId": "invalidEmailId", "imageData": load_image_data}

@pytest.fixture(scope="function")
def large_image_payload(load_large_image_data):
    return {"emailId": "validEmailId", "imageData": load_large_image_data}

@pytest.fixture(scope="function")
def empty_body_payload():
    return {}

@pytest.fixture(scope="function")
def valid_email_payload(load_image_data):
    return {"emailId": "validEmailId", "imageData": load_image_data}

@pytest.fixture(scope="function")
def teardown_email(get_headers):
    created_emails = []

    yield created_emails

    for email_id in created_emails:
        url = f"{EndpointCorreoImportant.GET_MAIL_IMPORTANT}{email_id}"
        headers = Auth().auth_valid_credential(get_headers)
        response = requests.delete(url, headers=headers)
        assert response.status_code == 200, f"Failed to delete email {email_id}"

@pytest.fixture
def load_image_data():
    try:
        with open('resources/images/image.png', 'rb') as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
            print(f"Loaded image data: {image_data[:100]}...")  # Debugging output
            return image_data
    except Exception as e:
        print(f"Failed to load image: {e}")
        raise

@pytest.fixture
def load_large_image_data():
    try:
        with open('resources/images/large_image.png', 'rb') as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
            print(f"Loaded large image data: {image_data[:100]}...")  # Debugging output
            return image_data
    except Exception as e:
        print(f"Failed to load large image: {e}")
        raise



