from core.config.config import BASE_URI


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
    def delete_call(id_call) -> str:
        return f"{BASE_URI}/Call/{id_call}"

    @staticmethod
    def gel_call_by_id(id_call) -> str:
        return f"{BASE_URI}/Call/{id_call}"

    @staticmethod
    def delete_call_more_than_one_call() -> str:
        return f"{BASE_URI}/MassAction"


