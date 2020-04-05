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
print(soup.prettify())