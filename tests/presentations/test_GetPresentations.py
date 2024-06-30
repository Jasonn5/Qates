from src.assertions.assertion_schemas import assert_schema_presentation
import requests
from config import BASE_URI
from src.assertions.assertion_status import assert_status_code_ok, assert_status_code_unauthorized
from src.assertions.assertion_content import assert_content_type_json
from src.assertions.assertion_comparison import *


def test_get_meetings_success(get_headers):
    url = f"{BASE_URI}/Meeting?select=id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName&maxSize=20&offset=0&orderBy=dateStart&order=desc"
    response = requests.get(url, headers=get_headers("jeyson", "Testing.123!"))
    assert_status_code_ok(response)

def test_get_meetings_schema_validation(get_headers):
    url = f"{BASE_URI}/Meeting?select=id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName&maxSize=20&offset=0&orderBy=dateStart&order=desc"
    response = requests.get(url, headers=get_headers("jeyson", "Testing.123!"))
    assert_schema_presentation(response.json())

def test_get_meetings_response_format(get_headers):
    url = f"{BASE_URI}/Meeting?select=id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName&maxSize=20&offset=0&orderBy=dateStart&order=desc"
    response = requests.get(url, headers=get_headers("jeyson", "Testing.123!"))
    assert_content_type_json(response)

def test_get_meetings_max_size(get_headers):
    max_size = 1
    url = f"{BASE_URI}/Meeting?select=id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName&maxSize={max_size}&offset=0&orderBy=dateStart&order=desc"
    response = requests.get(url, headers=get_headers("jeyson", "Testing.123!"))
    data = response.json()['list']
    assert_less_than_or_equal_to(len(data), max_size)

def test_get_meetings_unauthorized():
    url = f"{BASE_URI}/Meeting"
    response = requests.get(url)
    assert_status_code_unauthorized(response)

def test_get_meetings_invalid_auth(get_headers):
    url = f"{BASE_URI}/Meeting"
    headers = get_headers("invalid_user", "invalid_password")
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)
