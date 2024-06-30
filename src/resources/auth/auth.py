from src.utils.load_resources import load_credential_resource
class Auth:
    def __init__(self):
        self.users = self.load_file()

    @staticmethod
    def load_file():
        return load_credential_resource("users.json")

    def get_user(self, user_type):
        return self.users.get(user_type)

    @staticmethod
    def auth_valid_credential(self, get_headers):
        user = self.get_user("valid_credentials")
        return get_headers(user["username"], user["password"])
