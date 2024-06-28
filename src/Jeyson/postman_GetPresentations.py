import requests

url = "https://espo.spartan-soft.com/api/v1/Meeting?select=assignedUserId%2CassignedUserName%2CdateStart%2CdateStartDate%2Cstatus%2CparentId%2CparentType%2CparentName%2Cname&maxSize=20&offset=0&orderBy=dateStart&order=desc"

payload = {}
headers = {
  'cookie': '_ga=GA1.1.476256.1715457009; _ga_N9Z1S3V9NN=GS1.1.1715462238.2.0.1715462238.0.0.0; auth-token-secret=e43cf03f622ecbc3b1178afc3be88578; auth-token=5f1d0e4801415b41a9b9ded76bcee339; auth-token-secret=068858cae2765fdb68d845634fbf3746'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)