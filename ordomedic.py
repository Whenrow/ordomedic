# -*- coding: utf8 -*-

import requests
from BeautifulSoup import BeautifulSoup
import json


def generateSpecialities():
# Function to retrieve all the specialisation
  url = "https://ordomedic.be/fr/rechercher-un-medecin/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text)
  specList = soup.findAll("search_specialism")
  sList = {}
  for spec in specList:
    sList.append(spec.a.string)
  
  return sList
  
# Url building
site = "https://ordomedic.be/"
town = "5000"
numPage = "1"
language = "fr"

query = language+"/rechercher-un-medecin/?search_place="+town+"&page="+numPage
url = site+query

# Url connecting
response = requests.get(url)

# HTML parsing
defaultSoup = BeautifulSoup(response.text)


# Person list
people = []
for info in defaultSoup.findAll(attrs = {"class": "result"}):
  med = {}
  # Name's Extract
  name = info.findAll(attrs = {"class": "name"})
  # Address' extract
  address = info.findAll(attrs = {"class": "address"})
  # Text only of the info
  med["name"] = name[0].string
  med["Address"] = address[0].findAll("dd",limit=2)[0].string + address[0].findAll("dd",limit=2)[1].string
  med["Phone"] = address[0].findAll("dd")[-1].string.split(" ")[1]
  people.append(med)

# Save in a JSON file
with open('medecins.json', 'w') as outfile:
    json.dump(people, outfile)
