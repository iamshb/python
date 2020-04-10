import requests

with requests.Session() as s:
    r = s.get('http://httpbin.org/ip')
    print(r.text)
