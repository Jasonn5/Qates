from enum import Enum

class EndpointCorreoImportant(Enum):

    GET_MAIL_IMPORTANT = "/Email"
    GET_MAIL_OFFSET_1000 = "/Email?offset=1000"
    GET_MAIL_MAXSIZE_1 = "/Email?maxSize=1"
    GET_MAIL_INVALID_ORDER = "/Email?order=invalid"
    POST_EMAIL_INSERT_IMAGE = "/Attachment"
