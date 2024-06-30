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

def test_get_meetings_pagination(get_headers):
    offset = 1
    max_size = 2
    url_with_offset = f"{BASE_URI}/Meeting?select=id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName&maxSize={max_size}&offset={offset}&orderBy=dateStart&order=desc"
    url_without_offset = f"{BASE_URI}/Meeting?select=id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName&maxSize={max_size}&offset=0&orderBy=dateStart&order=desc"
    headers = get_headers("jeyson", "Testing.123!")
    response_with_offset = requests.get(url_with_offset, headers=headers)
    response_without_offset = requests.get(url_without_offset, headers=headers)

    assert_status_code_ok(response_with_offset)
    assert_status_code_ok(response_without_offset)

    data_with_offset = response_with_offset.json()
    data_without_offset = response_without_offset.json()

    data_list_with_offset = data_with_offset["list"]
    data_list_without_offset = data_without_offset["list"]

    assert_less_than_or_equal_to(len(data_list_with_offset), max_size)

    if len(data_list_without_offset) > offset:
        expected_first_item_with_offset = data_list_without_offset[offset]
        actual_first_item_with_offset = data_list_with_offset[0]
        assert_equal_to(actual_first_item_with_offset["id"], expected_first_item_with_offset["id"])


def test_get_meetings_order_desc(get_headers):
    url = f"{BASE_URI}/Meeting?select=id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName&maxSize=20&offset=0&orderBy=dateStart&order=desc"
    response = requests.get(url, headers=get_headers("jeyson", "Testing.123!"))

    assert_status_code_ok(response)

    data = response.json()
    meetings_list = data["list"]
    dates = [item['dateStart'] for item in meetings_list]

    assert_equal_to(dates, sorted(dates, reverse=True))