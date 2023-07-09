import requests


def request(url, method, payload):
    if method == 'POST':
        res = requests.post(url, json=payload)
    elif method == 'GET':
        res = requests.get(url)
    else:
        return None
    return res.json()


url = 'http://127.0.0.1:8000/api/v1/token/'
method = 'POST'
payload = {'username': 'aza', 'password': '123'}

result = request(url, method, payload)
print(result)
