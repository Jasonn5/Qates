import pytest
import allure
from api.request.api_request import EspoCRMRequest
from core.config.config import BASE_URI
from resources.auth.auth import Auth
from core.assertions.status import (
    assert_status_code_ok,
    assert_status_code_unauthorized,
    assert_status_code_not_found,
    assert_status_bad_request
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
    email_id = create_important_email
    url = f"{BASE_URI}/Email/{email_id}"
    headers = get_headers()
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
    email_id = create_important_email
    url = f"{BASE_URI}/Email/{email_id}"
    headers = {}
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_unauthorized(response)

#ne
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Important')
@allure.story('Delete Email Important')
def test_delete_multiple_important_emails(get_headers, create_multiple_important_emails):
    """
    Verify deletion of multiple important emails - status code 200 OK
    """
    email_ids = create_multiple_important_emails
    headers = Auth().auth_valid_credential(get_headers)

    for email_id in email_ids:
        url = f"{BASE_URI}/Email/{email_id}"
        response = EspoCRMRequest.delete(url, headers)
        assert_status_code_ok(response)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
@allure.feature('Email Important')
@allure.story('Delete Email Important')
def test_delete_already_deleted_email(get_headers, create_and_delete_important_email):
    """
    Verify deletion of an already deleted important email - status code 404 Not Found
    """
    email_id = create_and_delete_important_email
    url = f"{BASE_URI}/Email/{email_id}"
    headers = get_headers()
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_not_found(response)

