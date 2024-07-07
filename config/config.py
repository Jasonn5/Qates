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

EndpointEmail = {
    'POST_EMAIL_DRAFT': '/Email',
    'GET_EMAIL_WITH_PARAMS': '/Email?maxSize=10'
}