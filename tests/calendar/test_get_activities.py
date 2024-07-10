import allure
import pytest
from resources.auth.auth import Auth
from api.request.api_request import EspoCRMRequest
from core.assertions.status import assert_status_bad_request, assert_status_code_ok
from api.params.activities_params import ACTIVITIES_PARAM
from tests.calendar.conftest import url
from tests.conftest import get_headers
from core.assertions.calendar import assert_scope_meeting, assert_scope_task, assert_scope_call
from core.assertions.content import assert_empty_array, assert_size_array
from core.assertions.schemas import assert_schema_activity


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.smoke
def test_get_activity_success(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=ACTIVITIES_PARAM, headers=headers)
    assert_status_code_ok(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_empty_from(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['from'] = ''
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression
def test_get_activity_invalid_from(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['from'] = 'michi'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_scopelist_empty(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['scopeList'] = ''
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_empty_array(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_invalid_to(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['to'] = 'abcdefg'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_empty_to(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['to'] = ''
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_success_with_scope_list_meeting(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['scopeList'] = 'Meeting'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_scope_meeting(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_success_with_scope_list_task(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['scopeList'] = 'Task'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_scope_task(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_success_with_scope_list_call(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['scopeList'] = 'Call'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_scope_call(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_with_only_from_param(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['to'] = ''
    test_params['scopeList'] = ''
    test_params['agenda'] = ''
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_with_only_to_param(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['from'] = ''
    test_params['scopeList'] = ''
    test_params['agenda'] = ''
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.smoke
def test_get_activity_schema_validation(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=ACTIVITIES_PARAM, headers=headers)
    assert_schema_activity(response.json())


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.smoke
def test_get_activity_without_params(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['from'] = ''
    test_params['to'] = ''
    test_params['scopeList'] = ''
    test_params['agenda'] = ''
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_with_agenda_empty(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['agenda'] = ''
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_size_array(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.smoke
def test_get_activity_with_agenda_true(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['agenda'] = 'true'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_size_array(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_with_agenda_false(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['agenda'] = 'false'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_size_array(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_with_agenda_any_value(get_headers):
    headers = Auth().auth_valid_credential(get_headers)
    test_params = ACTIVITIES_PARAM.copy()
    test_params['agenda'] = 'michi'
    response = EspoCRMRequest.get_with_url_headers_params(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_size_array(response)
