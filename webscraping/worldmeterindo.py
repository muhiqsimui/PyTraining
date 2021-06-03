from bs4 import BeautifulSoup
import requests as r

#ambil
web=r.get("https://www.worldometers.info/coronavirus/country/indonesia/")
#seluruh code halamalan
print(web.content)

bs_fix=BeautifulSoup(web.content,'html.parser')

#find untuk menemukan id anu dan itu
data_cov=bs_fix.find(id="maincounter-wrap")
print(data_cov)
print("")
# text untuk menampilkan text nya saja
cov_text=data_cov.text
print(cov_text)

#cara 2
#find all untuk cari semua dengan class bla bla
data_cov2 = bs_fix.find_all("div", {"class": "maincounter-number"})
print(data_cov2)

print("")
#ambil text saja
for x in data_cov2:
  print(x.text)
