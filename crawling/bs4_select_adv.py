from bs4 import BeautifulSoup

html = open('./scrawling/foods.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')

print('1:', soup.select('li:nth-of-type(4)')[1].string)
print('2:', soup.select_one('ul#ac-list > li.alcohol.high').string)
print('3:', soup.select('#ac-list > li[data-lo="cn"]')[0].string)
print('4:', soup.select('#ac-list > .alcohol.high')[0].string)
print('5:', soup.select('#ac-list > .alcohol')[3].string)

param = {'data-lo':'cn', 'class':'alcohol'}
print('A:', soup.find('li', param).string)
print('B:', soup.find_all('li', param)[0].string)
print('C:', soup.find(id='ac-list').find('li', param).string)

for ac in soup.find_all('li'):
    # print(type(ac), ac)
    if ac['data-lo'] == 'us':
        print(ac.string)
