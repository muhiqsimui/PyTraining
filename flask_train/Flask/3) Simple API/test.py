import requests as r

BASE = 'http://127.0.0.1:5000/'

url = r.get(BASE+'api')
gdata = url.json()
print(gdata['data']['name'])
