import pytest
import base64

@pytest.fixture
def get_headers():
    def _get_headers(username, password):
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        return {
            'Authorization': f'Basic {encoded_credentials}',
            'Cookie': 'auth-token-secret=b51d5dc9ee9eafa0aaa329612425ad63; auth-token=288eacade0b7e816569a85a5d07f165a'
        }
    return _get_headers
