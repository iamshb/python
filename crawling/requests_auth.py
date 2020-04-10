import requests

r = requests.get('https://github.com/', auth=('user', 'pass'))
print(r.status_code)
print(r.headers)
