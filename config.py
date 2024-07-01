BASE_URI = 'https://espo.spartan-soft.com/api/v1'
USERNAME = "admin"
PASSWORD = "admin"
CALL_PARAM = {
    'select': 'assignedUserId%2CassignedUserName%2CdateStart%2Cstatus%2CparentId%2CparentType%2CparentName%2Cname',
    'maxsize': '20',
    'offset': '0',
    'orderBy': 'dateStart',
    'order': 'desc'
}

MEETING_PARAM = {
    'select': 'id,name,status,dateStart,dateEnd,dateStartDate,dateEndDate,parentId,parentType,parentName,createdById,assignedUserId,assignedUserName',
    'maxSize': '20',
    'offset': '0',
    'orderBy': 'dateStart',
    'order': 'asc'
}