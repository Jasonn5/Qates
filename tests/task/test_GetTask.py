import pytest
import requests

from config import BASE_URI, USERNAME, PASSWORD, TASK_PARAM, TASK_PARAM_LIST
from src.assertions.assertion_status import assert_status_code_ok, assert_status_code_unauthorized, assert_status_code_internal_server_error, assert_status_code_method_not_allowed, assert_status_bad_request
from src.espocrm_api.task_ednpoints import EndpointTask
from src.assertions.assertion_schemas import assert_schema_task


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_task_success(get_headers):
    url = f"{BASE_URI}{EndpointTask.GET_TASK_WITH_PARAMS.value}{TASK_PARAM}"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    assert_status_code_ok(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_task_unauthorized():
    url = f"{BASE_URI}{EndpointTask.GET_TASK_WITHOUT_PARAMS.value}"
    response = requests.get(url)
    assert_status_code_unauthorized(response)


@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_task_invalid_auth(get_headers):
    url = f"{BASE_URI}{EndpointTask.GET_TASK_WITHOUT_PARAMS.value}"
    headers = get_headers("invalid_user", "invalid_password")
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_task_schema_validation(get_headers):
    url = f"{BASE_URI}{EndpointTask.GET_TASK_WITHOUT_PARAMS.value}"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    headers = response.headers
    assert_schema_task(response.json())

@pytest.mark.functional
@pytest.mark.regression
def test_get_task_success_filter(get_headers):
    url = f"{BASE_URI}{EndpointTask.GET_TASK_WITH_PARAMS.value}{TASK_PARAM}&maxSize=5&offset=0&orderBy=createdAt&order=desc&where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=tarea"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    assert_status_code_ok(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_task_list(get_headers):
    url = f"{BASE_URI}{EndpointTask.GET_TASK_IN_LIST.value}{TASK_PARAM_LIST}"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    assert_status_code_ok(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_tasks_with_invalid_page(get_headers):
    url = f"{BASE_URI}{EndpointTask.GET_TASK_WITHOUT_PARAMS.value}"
    headers = get_headers(USERNAME, PASSWORD)
    TASK_PARAM['offset'] = '-1'
    response = requests.get(url, params= TASK_PARAM, headers=headers)
    assert_status_code_internal_server_error(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_tasks_ordered_alphabetically_by_name(get_headers):
    TASK_PARAM.update({'orderBy': 'name', 'order': 'asc'})
    url = f"{BASE_URI}{EndpointTask.GET_TASK_WITH_PARAMS.value}"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    assert_status_code_ok(response)

@pytest.mark.functional
@pytest.mark.regression
def test_method_not_allowed():
    url = f"{BASE_URI}{EndpointTask.GET_TASK_WITHOUT_PARAMS.value}"
    response = requests.post(url)
    assert_status_code_method_not_allowed(response)


@pytest.mark.functional
@pytest.mark.regression
def test_get_tasks_invalid_order_parameter(get_headers):
    TASK_PARAM.update({'orderBy': 'invalid_field', 'order': 'invalid_order'})
    url = f"{BASE_URI}{EndpointTask.GET_TASK_WITHOUT_PARAMS.value}{TASK_PARAM}"
    headers = get_headers(USERNAME, PASSWORD)
    response = requests.get(url, params=TASK_PARAM, headers=headers)
    assert_status_bad_request(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_tasks_list_ordered_alphabetically_by_name(get_headers):
    TASK_PARAM_LIST.update({'orderBy': 'name', 'order': 'asc'})
    url = f"{BASE_URI}{EndpointTask.GET_TASK_WITH_PARAMS.value}"
    response = requests.get(url, headers=get_headers(USERNAME, PASSWORD))
    assert_status_code_ok(response)

@pytest.mark.functional
@pytest.mark.regression
def test_get_tasks_list_invalid_order_parameter(get_headers):
    TASK_PARAM_LIST.update({'orderBy': 'invalid_field', 'order': 'invalid_order'})
    url = f"{BASE_URI}{EndpointTask.GET_TASK_WITHOUT_PARAMS.value}{TASK_PARAM}"
    headers = get_headers(USERNAME, PASSWORD)
    response = requests.get(url, params=TASK_PARAM, headers=headers)
    assert_status_bad_request(response)