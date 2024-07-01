from enum import Enum

class EndpointTask(Enum):
    GET_TASK_WITHOUT_PARAMS = "/Kanban/Task"
    GET_TASK_WITH_PARAMS = "/Kanban/Task?"
    GET_TASK_IN_LIST = "/Task?"