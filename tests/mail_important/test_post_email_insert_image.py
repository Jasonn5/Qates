import pytest
import allure
from api_endpoints.api_request import EspoCRMRequest
from api_endpoints.mail_important_endpoints import EndpointCorreoImportant
from assertions.assertion_status import *
from assertions.assertion_schemas import assert_valid_schema, email_insert_image_schema
from config.config import BASE_URI, USERNAME, PASSWORD
from resources.auth.auth import Auth
from payloads.mail_important.payload_email_insert_image import *
import requests


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_success(get_headers):
    """
    Verify successful addition of image to email - status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post_json(url, headers, email_insert_image_payload)
    assert_status_code_ok(response)
    data = response.json()
    assert_valid_schema(data, email_insert_image_schema)


@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_invalid_email_id(get_headers):
    """
    Verify addition of image to email with invalid email ID - status code 400 Bad Request
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post_json(url, headers, invalid_email_id_payload)
    assert_status_bad_request(response)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_without_auth_header(get_headers):
    """
    Verify addition of image to email without authorization header - status code 401
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = {}  # No authorization header
    response = EspoCRMRequest.post_json(url, headers, email_insert_image_payload)
    assert_status_code_unauthorized(response)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_invalid_auth_token(get_headers):
    """
    Verify addition of image to email with invalid authorization token - status code 401
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = {"Authorization": "Basic invalidcredentials"}
    response = EspoCRMRequest.post_json(url, headers, email_insert_image_payload)
    assert_status_code_unauthorized(response)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_network_timeout(get_headers, monkeypatch):
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


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_check_response_content_type(get_headers):
    """
    Verify addition of image to email and check response content type - status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post_json(url, headers, email_insert_image_payload)
    assert_status_code_ok(response)
    assert response.headers['Content-Type'] == 'application/json'


@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_large_image_size(get_headers):
    """
    Verify addition of image to email with large image size - status code 413 Request Entity Too Large
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post_json(url, headers, large_image_payload)
    assert response.status_code == 413


@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_empty_request_body(get_headers):
    """
    Verify addition of image to email with empty request body - status code 400 Bad Request
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post_json(url, headers, empty_body_payload)
    assert_status_bad_request(response)


@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_unauthorized_user(get_headers):
    """
    Verify addition of image to email by unauthorized user - status code 403 Forbidden
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = get_headers("unauthorizedUser", "unauthorizedPassword")
    response = EspoCRMRequest.post_json(url, headers, email_insert_image_payload)
    assert_status_code_forbidden(response)


@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_server_down(get_headers, monkeypatch):
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
    assert_status_code_service_unavailable(response)


@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_ensure_all_data_in_response(get_headers):
    """
    Verify addition of image to email and ensure all associated data is included in the response - status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoImportant.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post_json(url, headers, email_insert_image_payload)
    assert_status_code_ok(response)
    data = response.json()
    assert_valid_schema(data, email_insert_image_schema)