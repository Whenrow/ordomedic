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

# Person list
for med in defaultSoup.findAll(attrs = {"class": "result"}):
  # Name's Extract
  name = med.findAll(attrs = {"class": "name"})
  # Address' extract
  address = med.findAll(attrs = {"class": "address"})
  # Text only of the info
  print name[0].string
  print address[0].findAll("dd",limit=2)[0].string
  print address[0].findAll("dd",limit=2)[1].string
  print ""
