import urllib.request as req

image_url = 'http://cafefiles.naver.net/20120603_100/bawnim_1338724297760Ronfy_JPEG/na1338724239.jpg'
download_path = './urlopen_image.jpg'

source = req.urlopen(image_url).read()
with open(download_path, 'wb') as file:
    file.write(source)
