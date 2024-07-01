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