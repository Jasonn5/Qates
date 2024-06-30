from src.assertions.assertion_schemas import assert_schema_correoImportant
import requests
from config import BASE_URI
from src.assertions.assertion_status import assert_status_code_ok, assert_status_code_unauthorized


def test_get_email_succed(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent%2CparentId%2CparentType%2CparentName%2Csubject%2CpersonStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where%5B0%5D%5Btype%5D=inFolder&where%5B0%5D%5Battribute%5D=folderId&where%5B0%5D%5Bvalue%5D=important"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_status_code_ok(response)

def test_get_email_response_format(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent%2CparentId%2CparentType%2CparentName%2Csubject%2CpersonStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where%5B0%5D%5Btype%5D=inFolder&where%5B0%5D%5Battribute%5D=folderId&where%5B0%5D%5Bvalue%5D=important"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert response.headers['Content-Type'] == 'application/json'

def test_get_email_schema_validation(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent%2CparentId%2CparentType%2CparentName%2Csubject%2CpersonStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where%5B0%5D%5Btype%5D=inFolder&where%5B0%5D%5Battribute%5D=folderId&where%5B0%5D%5Bvalue%5D=important"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_schema_correoImportant(response.json())
    print(response.json())

def test_get_mail_invalid_order_parameter(get_headers):
        url = f"{BASE_URI}/Email?select=dateSent%2Csubject%2CfromName&maxSize=20&offset=0&orderBy=dateSent&order=invalidOrder"
        response = requests.get(url, headers=get_headers("admin", "admin"))
        assert response.status_code == 400

def test_get_mail_valid_maxsize_parameter(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent%2Csubject%2CfromName&maxSize=1&offset=0&orderBy=dateSent&order=desc"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_status_code_ok(response)

def test_get_mail_missing_auth_token_secret():
    url = f"{BASE_URI}/Email"
    headers = {"Cookie": "some_other_cookie=some_value"}
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

def test_get_mail_valid_offset_parameter(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent%2Csubject%2CfromName&maxSize=20&offset=1000&orderBy=dateSent&order=desc"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_status_code_ok(response)

def test_get_mail_invalid_basic_authorization():
    url = f"{BASE_URI}/Email"
    headers = {"Authorization": "Basic invalidcredentials"}
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

def test_get_mail_missing_auth_token_secret():
    url = f"{BASE_URI}/Email"
    headers = {"Cookie": "some_other_cookie=some_value"}
    response = requests.get(url, headers=headers)
    assert_status_code_unauthorized(response)

def test_get_mail_invalid_order_parameter(get_headers):
    url = f"{BASE_URI}/Email?select=dateSent%2Csubject%2CfromName&maxSize=20&offset=0&orderBy=dateSent&order=invalidOrder"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert response.status_code == 400