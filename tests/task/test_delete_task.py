'''import pytest

from api.request.api_request import EspoCRMRequest
from core.assertions.status import assert_status_code_ok, assert_status_code_unauthorized, assert_status_code_not_found
from api.endpoints.task import TaskEnpoints
from tests.task.conftest import create_task
from resources.auth.auth import Auth
from core.payloads.tasks.payload_tasks import payload_task

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_task_success(get_headers):
    task = create_task(get_headers, payload_task)
    url = f"{TaskEnpoints.post_task_without_params()}/{task['id']}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_ok(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_task_no_existent_id(get_headers):
    nonexistent_task_id = "nonexistent-id-123456"
    url = f"{TaskEnpoints.post_task_without_params()}/{nonexistent_task_id}"
    headers = Auth().auth_valid_credential(get_headers)
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_not_found(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_task_no_authorization(get_headers):
    url = f"{TaskEnpoints.post_task_without_params()}/{payload_task['id']}"
    headers = Auth().auth_empty_fields(get_headers)
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_unauthorized(response)

@pytest.mark.smoke
@pytest.mark.functional
@pytest.mark.regression
def test_delete_task_invalid_token(get_headers):
    url = f"{TaskEnpoints.post_task_without_params()}/{payload_task['id']}"
    headers = Auth().auth_invalid_credentials(get_headers)
    response = EspoCRMRequest.delete(url, headers)
    assert_status_code_unauthorized(response)
'''
