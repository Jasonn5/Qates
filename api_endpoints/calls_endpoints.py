from enum import Enum

from config.config import BASE_URI


class EndpointCalls:
    @staticmethod
    def get_call_without_params() -> str:
        return f"{BASE_URI}/Call"

    @staticmethod
    def get_call_with_params() -> str:
        return f"{BASE_URI}/Call?"

    @staticmethod
    def post_call() -> str:
        return f"{BASE_URI}/Call"

    @staticmethod
    def delete_call() -> str:
        return f"{BASE_URI}/Call"


