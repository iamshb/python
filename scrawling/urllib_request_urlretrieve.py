import urllib.request as req

image_url = 'http://cafefiles.naver.net/20120603_100/bawnim_1338724297760Ronfy_JPEG/na1338724239.jpg'
download_path = './urlretrieve_image.jpg'

req.urlretrieve(image_url, download_path)