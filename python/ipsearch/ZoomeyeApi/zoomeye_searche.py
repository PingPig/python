import requests
import json
import os

data = {
    'username': 'xxxxx@.com',
    'password': 'xxxxxx'
}
jsonData = json.dumps(data,indent=4)
r = requests.post('https://api.zoomeye.org/user/login',data=jsonData)
result = json.loads(r.text)
accessToken = result['access_token']
header = {'Authorization': 'JWT ' + accessToken,}
target = "citrix"
page = 1
g = requests.get(url='https://api.zoomeye.org/host/search?query=app:'+target+' country:Guinea &page='+ str(page),headers=header)
rdecode = json.loads(g.text)
for  i in rdecode['matches']:
    print(i['ip']+":"+str(i['portinfo']['port']))
