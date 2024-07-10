'''import pytest
import allure
from api.request.api_request import EspoCRMRequest
from api.endpoints.mail_important import EndpointCorreoImportant
from core.assertions.status import *
from core.config.config import BASE_URI
from resources.auth.auth import Auth
import requests


@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression

def test_post_email_insert_image_invalid_email_id(get_headers, invalid_email_id_payload):
    """
    Verify addition of image to email with invalid email ID - status code 400 Bad Request
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post_json(url, headers, invalid_email_id_payload)
    print(f"Response status code: {response.status_code}")
    assert_status_bad_request(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression

def test_post_email_insert_image_without_auth_header(email_insert_image_payload):
    """
    Verify addition of image to email without authorization header - status code 401
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = {}  # No authorization header
    response = EspoCRMRequest.post_json(url, headers, email_insert_image_payload)
    print(f"Response status code: {response.status_code}")
    assert_status_code_unauthorized(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression

def test_post_email_insert_image_invalid_auth_token(get_headers, email_insert_image_payload):
    """
    Verify addition of image to email with invalid authorization token - status code 401
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = {"Authorization": "Basic invalidcredentials"}
    response = EspoCRMRequest.post_json(url, headers, email_insert_image_payload)
    print(f"Response status code: {response.status_code}")
    assert_status_code_unauthorized(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression

def test_post_email_insert_image_network_timeout(get_headers, email_insert_image_payload, monkeypatch):
    """
    Verify addition of image to email with network timeout - status code 504 Gateway Timeout
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)

    def mock_post(*args, **kwargs):
        raise requests.exceptions.Timeout

    monkeypatch.setattr(requests, "post", mock_post)

    with pytest.raises(requests.exceptions.Timeout):
        EspoCRMRequest.post_json(url, headers, email_insert_image_payload)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression

def test_post_email_insert_image_empty_request_body(get_headers, empty_body_payload):
    """
    Verify addition of image to email with empty request body - status code 400 Bad Request
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post_json(url, headers, empty_body_payload)
    print(f"Response status code: {response.status_code}")
    assert_status_bad_request(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression

def test_post_email_insert_image_unauthorized_user(get_headers, email_insert_image_payload):
    """
    Verify addition of image to email by unauthorized user - status code 401
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = get_headers("unauthorizedUser", "unauthorizedPassword")
    response = EspoCRMRequest.post_json(url, headers, email_insert_image_payload)
    print(f"Response status code: {response.status_code}")
    assert_status_code_unauthorized(response)

@allure.suite('EspoCRM')
@allure.sub_suite('Ericka')
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
@allure.tag('author: Ericka')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression

def test_post_email_insert_image_server_down(get_headers, email_insert_image_payload, monkeypatch):
    """
    Verify addition of image to email when server is down - status code 503 Service Unavailable
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)

    def mock_post(*args, **kwargs):
        response = requests.Response()
        response.status_code = 503
        return response

    monkeypatch.setattr(requests, "post", mock_post)

    response = EspoCRMRequest.post_json(url, headers, email_insert_image_payload)
    print(f"Response status code: {response.status_code}")
    assert_status_code_service_unavailable(response)

'''
