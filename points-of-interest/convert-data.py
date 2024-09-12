import csv
import json
import os
from os.path import abspath, dirname

os.chdir(dirname(abspath(__file__)))
data = []
with open("points-data.csv", mode='r') as csv_file:
  csv_reader = csv.reader(csv_file)
  headers = next(csv_reader)
  for row in csv_reader:
    renamed_row = {}
    id = 0
    for index, value in enumerate(row):
      if index == 0:
        id = value.split("/")[-1].split(".")[0]
        renamed_row["id"] = id
      elif index == 1:
        l, r = value.split("/")
        renamed_row["latitude"] = int(l) / int(r)
      elif index == 2:
        l, r = value.split("/")
        renamed_row["longitude"] = int(l) / int(r) 

    renamed_row["images"] = [
      { "src": f"/src/assets/points-of-interest/{id}.jpg" }, 
      { "src": f"/src/assets/points-of-interest/thermal-{id}.jpg" }, 
      ]
    data.append(renamed_row)

with open("output.json", mode='w') as json_file:
  json.dump(data, json_file, indent=2)

