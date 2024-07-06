BASE_URI = 'https://espo.spartan-soft.com/api/v1'
USERNAME = "admin"
PASSWORD = "admin"

CALL_PARAM = {
    'select': 'id,name,deleted,status,dateStart,dateEnd,duration,direction,description,createdAt,modifiedAt,parentId,parentType,parentName,accountId,accountName,createdById,createdByName,modifiedById,modifiedByName,assignedUserId,assignedUserName',
    'maxsize': '20',
    'offset': '0',
    'orderBy': 'dateStart',
    'order': 'desc'
}

TASK_PARAM = {
    'select': 'dateEnd,dateEndDate,parentId,parentType,parentName,priority,name,status',
    'maxsize': '5',
    'offset': '0',
    'orderBy': 'createdAt',
    'order': 'desc'
}

TASK_PARAM_LIST = {
    'select': 'createdAt,assignedUserId,assignedUserName,dateEnd,dateEndDate,priority,status,name',
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
    'to': '2024-07-01 04:00'
}
