from src.assertions.assertion_schemas import assert_schema_presentation
import requests
from config import  BASE_URI
from src.assertions.assertion_status import assert_status_code_ok, assert_status_code_unauthorized


def test_get_email_succed(get_headers):
    url = f"{BASE_URI}/Email?select=2CparentType&maxSize=20&offset=0&order=desc&where%5B0%5D%5Btype%5D=inFolder&where%5B0%5D%5Battribute%5D=folderId&where%5B0%5D%5Bvalue%5D=drafts"
    response = requests.get(url, headers=get_headers("admin", "admin"))
    assert_status_code_ok(response)
