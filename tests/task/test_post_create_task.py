import pytest

from api_endpoints.api_request import EspoCRMRequest
from assertions.assertion_status import assert_status_code_ok, assert_status_bad_request, assert_status_code_unauthorized, assert_status_code_method_not_allowed
from api_endpoints.task_ednpoints import TaskEnpoints
from tests.task.conftest import delete_task
from resources.auth.auth import Auth
from payloads.tasks.payload_tasks import payload_task

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_post_task_success(get_headers):
    url = TaskEnpoints.post_task_without_params()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post(url, headers, payload_task)
    assert_status_code_ok(response)
    delete_task(payload_task['id'], get_headers)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_post_task_missing_required_fields(get_headers):
    url = TaskEnpoints.post_task_without_params()
    headers = Auth().auth_valid_credential(get_headers)
    payload_task.update({'name': " "})
    response = EspoCRMRequest.post(url, headers, payload_task)
    assert_status_bad_request(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_post_task_no_authorization(get_headers):
    url = TaskEnpoints.post_task_without_params()
    headers = Auth().auth_empty_fields(get_headers)
    response = EspoCRMRequest.post(url, headers, payload_task)
    assert_status_code_unauthorized(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_post_task_invalid_token(get_headers):
    url = TaskEnpoints.post_task_without_params()
    headers = Auth().auth_invalid_credentials(get_headers)
    response = EspoCRMRequest.post(url, headers, payload_task)
    assert_status_code_unauthorized(response)

@pytest.mark.functional
@pytest.mark.regression
def test_method_not_allowed(get_headers):
    url = TaskEnpoints.post_task_without_params()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_method_not_allowed(response)

'''@pytest.mark.functional
@pytest.mark.regression
def test_post_task_schema_payload(get_headers):
    url = TaskEnpoints.post_task_without_params()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post(url, headers, payload_task)
    assert_payload_schema_task(response.json())'''

'''@pytest.mark.functional
@pytest.mark.regression
def test_post_task_missing_optional_fields(get_headers):
    url = TaskEnpoints.post_task_without_params()
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.post(url, headers, payload_task)
    assert_status_code_ok(response)
    delete_task(payload_task['id'], get_headers)'''

'''@pytest.mark.functional
@pytest.mark.regression
def test_post_task_duplicate_creation(setup_teardown_task, get_headers):
    response = setup_teardown_task
    assert_status_bad_request(response)'''
