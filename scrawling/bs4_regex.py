from bs4 import BeautifulSoup
import re #regex

# ref.
# http://pythonstudy.xyz/python/article/401-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-Regex

html = """
<html>
<body>
    <ul>
        <li id='naver'><a href='https://www.naver.com'>naver</a></li>
        <li><a href='http://www.daum.com'>daum</a></li>
        <li><a href='https://www.daum.com'>daum</a></li>
        <li><a href='https://www.google.com'>google</a></li>
        <li><a href='http://www.tistory.com'>tistory</a></li>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
print('naver:', soup.find(id='naver').string)
print('google:', soup.find(href='https://www.google.com').attrs['href'])

# li_list = soup.find_all(href=re.compile(r'da'))
li_list = soup.find_all(href=re.compile(r'^https'))
for li in li_list:
    print(li.string, ":", li.attrs['href'])
