import allure
import pytest
from resources.auth.auth import Auth
from api.request.api_request import EspoCRMRequest
from core.assertions.schemas import assert_schema_contact_post, assert_schema_error_contact_post
from core.assertions.status import assert_status_code_conflict, assert_status_code_created, \
    assert_status_bad_request
from tests.contact.conftest import modify_first_name_payload, teardown_post_contact, post_payload, url, \
    post_full_payload


@allure.feature('Contact - Nicole Muñoz')
@allure.story('Post contact')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.smoke
def test_post_contact_success(get_headers):
    post_payload['firstName'] = modify_first_name_payload()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post(url, headers=headers, payload=post_payload)
    response_json = response.json()
    assert_status_code_created(response)
    teardown_post_contact(headers, response_json)


@allure.feature('Contact - Nicole Muñoz')
@allure.story('Post contact')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.smoke
def test_contact_schema_validation(get_headers):
    post_payload['firstName'] = modify_first_name_payload()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post(url, headers=headers, payload=post_payload)
    response_json = response.json()
    assert_schema_contact_post(response_json)
    teardown_post_contact(headers, response_json)


@allure.feature('Contact - Nicole Muñoz')
@allure.story('Post contact')
@pytest.mark.functional
@pytest.mark.regression
def test_duplicate_contact(get_headers):
    post_payload['firstName'] = modify_first_name_payload()
    headers = Auth().auth_valid_credential(get_headers)
    EspoCRMRequest.post(url, headers=headers, payload=post_payload)
    duplicated_response = EspoCRMRequest.post(url, headers=headers, payload=post_payload)
    assert_status_code_conflict(duplicated_response)


@allure.feature('Contact - Nicole Muñoz')
@allure.story('Post contact')
@pytest.mark.functional
@pytest.mark.regression
def test_required_first_name_empty(get_headers):
    post_payload['firstName'] = ""
    post_payload['lastName'] = modify_first_name_payload()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post(url, headers=headers, payload=post_payload)
    assert_status_bad_request(response)


@allure.feature('Contact - Nicole Muñoz')
@allure.story('Post contact')
@pytest.mark.functional
@pytest.mark.regression
def test_required_last_name_empty(get_headers):
    post_payload['firstName'] = modify_first_name_payload()
    post_payload['lastName'] = ""
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post(url, headers=headers, payload=post_payload)
    assert_status_bad_request(response)


@allure.feature('Contact - Nicole Muñoz')
@allure.story('Post contact')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.smoke
def test_error_contact_schema_validation(get_headers):
    post_payload['firstName'] = modify_first_name_payload()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post(url, headers=headers, payload=post_payload)
    response_json = response.json()
    assert_schema_error_contact_post(response_json)


@allure.feature('Contact - Nicole Muñoz')
@allure.story('Post contact')
@pytest.mark.functional
@pytest.mark.regression
def test_post_contact_success_with_all_values(get_headers):
    post_full_payload['firstName'] = modify_first_name_payload()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post(url, headers=headers, payload=post_full_payload)
    assert_status_code_created(response)
    response_json = response.json()
    teardown_post_contact(headers, response_json)
