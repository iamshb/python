from bs4 import BeautifulSoup

html = """
<html>
<body>
    <div id ='main'>
        <h1>강의목록</h1>
        <ul class='lecs'>
            <li>Java</li>
            <li>Python</li>
            <li>Tensorflow</li>
            <li>iOS Dev</li>
        </ul>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select_one('div#main > h1')
# print('h1:', h1)

# lecture_list = soup.select('div#main > ul.lecs > li')
lecture_list = soup.select('#main > .lecs > li')
for lecture in lecture_list:
    print(lecture.string)
