import pytest
import base64
import allure
import requests

from config.config import BASE_URI, USERNAME, PASSWORD
from assertions.assertion_important import assert_content_type_applicationJson, assert_status_code_ok, assert_status_code_unauthorized, assert_status_code_bad_request, assert_status_code_forbidden, assert_status_code_gateway_timeout, assert_status_code_service_unavailable
from api_endpoints.api_request import EspoCRMRequest
from api_endpoints.mail_draft_endpoints import EndpointCorreoDraft
from resources.auth.auth import Auth


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_success(get_headers):
    """
    Verify successful addition of image to email - status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoDraft.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    payload = {"emailId": "validEmailId", "imageData": "base64ImageData"}
    response = EspoCRMRequest.post(url, headers, payload)
    assert_status_code_ok(response)
    assert_content_type_applicationJson(response)


@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_invalid_email_id(get_headers):
    """
    Verify addition of image to email with invalid email ID - status code 400 Bad Request
    """
    url = f"{BASE_URI}{EndpointCorreoDraft.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    payload = {"emailId": "invalidEmailId", "imageData": "base64ImageData"}
    response = EspoCRMRequest.post(url, headers, payload)
    assert_status_code_bad_request(response)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_no_authorization(get_headers):
    """
    Verify addition of image to email without authorization header - status code 401
    """
    url = f"{BASE_URI}{EndpointCorreoDraft.POST_EMAIL_INSERT_IMAGE.value}"
    headers = {}
    payload = {"emailId": "validEmailId", "imageData": "base64ImageData"}
    response = EspoCRMRequest.post(url, headers, payload)
    assert_status_code_unauthorized(response)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_invalid_authorization(get_headers):
    """
    Verify addition of image to email with invalid authorization token - status code 401
    """
    url = f"{BASE_URI}{EndpointCorreoDraft.POST_EMAIL_INSERT_IMAGE.value}"
    headers = get_headers("invalidUser", "invalidPassword")
    payload = {"emailId": "validEmailId", "imageData": "base64ImageData"}
    response = EspoCRMRequest.post(url, headers, payload)
    assert_status_code_unauthorized(response)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_network_timeout(get_headers):
    """
    Verify addition of image to email with network timeout - status code 504 Gateway Timeout
    """
    url = f"{BASE_URI}{EndpointCorreoDraft.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    payload = {"emailId": "validEmailId", "imageData": "base64ImageData"}

    with pytest.raises(requests.exceptions.Timeout):
        response = EspoCRMRequest.post(url, headers, payload)
        assert_status_code_gateway_timeout(response)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_large_image_size(get_headers):
    """
    Verify addition of image to email with large image size - status code 413 Request Entity Too Large
    """
    url = f"{BASE_URI}{EndpointCorreoDraft.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    payload = {"emailId": "validEmailId", "imageData": "largeBase64ImageData"}
    response = EspoCRMRequest.post(url, headers, payload)
    assert response.status_code == 413


@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_empty_request_body(get_headers):
    """
    Verify addition of image to email with empty request body - status code 400 Bad Request
    """
    url = f"{BASE_URI}{EndpointCorreoDraft.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    payload = {}
    response = EspoCRMRequest.post(url, headers, payload)
    assert_status_code_bad_request(response)


@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_expired_token(get_headers):
    """
    Verify addition of image to email with expired authorization token - status code 401 Unauthorized
    """
    url = f"{BASE_URI}{EndpointCorreoDraft.POST_EMAIL_INSERT_IMAGE.value}"
    headers = get_headers("expiredUser", "expiredPassword")
    payload = {"emailId": "validEmailId", "imageData": "base64ImageData"}
    response = EspoCRMRequest.post(url, headers, payload)
    assert_status_code_unauthorized(response)


@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_unauthorized_user(get_headers):
    """
    Verify addition of image to email by unauthorized user - status code 403 Forbidden
    """
    url = f"{BASE_URI}{EndpointCorreoDraft.POST_EMAIL_INSERT_IMAGE.value}"
    headers = get_headers("unauthorizedUser", "unauthorizedPassword")
    payload = {"emailId": "validEmailId", "imageData": "base64ImageData"}
    response = EspoCRMRequest.post(url, headers, payload)
    assert_status_code_forbidden(response)


@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_server_down(get_headers):
    """
    Verify addition of image to email when server is down - status code 503 Service Unavailable
    """
    url = f"{BASE_URI}{EndpointCorreoDraft.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    payload = {"emailId": "validEmailId", "imageData": "base64ImageData"}

    with pytest.raises(requests.exceptions.ConnectionError):
        response = EspoCRMRequest.post(url, headers, payload)
        assert_status_code_service_unavailable(response)


@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Insert Image')
@allure.story('Post Email Insert Image')
def test_post_email_insert_image_response_content(get_headers):
    """
    Verify addition of image to email and ensure all associated data is included in the response - status code 200 OK
    """
    url = f"{BASE_URI}{EndpointCorreoDraft.POST_EMAIL_INSERT_IMAGE.value}"
    headers = Auth().auth_valid_credential(get_headers)
    payload = {"emailId": "validEmailId", "imageData": "base64ImageData"}
    response = EspoCRMRequest.post(url, headers, payload)
    assert_status_code_ok(response)
    assert_content_type_applicationJson(response)
    response_data = response.json()
    assert "emailId" in response_data
    assert "imageData" in response_data
    assert response_data["emailId"] == "validEmailId"
