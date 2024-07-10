TASK_PARAM_LIST = {
    'select': 'createdAt%2CassignedUserId%2CassignedUserName%2CdateEnd%2CdateEndDate%2Cpriority%2Cstatus%2Cname',
    'maxsize': '20',
    'offset': '0',
    'orderBy': 'createdAt',
    'order': 'desc'
}
TASK_PARAM_NORM = {
    'select': 'dateEnd%2CdateEndDate%2CparentId%2CparentType%2CparentName%2Cpriority%2Cname%2Cstatus',
    'maxSize': '5',
    'offset': '0',
    'orderBy': 'createdAt',
    'order': 'desc'
}
TASK_PARAM_FILTER = {
    'select': 'dateEnd%2CdateEndDate%2CparentId%2CparentType%2CparentName%2Cpriority%2Cname%2Cstatus',
    'maxSize': '5',
    'offset': '0',
    'orderBy': 'createdAt',
    'order': 'desc',
    'where[0][type]': 'textFilter',
    'where[0][value]': 'tarea'
}

TASK_PARAM_ORD = {
    'select': 'dateEnd%2CdateEndDate%2CparentId%2CparentType%2CparentName%2Cpriority%2Cname%2Cstatus',
    'maxSize': '5',
    'offset': '0',
    'orderBy': 'name',
    'order': 'asc'
}
