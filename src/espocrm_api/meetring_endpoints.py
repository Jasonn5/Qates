from enum import Enum

class EndpointMeetings(Enum):
    GET_MEETINGS_WITHOUT_PARAMS = "/Meeting"
    GET_MEETINGS_WITH_PARAMS = "/Meeting?"
