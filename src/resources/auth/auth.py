from src.utils.load_resources import load_credential_resource
class Auth:
    def __init__(self):
        self.users = self.load_file()

    @staticmethod
    def load_file():
        return load_credential_resource("user.json")

    def get_user(self, user_type):
        return self.users.get(user_type)

    def auth_valid_credential(self, get_headers):
        user = self.get_user("valid_credentials")
        return get_headers(user["username"], user["password"])

    def auth_invalid_username(self, get_headers):
        user = self.get_user("invalid_username")
        return get_headers(user["username"], user["password"])

    def auth_invalid_password(self, get_headers):
        user = self.get_user("invalid_password")
        return get_headers(user["username"], user["password"])

    def auth_invalid_credentials(self, get_headers):
        user = self.get_user("invalid_credentials")
        return get_headers(user["username"], user["password"])

    def auth_empty_fields(self, get_headers):
        user = self.get_user("empty_fields")
        return get_headers(user["username"], user["password"])

    def auth_empty_user(self, get_headers):
        user = self.get_user("empty_username")
        return get_headers(user["username"], user["password"])

    def auth_empty_password(self, get_headers):
        user = self.get_user("empty_password")
        return get_headers(user["username"], user["password"])
