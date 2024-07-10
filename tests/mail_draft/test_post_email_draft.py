import pytest
import requests
import allure
from core.config.config import BASE_URI
from resources.auth.auth import Auth
from api.endpoints.mail_draft import EndpointEmail
from core.utils.load_resources import load_payload, PayloadPaths

@allure.suite('EspoCRM')
@allure.sub_suite('Diego')
@allure.epic('EspoCRM')
@allure.feature('Mail Draft')
@allure.story('Post Mail Draft')
@allure.tag('author: Diego')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_success(get_headers):
    url = f"{BASE_URI}{EndpointEmail.POST_EMAIL_DRAFT.value}"
    headers = Auth().auth_valid_credential(get_headers)
    print(f"Request Headers: {headers}")
    payload_success = load_payload(PayloadPaths.EMAIL_DRAFT_SUCCESS)
    response = requests.post(url, headers=headers, json=payload_success)
    print(f"Response: {response.text}")
    assert response.status_code == 201

@allure.suite('EspoCRM')
@allure.sub_suite('Diego')
@allure.epic('EspoCRM')
@allure.feature('Mail Draft')
@allure.story('Post Mail Draft')
@allure.tag('author: Diego')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_missing_fields(get_headers):
    url = f"{BASE_URI}{EndpointEmail.POST_EMAIL_DRAFT.value}"
    headers = Auth().auth_valid_credential(get_headers)
    print(f"Request Headers: {headers}")
    response = requests.post(url, headers=headers, json={})
    print(f"Response: {response.text}")
    assert response.status_code == 400

@allure.suite('EspoCRM')
@allure.sub_suite('Diego')
@allure.epic('EspoCRM')
@allure.feature('Mail Draft')
@allure.story('Post Mail Draft')
@allure.tag('author: Diego')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_create_email_draft_invalid_email_format(get_headers):
    url = f"{BASE_URI}{EndpointEmail.POST_EMAIL_DRAFT.value}"
    headers = Auth().auth_valid_credential(get_headers)
    print(f"Request Headers: {headers}")
    payload_invalid_email_format = load_payload(PayloadPaths.EMAIL_DRAFT_INVALID_EMAIL_FORMAT)
    response = requests.post(url, headers=headers, json=payload_invalid_email_format)
    print(f"Response: {response.text}")
    assert response.status_code == 400
