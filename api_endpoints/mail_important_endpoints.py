from enum import Enum

class EndpointCorreoImportant(Enum):
    GET_CORREO_IMPORTANT = "/Email"
    GET_CORREO_OFFSET_1000 = "/Email?offset=1000"
    GET_CORREO_MAXSIZE_1 = "/Email?maxSize=1"
    GET_CORREO_INVALID_ORDER = "/Email?order=invalid"