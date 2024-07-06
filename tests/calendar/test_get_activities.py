import pytest

from tests.conftest import get_headers
from assertions.assertion_calendar import assert_scope_meeting, assert_scope_task, assert_scope_call
from assertions.assertion_content import assert_empty_array, assert_size_array
from assertions.assertion_schemas import assert_schema_activity
import requests
from config.config import BASE_URI, ACTIVITIES_PARAM
from assertions.assertion_status import assert_status_code_ok, assert_status_bad_request
from api_endpoints.activities_endpoints import ActivitiesEndpoint

url = f"{BASE_URI}{ActivitiesEndpoint.MAIN_ROUTE.value}?"

@pytest.mark.regression
def test_get_activity_success(get_headers):
    headers = get_headers("admin", "admin")
    response = requests.get(url, params=ACTIVITIES_PARAM, headers=headers)
    assert_status_code_ok(response)

@pytest.mark.regression
def test_get_activity_empty_from(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['from'] = ''
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_bad_request(response)

@pytest.mark.regression
def test_get_activity_invalid_from(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['from'] = 'michi'
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_bad_request(response)

@pytest.mark.functional
def test_get_activity_scopeListEmpty(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['scopeList'] = ''
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_empty_array(response)

@pytest.mark.regression
def test_get_activity_invalid_to(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['to'] = 'abcdefg'
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_bad_request(response)

@pytest.mark.regression
def test_get_activity_empty_to(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['to'] = ''
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_bad_request(response)

@pytest.mark.regression
def test_get_activity_success_with_scopeList_meeting(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['scopeList'] = 'Meeting'
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_scope_meeting(response)

@pytest.mark.regression
def test_get_activity_success_with_scopeList_task(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['scopeList'] = 'Task'
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_scope_task(response)

@pytest.mark.regression
def test_get_activity_success_with_scopeList_call(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['scopeList'] = 'Call'
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_scope_call(response)

@pytest.mark.functional
def test_get_activity_with_only_from_param(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['to'] = ''
    test_params['scopeList'] = ''
    test_params['agenda'] = ''
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_bad_request(response)

@pytest.mark.functional
def test_get_activity_with_only_to_param(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['from'] = ''
    test_params['scopeList'] = ''
    test_params['agenda'] = ''
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_bad_request(response)


@pytest.mark.smoke
def test_get_activity_schema_validation(get_headers):
    headers = get_headers("admin", "admin")
    response = requests.get(url, params=ACTIVITIES_PARAM, headers=headers)
    assert_schema_activity(response.json())

@pytest.mark.functional 
def test_get_activity_without_params(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['from'] = ''
    test_params['to'] = ''
    test_params['scopeList'] = ''
    test_params['agenda'] = ''
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_bad_request(response)

@pytest.mark.functional
def test_get_activity_with_agenda_empty(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['agenda'] = ''
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_size_array(response)

@pytest.mark.functional
def test_get_activity_with_agenda_true(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['agenda'] = 'true'
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_size_array(response)

@pytest.mark.functional
def test_get_activity_with_agenda_false(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['agenda'] = 'false'
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_size_array(response)

@pytest.mark.functional
def test_get_activity_with_agenda_any_value(get_headers):
    headers = get_headers("admin", "admin")
    test_params = ACTIVITIES_PARAM.copy()
    test_params['agenda'] = 'michi'
    response = requests.get(url, params=test_params, headers=headers)
    assert_status_code_ok(response)
    assert_size_array(response)
