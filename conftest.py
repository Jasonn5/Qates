import base64
import pytest

@pytest.fixture
def get_headers():
    def _get_headers(username, password):
        espo_authorization = encoded(username, password)
        return {
            'Espo-Authorization': espo_authorization
        }

    return _get_headers

def get_auth_headers(username, password):
    espo_authorization = encoded(username, password)
    return {
        'Espo-Authorization': espo_authorization
    }
def encoded(username, password):
    credentials = f'{username}:{password}'
    encode = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return encode