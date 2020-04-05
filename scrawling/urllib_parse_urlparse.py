import urllib.request as req
from urllib.parse import urlparse

url = 'http://www.google.com'

parsed = req.urlopen(url)

print('geturl():', parsed.geturl())
print('status:', parsed.status)
print('getheaders():\n', parsed.getheaders())
print('info():\n', parsed.info())
print('getcode():', parsed.getcode())
print('read():\n', parsed.read(100).decode('utf-8'))

print('urlparse:\n', urlparse(url + '?test=test'))