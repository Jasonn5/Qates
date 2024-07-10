from enum import Enum

CONTACT_ROUTE = 'Contact'


class ContactEndpoint(Enum):
    MAIN_ROUTE = f'/{CONTACT_ROUTE}'
