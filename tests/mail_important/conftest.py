import pytest
import base64
import requests


from api_endpoints.api_request import EspoCRMRequest
from config.config import USERNAME, PASSWORD, BASE_URI

@pytest.fixture
def email_insert_image_payload(load_image_data):
    return {"emailId": "validEmailId", "imageData": load_image_data}

@pytest.fixture
def invalid_email_id_payload(load_image_data):
    return {"emailId": "invalidEmailId", "imageData": load_image_data}

@pytest.fixture
def large_image_payload(load_large_image_data):
    return {"emailId": "validEmailId", "imageData": load_large_image_data}

@pytest.fixture
def empty_body_payload():
    return {}

@pytest.fixture
def valid_email_payload(load_image_data):
    return {"emailId": "validEmailId", "imageData": load_image_data}

@pytest.fixture
def get_headers():
    def _get_headers(username=USERNAME, password=PASSWORD):
        auth = base64.b64encode(f"{username}:{password}".encode()).decode()
        return {
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/json"
        }
    return _get_headers


"""
def get_first_non_important_email_id(response):
    response_json = response.json()
    for email in response_json["list"]:
        if not email.get["isImportant"]:
            return email["id"]
    return None


@pytest.fixture(scope="function")
def create_important_email():
        url = f"{BASE_URI}/Email"
        headers = {"Cookie": "some_other_cookie=some_value"}
        response_get = EspoCRMRequest.get_with_url_headers(url, headers)
        id_email_not_important = get_first_non_important_email_id(response_get)
        print (response_get)
        print (id_email_not_important)


        url = f"{BASE_URI}/Email/inbox/important"
        headers = get_headers()
        payload = {"ids":["668e047bb56c1efb5"]}
        payload["ids"] = [id_email_not_important]
        response = requests.post(url, headers=headers, json=payload)
        assert response.status_code == 200, f"Failed to create important email. Response: {response.text}"
        email_id = response.json().get('id')
        #created_emails.append(email_id)
        yield email_id

"""
#nuevo


def get_first_non_important_email_id(response):
    response_json = response.json()
    for email in response_json.get("list", []):
        if not email.get("isImportant", False):
            return email["id"]
    return None


@pytest.fixture
def get_headers():
    def _get_headers(username=USERNAME, password=PASSWORD):
        auth = base64.b64encode(f"{username}:{password}".encode()).decode()
        return {
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/json"
        }

    return _get_headers


@pytest.fixture(scope="function")
def create_important_email(get_headers):
    # Paso 1: Obtener el ID de un correo no importante
    url = f"{BASE_URI}/Email"
    headers = get_headers()

    response_get = requests.get(url, headers=headers)
    assert response_get.status_code == 200, f"Failed to fetch emails. Response: {response_get.text}"

    id_email_not_important = get_first_non_important_email_id(response_get)
    assert id_email_not_important is not None, "No non-important email found"

    # Paso 2: Marcar el correo no importante como importante
    url = f"{BASE_URI}/Email/inbox/important"
    payload = {"ids": [id_email_not_important]}
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200, f"Failed to create important email. Response: {response.text}"

    yield id_email_not_important

    # Limpieza: Verificar si el correo aún existe antes de intentar eliminarlo
    url = f"{BASE_URI}/Email/{id_email_not_important}"
    response_check = requests.get(url, headers=headers)


