from utils.api_client import APIClient

class LoginPage:
    def __init__(self, base_url):
        self.api_client = APIClient(base_url)

    def login(self, username, password):
        return self.api_client.get_login(username, password)
