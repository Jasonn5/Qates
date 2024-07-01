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
EMAIL_IMPORTAN_PARAM = {
    "select": "dateSent,parentId,parentType,parentName,subject,personStringData",
    "maxSize": 20,
    "offset": 0,
    "orderBy": "dateSent",
    "order": "desc",
    "where[0][type]": "inFolder",
    "where[0][attribute]": "folderId",
    "where[0][value]": "important"
}