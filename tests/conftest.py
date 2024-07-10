import base64
import pytest
@pytest.fixture
def get_headers():
    def _get_headers(username, password):
        espo_authorization = encoded(username, password)
        return {
            'Espo-Authorization': espo_authorization,
            'Cookie': 'auth-token-secret=b51d5dc9ee9eafa0aaa329612425ad63; auth-token=288eacade0b7e816569a85a5d07f165a'
        }
    return _get_headers

def encoded(username, password):
    credentials = f'{username}:{password}'
    encode = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return encode

@pytest.fixture
def get_header_cookie():
    def _get_headers_withCookie_and_auth(username, password):
        encodedAuth = encoded(username, password)
        return {
            'Authorization': 'Basic ' + encodedAuth,
            'Cookie': 'auth-token-secret=b51d5dc9ee9eafa0aaa329612425ad63; auth-token=288eacade0b7e816569a85a5d07f165a'
        }
    return _get_headers_withCookie_and_auth
