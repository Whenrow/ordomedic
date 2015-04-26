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
language = "fr"
numPage = 1
people = []
isEnd = "N"

while isEnd == "N":

  query = language+"/rechercher-un-medecin/?search_place="+town+"&page="+str(numPage)
  url = site+query

  # Url connecting
  response = requests.get(url)
  print response.status_code

  # HTML parsing
  defaultSoup = BeautifulSoup(response.text)


  # Person list
  for info in defaultSoup.findAll(attrs = {"class": "result"}):
    med = {}
    # Name's Extract
    name = info.findAll(attrs = {"class": "name"})
    # Address' extract
    address = info.findAll(attrs = {"class": "address"})
    # Text only of the info
    med["name"] = name[0].string
    med["Address"] = address[0].findAll("dd",limit=2)[0].string + address[0].findAll("dd",limit=2)[1].string
    # Extract of the phone number
    phone = address[0].findAll("dd")[-1].string
    if phone[1:3] == "Tel":
      med["Phone"] = phone.split(" ")[1]
    else
      med["Phone"] = "None"
    people.append(med)

  # Add one to index
  numPage = numPage+1
  if numPage >= 20:
    isEnd = "Y"

# Save in a JSON file
with open('medecins.json', 'w') as outfile:
    json.dump(people, outfile)
