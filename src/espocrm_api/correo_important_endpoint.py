from enum import Enum

class EndpointCorreoImportant(Enum):
    GET_CORREO_IMPORTANT = "/Email?select=dateSent%2CparentId%2CparentType%2CparentName%2Csubject%2CpersonStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where%5B0%5D%5Btype%5D=inFolder&where%5B0%5D%5Battribute%5D=folderId&where%5B0%5D%5Bvalue%5D=important"
