import requests
import base64

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_login(self, username, password):
        url = f'{self.base_url}/App/user'
        espo_authorization = self._encode_credentials(username, password)
        headers = {
            'Espo-Authorization': espo_authorization,
            'content-type': 'application/json'
        }

        response = requests.get(url, headers=headers)
        return response

    def _encode_credentials(self, username, password):
        credentials = f'{username}:{password}'
        encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        return encoded_credentials
