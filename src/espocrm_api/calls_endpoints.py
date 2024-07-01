from enum import Enum

class EndpointCalls(Enum):
    GET_CALLS_WITHOUT_PARAMS = "/Call"
    GET_CALLS_WITH_PARAMS = "/Call?"