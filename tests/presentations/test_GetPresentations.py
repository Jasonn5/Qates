from src.assertions.assetrion_schemas import assert_schema_presentation
import requests
from config import  BASE_URI


def test_get_meetings_success(get_headers):
    url = f"{BASE_URI}/Meeting?select=id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName&maxSize=20&offset=0&orderBy=dateStart&order=desc"
    response = requests.get(url, headers=get_headers("jeyson", "Testing.123!"))
    assert_schema_presentation(response.json())