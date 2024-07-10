'''import pytest
import allure
from api.request.api_request import EspoCRMRequest
from core.config.config import BASE_URI
from resources.auth.auth import Auth
from core.assertions.status import (
    assert_status_code_ok,
    assert_status_code_unauthorized
)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Important')
@allure.story('Delete Email Important')
def test_delete_email_important_success(get_headers, create_important_email):
    """
    Verify successful deletion of important email - status code 200 OK
    """
    email_id = create_important_email()
    url = f"{BASE_URI}/Email/inbox/important/{email_id}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_ok(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Important')
@allure.story('Delete Email Important')
def test_delete_multiple_important_emails(get_headers, create_important_email):
    """
    Verify deletion of multiple important emails - status code 200 OK
    """
    email_ids = [create_important_email() for _ in range(2)]
    headers = Auth().auth_valid_credential(get_headers)

    for email_id in email_ids:
        url = f"{BASE_URI}/Email/inbox/important/{email_id}"
        response = EspoCRMRequest.delete(url, headers)
        assert_status_code_ok(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Important')
@allure.story('Delete Email Important')
def test_delete_email_important_without_auth_header(create_important_email):
    """
    Verify deletion of important email without authorization header - status code 401 Unauthorized
    """
    email_id = create_important_email()
    url = f"{BASE_URI}/Email/inbox/important/{email_id}"
    headers = {}
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_unauthorized(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Important')
@allure.story('Delete Email Important')
def test_delete_email_important_invalid_auth_token(get_headers, create_important_email):
    """
    Verify deletion of important email with invalid authorization token - status code 401 Unauthorized
    """
    email_id = create_important_email()
    url = f"{BASE_URI}/Email/inbox/important/{email_id}"
    headers = {"Authorization": "Basic invalidcredentials"}
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_unauthorized(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Important')
@allure.story('Delete Email Important')
def test_delete_email_important_check_response_content_type(get_headers, create_important_email):
    """
    Verify deletion of important email and check response content type - status code 200 OK
    """
    email_id = create_important_email()
    url = f"{BASE_URI}/Email/inbox/important/{email_id}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_ok(response)
    assert response.headers['Content-Type'] == 'application/json'''