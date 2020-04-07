from bs4 import BeautifulSoup

html = """
<html>
<body>
    <ul>
        <li><a href='http://www.naver.com'>naver</a></li>
        <li><a href='http://www.daum.com'>daum</a></li>
        <li><a href='http://www.google.com'>google</a></li>
        <li><a href='http://www.tistory.com'>tistory</a></li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

a_list = soup.find_all('a')
# for a in a_list:
#     print('a tag:', a)
#     print('a string:', a.string)
#     print('attr href:', a.attrs['href'])

google = soup.find('a', string='google')
print('google: ', google)

naver_google = soup.find_all('a', string=['naver', 'google'])
print('naver_google:', naver_google)

limit = soup.find_all('a', limit=2)
print('limit:', limit)
