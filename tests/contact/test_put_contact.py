import allure
import pytest

from api_endpoints.api_request import EspoCRMRequest
from api_endpoints.contact_endpoint import ContactEndpoint
from assertions.assertion_schemas import assert_schema_contact_put
from assertions.assertion_status import assert_status_code_ok, assert_status_code_not_found, \
    assert_status_code_unprocessable_entity, assert_status_code_unauthorized
from config.config import BASE_URI
from tests.contact.conftest import modify_first_name_payload, put_payload, put_url


@allure.feature('Contact - Nicole Muñoz')
@allure.story('Put contact')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.smoke
def test_update_contact_success(get_headers):
    put_payload['firstName'] = modify_first_name_payload()
    headers = get_headers("admin", "admin")
    response = EspoCRMRequest.put(put_url, headers=headers, payload=put_payload)
    assert_status_code_ok(response)


@allure.feature('Contact - Nicole Muñoz')
@allure.story('Put contact')
@pytest.mark.functional
@pytest.mark.smoke
@pytest.mark.regression
def test_update_nonexistent_contact(get_headers):
    nonexistent_url = f"{BASE_URI}{ContactEndpoint.MAIN_ROUTE.value}/michi"
    put_payload['firstName'] = modify_first_name_payload()
    headers = get_headers("admin", "admin")
    response = EspoCRMRequest.put(url=nonexistent_url, headers=headers, payload=put_payload)
    assert_status_code_not_found(response)


@allure.feature('Contact - Nicole Muñoz')
@allure.story('Put contact')
@pytest.mark.functional
@pytest.mark.regression
def test_update_contact_invalid_format(get_headers):
    put_payload['firstName'] = modify_first_name_payload()
    put_payload['michi'] = "michi"
    headers = get_headers("admin", "admin")
    response = EspoCRMRequest.put(put_url, headers=headers, payload=put_payload)
    assert_status_code_unprocessable_entity(response)


@allure.feature('Contact - Nicole Muñoz')
@allure.story('Put contact')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.smoke
def test_update_contact_without_authentication(get_headers):
    put_payload['firstName'] = modify_first_name_payload()
    headers = {}
    response = EspoCRMRequest.put(put_url, headers=headers, payload=put_payload)
    assert_status_code_unauthorized(response)


@allure.feature('Contact - Nicole Muñoz')
@allure.story('Put contact')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.smoke
def test_update_contact_schema_validation(get_headers):
    put_payload['firstName'] = modify_first_name_payload()
    headers = get_headers("admin", "admin")
    response = EspoCRMRequest.put(put_url, headers=headers, payload=put_payload)
    response_json = response.json()
    assert_schema_contact_put(response_json)
