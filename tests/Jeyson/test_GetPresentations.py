import requests
import pytest
from jsonschema import validate
from test_login import get_auth_headers, BASE_URI

meeting_schema = {
    "type": "object",
    "properties": {
        "total": {
            "type": "integer"
        },
        "list": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "status": {"type": "string"},
                    "dateStart": {"type": "string"},
                    "dateEnd": {"type": "string"},
                    "dateStartDate": {"type": ["null", "string"]},
                    "dateEndDate": {"type": ["null", "string"]},
                    "parentId": {"type": ["string", "null"]},
                    "parentType": {"type": ["string", "null"]},
                    "parentName": {"type": ["string", "null"]},
                    "createdById": {"type": "string"},
                    "assignedUserId": {"type": "string"},
                    "assignedUserName": {"type": "string"}
                },
                "required": [
                    "id", "name", "status", "dateStart", "dateEnd",
                    "dateStartDate", "dateEndDate", "parentId", "parentType",
                    "parentName", "createdById", "assignedUserId", "assignedUserName"
                ]
            }
        }
    },
    "required": ["total", "list"]
}


@pytest.fixture
def auth_headers():
    return get_auth_headers("jeyson", "Testing.123!")

def test_get_meetings_success(auth_headers):
    url = f"{BASE_URI}/Meeting?select=id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName&maxSize=20&offset=0&orderBy=dateStart&order=desc"
    response = requests.get(url, headers=auth_headers)
    assert response.status_code == 200

def  test_get_meetings_schema_validation(auth_headers):
    url = f"{BASE_URI}/Meeting?select=id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName&maxSize=20&offset=0&orderBy=dateStart&order=desc"
    response = requests.get(url, headers=auth_headers)
    assert response.status_code == 200

    validate(instance=response.json(), schema=meeting_schema)

def test_get_meetings_response_format(auth_headers):
    url = f"{BASE_URI}/Meeting?select=id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName&maxSize=20&offset=0&orderBy=dateStart&order=desc"
    response = requests.get(url, headers=auth_headers)
    assert response.headers['Content-Type'] == 'application/json'


def test_get_meetings_unauthorized():
    url = f"{BASE_URI}/Meeting"
    response = requests.get(url)
    assert response.status_code == 401

