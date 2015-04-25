import requests
from BeautifulSoup import BeautifulSoup

# Url building
site = "https://ordomedic.be/"
town = "5000"
language = "fr"

query = language+"/rechercher-un-medecin/?search_place="+town+"&page=1"
url = site+query

# Url connecting
response = requests.get(url)

# HTML parsing
defaultSoup = BeautifulSoup(response.text)

for med in defaultSoup.findAll(attrs = {"class": "result"}):
  name = med.findAll(attrs = {"class": "name"})
  address = med.findAll(attrs = {"class": "address"})
  print name[0].string
  print ""
  #print med.get("name")
