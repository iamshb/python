from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import os

# # naver headers
# opener = req.build_opener()
# opener.addheaders = [('User-agent','Mozilla/5.0')]
# req.install_opener(opener)

base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
query = '신혜선'
quote = rep.quote_plus(query)
url = base_url + quote

savePath = os.path.join('./crawling/image', query)

try:
    if not os.path.isdir(savePath):
        os.makedirs(savePath);
except OSError as e:
    if e.errno != errono.EEXIST:
        print('fail to make directory!')
        raise

res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

image_list = soup.select('div.img_area > a.thumb._thumb > img')

for i, img in enumerate(image_list, 1):
    file_path = os.path.join(savePath, str(i) + '.jpg')
    req.urlretrieve(img['data-source'], file_path)
