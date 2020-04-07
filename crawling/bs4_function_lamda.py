from bs4 import BeautifulSoup

html = open('./scrawling/cars.html', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')

def car_function(sel):
    print('car_func:', soup.select_one(sel).string)

car_lambda = lambda sel : print('car_lambda:', soup.select_one(sel).string)

car_function('ul#cars > li#so')
car_function('#cars > #so')
car_function('#cars #so')
car_function('#so')
car_function('li[id="so"]')

car_lambda('ul#cars > li#so')
car_lambda('#cars > #so')
car_lambda('#cars #so')
car_lambda('#so')
car_lambda('li[id="so"]')
