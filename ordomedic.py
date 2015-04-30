# -*- coding: utf8 -*-

import requests
from BeautifulSoup import BeautifulSoup
import json

def generateSpecialities():
# Function to retrieve all the specialisation
  url = "https://ordomedic.be/fr/rechercher-un-medecin/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text)
  specList = soup.findAll(attrs={"name":"search_specialism"})
  sList = []
  for spec in specList[0].findAll("option")[1:]:
    sList.append({"value":spec.get("value"),"name":spec.string})

  return sList
  
def RetrievePeople(page,speciality,people):
# Function to retrieve people of a certain page for a certain speciality
  query = language+"/rechercher-un-medecin/?"
  query = query + "search_specialism=" + spec["value"]
  query = query + "search_place=" + town
  query + query + "&page=" + str(numPage)
  url = site+query

  # Url connecting
  response = requests.get(url)

  # Stop if bad connection
  if response.status_code != 200:
    print response.status_code
    isEnd = "Y"
    continue

  # Or no more people to gather
  if numberOfPeople == people:
    isEnd = "Y"
    print "too many people !"
    break

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
    med["Address"] = str(address[0].findAll("dd",limit=2)[0].string) + str(address[0].findAll("dd",limit=2)[1].string)
    # Extract of the phone number
    phone = address[0].findAll("dd")[-1].string
    if phone[1:3] == "Tel":
      med["Phone"] = phone.split(" ")[1]
    else:
      med["Phone"] = "None"
    # Add the specialisation
    med["specialisation"] = spec["name"]

    # Not add duplicates
    if med not in people:
      people.append(med)
  
  return people

# Url building
site = "https://ordomedic.be/"
town = "5000"
language = "fr"
people = []
numberOfPeople = len(people)
isEnd = "N"

for spec in generateSpecialities():
  numPage = 1
  while isEnd == "N":

    people = retrievePeople(numPage,spec,people)

    # Add one to index
    numPage = numPage+1
    if numPage >= 10:
      isEnd = "Y"

# Save in a JSON file
with open('medecins.json', 'w') as outfile:
    json.dump(people, outfile)
