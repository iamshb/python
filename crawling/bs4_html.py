from bs4 import BeautifulSoup

html = """
<html>
<body>
<h1>python BeautifulSoup study</h1>
<p>tag selector</p>
<p>css selector</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

print('h1 >>', h1.string)
print('p1 >>', p1.string)
print('p2 >>', p2.string)
