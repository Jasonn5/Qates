import requests
from config import BASE_URI
from src.assertions.assertion_status import (
    assert_status_code_ok,
    assert_status_code_unauthorized,
    assert_status_bad_request
)


def test_get_email_succed(get_headers):
    url = f"{BASE_URI}/Email?select=2CparentType&maxSize=20&offset=0&order=desc&where%5B0%5D%5Btype%5D=inFolder&where%5B0%5D%5Battribute%5D=folderId&where%5B0%5D%5Bvalue%5D=drafts"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_status_code_ok(response)

def test_get_all_drafts_status_code_200(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts"
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

def test_get_drafts_with_wrong_basic_auth(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts"
    headers = get_headers("wrong", "credentials")
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

#Is a bug?
def test_get_drafts_without_auth_token_secret(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts"
    headers = get_headers("admin", "admin")
    if "cookie" in headers:
        headers.pop("cookie")
    response = requests.get(url, headers=headers)
    print(f"Request Headers: {response.request.headers}")
    print(f"Request URL: {response.request.url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    assert_status_code_unauthorized(response)
#Is a bug?
def test_get_drafts_with_wrong_content_type(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts"
    headers = get_headers("admin", "admin")
    headers["Content-Type"] = "text/plain"
    response = requests.get(url, headers=headers)
    print(f"Request Headers: {response.request.headers}")
    print(f"Request URL: {response.request.url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    assert_status_bad_request(response)

#Is a bug?
def test_get_drafts_with_additional_parameters(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts&extra_param=value"
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    print(f"Request Headers: {response.request.headers}")
    print(f"Request URL: {response.request.url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    assert_status_bad_request(response)

def test_get_drafts_with_empty_search_param(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts&search="
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

#Is a bug?
def test_get_drafts_with_invalid_search_fields(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts&search=invalid_field"
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    print(f"Request Headers: {response.request.headers}")
    print(f"Request URL: {response.request.url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    assert_status_bad_request(response)

def test_get_drafts_with_empty_maxsize_param(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=&offset=0&orderBy=dateSent&order=desc&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts"
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

def test_get_drafts_with_valid_maxsize_param(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=10&offset=0&orderBy=dateSent&order=desc&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts"
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert_status_code_ok(response)

#Is a bug?
def test_get_drafts_with_invalid_maxsize_param(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=invalid&offset=0&orderBy=dateSent&order=desc&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts"
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    print(f"Request Headers: {response.request.headers}")
    print(f"Request URL: {response.request.url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    assert_status_bad_request(response)

#Is a bug?
def test_get_drafts_with_invalid_offset_type(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=20&offset=not_an_integer&orderBy=dateSent&order=desc&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts"
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    print(f"Request Headers: {response.request.headers}")
    print(f"Request URL: {response.request.url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    assert_status_bad_request(response)

def test_get_drafts_with_invalid_order_type(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=20&offset=0&orderBy=dateSent&order=invalid&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts"
    headers = get_headers("admin", "admin")
    response = requests.get(url, headers=headers)
    assert_status_bad_request(response)
