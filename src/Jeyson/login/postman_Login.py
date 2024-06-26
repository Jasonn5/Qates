import requests
import json

url = "https://espo.spartan-soft.com/api/v1/App/user"

payload = {}
headers = {
  'authorization': 'Basic amV5c29uOlRlc3RpbmcuMTIzIQ==',
  'content-type': 'application/json',
  'Cookie': 'auth-token-secret=068858cae2765fdb68d845634fbf3746'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
