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

