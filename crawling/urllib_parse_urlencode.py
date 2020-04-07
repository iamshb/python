from urllib.parse import urlencode
import urllib.request as req

api = 'https://api.ipify.org'
params = {'ctxCd': '1001'}
url = api + "?" + urlencode(params)

response = req.urlopen(url).read().decode('utf-8')
print('> your ip is', response)