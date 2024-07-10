import pytest
import allure

from api.params.task_params_list import *
from resources.auth.auth import Auth
from core.assertions.status import assert_status_code_ok, assert_status_code_unauthorized, assert_status_code_internal_server_error, assert_status_code_method_not_allowed, assert_status_bad_request
from core.assertions.schemas import assert_schema_task
from api.endpoints.task import TaskEnpoints
from api.request.api_request import EspoCRMRequest
from core.payloads.tasks.payload_tasks import payload_task
from tests.task.conftest import create_task, delete_task
from core.assertions.task import assert_task_exists_in_list


@allure.suite('EspoCRM')
@allure.sub_suite('Freddy')
@allure.epic('EspoCRM')
@allure.feature('Task')
@allure.story('Get Task')
@allure.tag('author: Freddy')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_task_success(get_headers):
    task = create_task(get_headers, payload_task)
    url = TaskEnpoints.get_task_with_params(TASK_PARAM_NORM)
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_ok(response)
    assert_task_exists_in_list(task['id'], response.json())
    delete_task(payload_task['id'], get_headers)



@allure.suite('EspoCRM')
@allure.sub_suite('Freddy')
@allure.epic('EspoCRM')
@allure.feature('Task')
@allure.story('Get Task')
@allure.tag('author: Freddy')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_task_unauthorized():
    url = TaskEnpoints.get_task_with_params(TASK_PARAM_NORM)
    response = EspoCRMRequest.get_with_url(url)
    assert_status_code_unauthorized(response)


@allure.suite('EspoCRM')
@allure.sub_suite('Freddy')
@allure.epic('EspoCRM')
@allure.feature('Task')
@allure.story('Get Task')
@allure.tag('author: Freddy')
@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_get_task_invalid_auth(get_headers):
    url = TaskEnpoints.get_task_with_params(TASK_PARAM_NORM)
    headers = Auth().auth_invalid_credentials(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url,headers)
    assert_status_code_unauthorized(response)


@allure.suite('EspoCRM')
@allure.sub_suite('Freddy')
@allure.epic('EspoCRM')
@allure.feature('Task')
@allure.story('Get Task')
@allure.tag('author: Freddy')
@pytest.mark.functional
@pytest.mark.regression
def test_get_task_schema_validation(get_headers):
    url = TaskEnpoints.get_task_with_params(TASK_PARAM_NORM)
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_schema_task(response.json())

@allure.suite('EspoCRM')
@allure.sub_suite('Freddy')
@allure.epic('EspoCRM')
@allure.feature('Task')
@allure.story('Get Task')
@allure.tag('author: Freddy')
@pytest.mark.functional
@pytest.mark.regression
def test_get_task_success_filter(get_headers):
    task = create_task(get_headers, payload_task)
    url = TaskEnpoints.get_task_with_params(TASK_PARAM_FILTER)
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_ok(response)
    assert_task_exists_in_list(task['id'], response.json())
    delete_task(payload_task['id'], get_headers)


@allure.suite('EspoCRM')
@allure.sub_suite('Freddy')
@allure.epic('EspoCRM')
@allure.feature('Task')
@allure.story('Get Task')
@allure.tag('author: Freddy')
@pytest.mark.functional
@pytest.mark.regression
def test_get_task_list(get_headers):
    task = create_task(get_headers, payload_task)
    url = TaskEnpoints.get_task_with_params(TASK_PARAM_LIST)
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_ok(response)
    assert_task_exists_in_list(task['id'], response.json())
    delete_task(payload_task['id'], get_headers)


@allure.suite('EspoCRM')
@allure.sub_suite('Freddy')
@allure.epic('EspoCRM')
@allure.feature('Task')
@allure.story('Get Task')
@allure.tag('author: Freddy')
@pytest.mark.functional
@pytest.mark.regression
def test_get_tasks_ordered_alphabetically_by_name(get_headers):
    task = create_task(get_headers, payload_task)
    url = TaskEnpoints.get_task_with_params(TASK_PARAM_ORD)
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url, headers)
    assert_status_code_ok(response)
    assert_task_exists_in_list(task['id'], response.json())
    delete_task(payload_task['id'], get_headers)

@allure.suite('EspoCRM')
@allure.sub_suite('Freddy')
@allure.epic('EspoCRM')
@allure.feature('Task')
@allure.story('Get Task')
@allure.tag('author: Freddy')
@pytest.mark.functional
@pytest.mark.regression
def test_method_not_allowed(get_headers):
    url = TaskEnpoints.get_task_with_params(TASK_PARAM_NORM)
    headers = Auth().auth_valid_credential(get_headers)
    response_post = EspoCRMRequest.post(url, headers, payload_task)
    response_delete = EspoCRMRequest.delete(url, headers)
    assert_status_code_method_not_allowed(response_post)
    assert_status_code_method_not_allowed(response_delete)
    '''
        Este error se encuentra reportado en el BUG-108
    '''


@allure.suite('EspoCRM')
@allure.sub_suite('Freddy')
@allure.epic('EspoCRM')
@allure.feature('Task')
@allure.story('Get Task')
@allure.tag('author: Freddy')
@pytest.mark.functional
@pytest.mark.regression
def test_get_tasks_list_ordered_alphabetically_by_name(get_headers):
    task = create_task(get_headers, payload_task)
    url = TaskEnpoints.get_task_list_with_params(TASK_PARAM_ORD)
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.get_with_url_headers(url,headers)
    assert_status_code_ok(response)
    assert_task_exists_in_list(task['id'], response.json())
    delete_task(payload_task['id'], get_headers)