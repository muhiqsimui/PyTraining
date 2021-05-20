import json
import requests 
url_1="https://data.covid19.go.id/public/api/update.json"
url_2="https://coronavirus-19-api.herokuapp.com/all"
url_3="https://covid19.mathdro.id/api"
url = url_2
x=True
def con(url):
  timeout = 1
  try:
	  request = requests.get(url, timeout=timeout)
	  print("Connected to the Internet")
  except (requests.ConnectionError, requests.Timeout) as exception:
	  print("No internet connection.")
    # x=False

print("API Kemkes 1 : ")
con(url_1)
print("API Inter : ")
con(url_2)
print("API MathDroid : ")
con(url_3)
