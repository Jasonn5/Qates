from api_endpoints.api_request import EspoCRMRequest
from assertions.assertion_status import assert_status_code_ok


def test_get_contact_success(get_header_cookie):
    url = "https://espo.spartan-soft.com/api/v1/Contact/6685c148248c8b75d"
    headers = get_header_cookie("admin", "admin")
    response = EspoCRMRequest.get_with_url_headers(url, headers=headers)

    assert_status_code_ok(response)  # Verificar que el código de estado sea 200 OK

