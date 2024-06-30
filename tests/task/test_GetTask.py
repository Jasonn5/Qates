from src.assertions.assertion_schemas import assert_schema_task
import requests
from config import  BASE_URI
from src.assertions.assertion_status import assert_status_code_ok, assert_status_code_unauthorized

def test_get_task_success(get_headers):
    url = f"{BASE_URI}/Kanban/Task?select=dateEnd%2CdateEndDate%2CparentId%2CparentType%2CparentName%2Cpriority%2Cname%2Cstatus&maxSize=5&offset=0&orderBy=createdAt&order=desc"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_status_code_ok(response)

def test_get_task_success_filter(get_headers):
    url = f"{BASE_URI}/Kanban/Task?select=dateEnd%2CdateEndDate%2CparentId%2CparentType%2CparentName%2Cpriority%2Cname%2Cstatus&maxSize=5&offset=0&orderBy=createdAt&order=desc&where%5B0%5D%5Btype%5D=textFilter&where%5B0%5D%5Bvalue%5D=tarea"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_status_code_ok(response)

def test_get_task_list(get_headers):
    url = f"{BASE_URI}/Task?select=createdAt%2CassignedUserId%2CassignedUserName%2CdateEnd%2CdateEndDate%2Cpriority%2Cstatus%2Cname&maxSize=20&offset=0&orderBy=createdAt&order=desc"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_status_code_ok(response)

def test_get_task_unauthorized():
    url = f"{BASE_URI}/Kanban/Task"
    response = requests.get(url)
    assert_status_code_unauthorized(response)

def test_get_task_invalid_auth(get_headers):
    url = f"{BASE_URI}/Kanban/Task"
    headers = get_headers("invalid_user", "invalid_password")
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

