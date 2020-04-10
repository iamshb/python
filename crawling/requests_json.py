import requests
import json

s = requests.Session()
r = s.get('https://jsonplaceholder.typicode.com/albums')
print(r.json())
print(r.content)
print(r.encoding)
print(r.raw)
print(r.status_code)
print(r.ok)

s.close()


with requests.Session() as s:
    r = s.get('http://httpbin.org/stream/20')

    for line in r.iter_lines(decode_unicode='utf-8'):
        # print(type(line)) -> binary
        json_str = json.loads(line)
        # print(type(json_str)) -> dict
        for e in json_str.keys():
            print('#', e, ':', json_str[e])
