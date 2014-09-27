import json
import subprocess
import requests


with open('userDict.json') as userDict:
    userBadgeData = json.load(userDict)
    #print(userBadgeData)

for key, value in userBadgeData.items():
    #value = json.dumps(value)
    print(value)
    headers = {'content-type' : 'application/json'}
    badge_url = 'https://sandbox.youracclaim.com/api/v1/organizations/41dd84f5-e826-4e17-a819-14b6af8bdb1f/badge_templates'
    r = requests.post(badge_url, data=json.dumps(value) , auth=('59kyows7O22yDDvz_g40', ''), headers=headers)

    print(r.headers['status'])
