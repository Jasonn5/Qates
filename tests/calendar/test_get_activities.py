'''import allure
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


@pytest.fixture
def setup_data(request):
    original_params = ACTIVITIES_PARAM.copy()

    def finalizer():
        ACTIVITIES_PARAM.clear()
        ACTIVITIES_PARAM.update(original_params)
    request.addfinalizer(finalizer)
    return ACTIVITIES_PARAM


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
def test_get_activity_empty_from(get_headers, setup_data):
    setup_data['from'] = ''
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.regression
def test_get_activity_invalid_from(get_headers, setup_data):
    setup_data['from'] = 'michi'
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_scopelist_empty(get_headers, setup_data):
    setup_data['scopeList'] = ''
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_code_ok(response)
    assert_empty_array(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_invalid_to(get_headers,setup_data):
    setup_data['to'] = 'michi'
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_empty_to(get_headers, setup_data):
    setup_data['to'] = ''
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_success_with_scope_list_meeting(get_headers, setup_data):
    setup_data['scopeList'] = 'Meeting'
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_code_ok(response)
    assert_scope_meeting(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_success_with_scope_list_task(get_headers,setup_data):
    setup_data['scopeList'] = 'Task'
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_code_ok(response)
    assert_scope_task(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_success_with_scope_list_call(get_headers, setup_data):
    setup_data['scopeList'] = 'Call'
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_code_ok(response)
    assert_scope_call(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_with_only_from_param(get_headers, setup_data):
    setup_data['to'] = ''
    setup_data['scopeList'] = ''
    setup_data['agenda'] = ''
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_with_only_to_param(get_headers, setup_data):
    setup_data['from'] = ''
    setup_data['scopeList'] = ''
    setup_data['agenda'] = ''
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

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
def test_get_activity_without_params(get_headers, setup_data):
    setup_data['from'] = ''
    setup_data['to'] = ''
    setup_data['scopeList'] = ''
    setup_data['agenda'] = ''
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_bad_request(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_with_agenda_empty(get_headers, setup_data):
    setup_data['agenda'] = ''
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_code_ok(response)
    assert_size_array(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
@pytest.mark.smoke
def test_get_activity_with_agenda_true(get_headers, setup_data):
    setup_data['agenda'] = 'true'
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_code_ok(response)
    assert_size_array(response)


@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_with_agenda_false(get_headers, setup_data):
    setup_data['agenda'] = 'false'
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_code_ok(response)
    assert_size_array(response)

@allure.feature('Activity - Nicole Muñoz')
@allure.story('Get activity')
@pytest.mark.functional
@pytest.mark.regression
def test_get_activity_with_agenda_any_value(get_headers, setup_data):
    setup_data['agenda'] = 'michi'
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers_params(url, params=setup_data, headers=headers)

    assert_status_code_ok(response)
    assert_size_array(response)
'''