import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.bbc.com")
c = r.content
html = BeautifulSoup(c, 'html.parser')
print(html, type(html))

print(html.find_all('h1'))