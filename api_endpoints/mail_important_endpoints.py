from enum import Enum

class EndpointCorreoImportant(Enum):
    GET_CORREO_IMPORTANT = "/Email?select=dateSent%2CparentId%2CparentType%2CparentName%2Csubject%2CpersonStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where%5B0%5D%5Btype%5D=inFolder&where%5B0%5D%5Battribute%5D=folderId&where%5B0%5D%5Bvalue%5D=important"
    GET_CORREO_INVALID_ORDER = "/Email?select=dateSent%2Csubject%2CfromName&maxSize=20&offset=0&orderBy=dateSent&order=invalidOrder"
    GET_CORREO_MAXSIZE_1 = "/Email?select=dateSent%2Csubject%2CfromName&maxSize=1&offset=0&orderBy=dateSent&order=desc"
    GET_CORREO_OFFSET_1000 = "/Email?select=dateSent%2Csubject%2CfromName&maxSize=20&offset=1000&orderBy=dateSent&order=desc"
    POST_EMAIL_INSERT_IMAGE = "/Attachment"