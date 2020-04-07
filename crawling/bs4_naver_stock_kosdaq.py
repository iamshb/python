from bs4 import BeautifulSoup
import urllib.request as req

url = 'https://finance.naver.com/sise/sise_rise.nhn?sosok=1'
res = req.urlopen(url).read().decode('euc-kr')

soup = BeautifulSoup(res, 'html.parser')
# print(soup)

top10 = soup.select('div.box_type_l > table.type_2 > tr')
i = 1

for e in top10:
    if e.select_one('td > a.tltle') is not None:
        href = e.select_one('td > a').attrs['href']
        code = href.split('=')[1]
        title = e.select_one('td > a.tltle').string
        price = e.select('td')[2].string
        updown = e.select('td')[4].select_one('span').string.strip()
        trade_num = e.select('td')[5].string.replace(',', '')

        print(i, ':', title, price, href, code, updown, trade_num)
        i += 1
