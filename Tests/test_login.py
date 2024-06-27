import base64
import json
import requests

#Testing the Login of EspoCRM
#Basic authentication is a very simple authentication scheme that is built into the HTTP protocol.
#The client sends HTTP requests with the Authorization header that contains
#the Basic word followed by a space and a base64-encoded username:password string

#### Valid credentials sent in the header
def test_login_valid_credentials():
    url = "https://espo.spartan-soft.com/api/v1/App/user"
    payload = ""
    username = "admin" #tambien permite con "Admin"
    password = "admin"
    joinedString = username + ":" +password
    bytes_string = joinedString.encode('utf-8')

    # Codificar la cadena en bytes a Base64
    base64_encoded = base64.b64encode(bytes_string)

    # Convertir el resultado de Base64 de bytes a string
    base64_encoded_string = base64_encoded.decode('utf-8')
    print("This is the base64 authorization: " + base64_encoded_string)

    payload = {}
    headers = {
        'authorization': 'Basic '+base64_encoded_string,
        'content-type': 'application/json',
        'referer': 'https://espo.spartan-soft.com/'
    }
    response = requests.get(url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["user"]["id"] is not None
    assert response_data["user"]["ipAddress"] is not None
    assert response_data["user"]["name"] == "Admin"


#Invalid credential sent in the header
def test_login_invalid_credentials():
    url = "https://espo.spartan-soft.com/api/v1/App/user"
    payload = ""
    username = "admin"
    password = "Admin123"
    joinedString = username + ":" +password
    bytes_string = joinedString.encode('utf-8')

    # Codificar la cadena en bytes a Base64
    base64_encoded = base64.b64encode(bytes_string)

    # Convertir el resultado de Base64 de bytes a string
    base64_encoded_string = base64_encoded.decode('utf-8')
    print("This is the base64 authorization: " + base64_encoded_string)

    payload = {}
    headers = {
        'authorization': 'Basic '+base64_encoded_string,
        'content-type': 'application/json',
        'referer': 'https://espo.spartan-soft.com/'
    }
    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 401

#Access denied by to many attempts
def test_login_access_denied():
    url = "https://espo.spartan-soft.com/api/v1/App/user"
    payload = ""
    username = "admin"
    password = "Admin123"
    joinedString = username + ":" +password
    bytes_string = joinedString.encode('utf-8')
    base64_encoded = base64.b64encode(bytes_string)
    base64_encoded_string = base64_encoded.decode('utf-8')

    payload = {}
    headers = {
        'authorization': 'Basic '+base64_encoded_string,
        'content-type': 'application/json',
        'referer': 'https://espo.spartan-soft.com/'
    }

    response = requests.get(url, headers=headers, data=payload)
    intentos = 1
    while response.status_code == 401:
        response = requests.get(url, headers=headers, data=payload)
        intentos+=1

    print("Number of tries to get access denied is: "+ str(intentos))
    assert response.status_code == 403



