from enum import Enum

class EndpointEmail(Enum):
    GET_EMAIL_WITHOUT_PARAMS = "/Email?select=2CparentType&maxSize=20&offset=0&order=desc&where%5B0%5D%5Btype%5D=inFolder&where%5B0%5D%5Battribute%5D=folderId&where%5B0%5D%5Bvalue%5D=drafts"
    GET_EMAIL_WITH_PARAMS = "/Email?select=dateSent,parentId,parentType,parentName,subject,personStringData&maxSize=20&offset=0&orderBy=dateSent&order=desc&where[0][type]=inFolder&where[0][attribute]=folderId&where[0][value]=drafts"
    POST_EMAIL_DRAFT = "/Email"
    DELETE_EMAIL_DRAFT = "/api/v1/Email/{id}"