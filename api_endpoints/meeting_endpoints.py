from config.config import BASE_URI

class MeetingEndpoints:
    @staticmethod
    def get_meeting_without_params() -> str:
        return f"{BASE_URI}/Meeting"

    @staticmethod
    def get_meeting_with_params(params) -> str:
        return f"{BASE_URI}/Meeting?{params}"

    @staticmethod
    def get_meeting_by_id(meeting_id):
        return f"{BASE_URI}/Meeting/{meeting_id}"

    @staticmethod
    def create_meeting() -> str:
        return f"{BASE_URI}/Meeting"

    @staticmethod
    def delete_meeting(meeting_id) -> str:
        return f"{BASE_URI}/Meeting/{meeting_id}"
