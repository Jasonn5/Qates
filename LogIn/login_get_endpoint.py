import requests
import json

url = "https://espo.spartan-soft.com/api/v1/App/user"

payload = {}
headers = {
  'authorization': 'Basic YWRtaW46YWRtaW4=',
  'content-type': 'application/json',
  'espo-authorization': 'YWRtaW46YWRtaW4=',
  'espo-authorization-by-token': 'false',
  'espo-authorization-create-token-secret': 'true',
  'priority': 'u=1, i',
  'referer': 'https://espo.spartan-soft.com/',
  'Cookie': 'auth-token-secret=50fe377b22952fca5ac1901ec2af8e90'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
