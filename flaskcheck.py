import requests

URL = 'http://127.0.0.1:5002/api/uppercase'

for t in ['hello reest', ' ipc demo', 'bye']:
    payload = {'text':t}
    resp = requests.post(URL, json=payload)
    print('sent:', t)
    print('Response:', resp.json())