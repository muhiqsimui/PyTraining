

import requests as r
from bs4 import BeautifulSoup
# web=r.get("https://nanime.biz")

# soup=BeautifulSoup(web.content,'html.parser')

# posta=soup.find_all('h3',{'class':'post-title'})

# for poster in posta:
#   print(poster.text)

def gsc(url,tag):
  url2="https://www.google.com/search?q="+url+"&safe=strict&source=lnms&tbm=nws"
  web=r.get(url2)
  soup=BeautifulSoup(web.content,'html.parser')
  elemen=soup.find_all(tag)

  for datascr in elemen:   
    print(datascr.text)

gsc("kasus covid-19 jakarta",('h3'))

def scraping(url,tag):
  web=r.get(url)
  soup=BeautifulSoup(web.content,'html.parser')
  cari=soup.find_all(tag)
  for search in cari:
    print(search.text)
scraping("https://www.okezone.com",('title'))

link='https://covid19.go.id/tanya-jawab'

scraping(link,"title")
scraping(link,"h1")
scraping(link,"p")

