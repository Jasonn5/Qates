BASE_URI = 'https://espo.spartan-soft.com/api/v1'
USERNAME = "admin"
PASSWORD = "admin"

CALL_PARAM = {
    'select': 'id%2Cname%2Cdeleted%2Cstatus%2CdateStart%2CdateEnd%2Cduration%2Cdirection%2Cdescription%2CcreatedAt"%2CmodifiedAt%2CparentId%2CparentType%2CparentName%2CaccountId%2CaccountName%2CcreatedById%2CcreatedByName%2CmodifiedById"%2CmodifiedByName%2CassignedUserId%2CassignedUserName',
    'maxsize': '20',
    'offset': '0',
    'orderBy': 'dateStart',
    'order': 'desc'
}

TASK_PARAM = {
    'select': 'dateEnd%2CdateEndDate%2CparentId%2CparentType%2CparentName%2Cpriority%2Cname%2Cstatus',
    'maxsize': '5',
    'offset': '0',
    'orderBy': 'createdAt',
    'order': 'desc'
}

TASK_PARAM_LIST = {
    'select': 'createdAt%2CassignedUserId%2CassignedUserName%2CdateEnd%2CdateEndDate%2Cpriority%2Cstatus%2Cname',
    'maxsize': '20',
    'offset': '0',
    'orderBy': 'createdAt',
    'order': 'desc'
}

MEETING_PARAM = {
    'select': 'id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName',
    'maxSize': '20',
    'offset': '0',
    'orderBy': 'dateStart',
    'order': 'asc'
}

ACTIVITIES_PARAM = {
    'from': '2024-06-24 04:00',
    'to': '2024-07-01 04:00',
}


EMAIL_IMPORTANT_PARAM = {
    'select': 'id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName',
    'maxSize': '20',
    'offset': '0',
    'orderBy': 'dateStart',
    'order': 'asc'
}

CALL_REQUIRED_AND_OPTIONAL_DATA = {
    "status": "Planned",
    "dateStart": "2024-07-07 02:45:00",
    "duration": 300,
    "direction": "Outbound",
    "assignedUserId": "66744ee8d0ffd7849",
    "assignedUserName": "Admin",
    "acceptanceStatus": "None",
    "dateEnd": "2024-07-07 02:50:00",
    "name": "Llamada required and optional",
    "parentType": "Account",
    "parentName": "Real Home",
    "parentId": "667b9d7255e8ccf64",
    "reminders": [
        {
            "type": "Popup",
            "seconds": 0
        }
    ],
    "description": "Descripción de llamada",
    "teamsIds": [
        "6676272ac68b8f1ba",
        "667885ad7e952a085",
        "668742a5d9c7db1bf"
    ],
    "teamsNames": {
        "6676272ac68b8f1ba": "Equipo 6",
        "667885ad7e952a085": "equipo 7",
        "668742a5d9c7db1bf": "Equipo21"
    },
    "usersIds": [
        "667620f85938976bd",
        "66788c2cd22ae27a3",
        "66788c001d3b51e97"
    ],
    "usersNames": {
        "667620f85938976bd": "David Pérez",
        "66788c2cd22ae27a3": "Diego Acosta",
        "66788c001d3b51e97": "Eddy Montano"
    },
    "usersColumns": {
        "667620f85938976bd": {
            "status": "Accepted"
        },
        "66788c2cd22ae27a3": {
            "status": "Tentative"
        },
        "66788c001d3b51e97": {
            "status": "Declined"
        }
    },
    "contactsIds": [
        "668a01bb35411ec94",
        "6689e3d32ac770025"
    ],
    "contactsNames": {
        "668a01bb35411ec94": "Maddy Test",
        "6689e3d32ac770025": "bety pinzon"
    },
    "contactsColumns": {
        "668a01bb35411ec94": {
            "status": "Accepted"
        },
        "6689e3d32ac770025": {
            "status": "Tentative"
        }
    },
    "leadsIds": [
        "667b9c285193dbb98"
    ],
    "leadsNames": {
        "667b9c285193dbb98": "Alison Guzman"
    },
    "leadsColumns": {
        "667b9c285193dbb98": {
            "status": "Accepted"
        }
    }
}

