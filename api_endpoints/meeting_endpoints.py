from config.config import BASE_URI

class MeetingEndpoints:
    @staticmethod
    def get_meeting_without_params() -> str:
        return f"{BASE_URI}/Meeting"

    @staticmethod
    def get_meeting_with_params(params: str) -> str:
        return f"{BASE_URI}/Meeting?{params}"

    @staticmethod
    def create_meeting() -> str:
        return f"{BASE_URI}/Meeting"

    @staticmethod
    def update_meeting(meeting_id: str) -> str:
        return f"{BASE_URI}/Meeting/{meeting_id}"

    @staticmethod
    def delete_meeting(meeting_id: str) -> str:
        return f"{BASE_URI}/Meeting/{meeting_id}"
