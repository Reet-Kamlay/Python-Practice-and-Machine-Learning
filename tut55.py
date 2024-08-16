import requests
from bs4 import BeautifulSoup
url=""
r=requests.get(url)
print(r.text)
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())