from enum import Enum

class EndpointTask(Enum):
    GET_TASK_WITHOUT_PARAMS = "/Kanban/Task"
    GET_TASK_WITH_PARAMS = "/Kanban/Task?"
    GET_TASK_IN_LIST = "/Task?"
    POST_TASK_WITHOUT_PARAMS = "/Task"

from config.config import BASE_URI

class TaskEnpoints:
    @staticmethod
    def get_task_without_params() -> str:
        return f"{BASE_URI}/Kanban/Task"

    @staticmethod
    def get_task_with_params(params: str) -> str:
        return f"{BASE_URI}/Kanban/Task?{params}"

    @staticmethod
    def get_task_in_list() -> str:
        return f"{BASE_URI}/Task?"

    @staticmethod
    def post_task_without_params() -> str:
        return f"{BASE_URI}/Task"