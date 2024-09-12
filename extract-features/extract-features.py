import json 
import os
from os.path import abspath, dirname
os.chdir(dirname(abspath(__file__)))

OVERPASS_FILE = "import.json"
OUTPUT_FILE = "output.json"

with open(OVERPASS_FILE,"r") as file:
  jsonData = json.load(file)

elements = jsonData['features']

output_dict = [x["properties"] for x in elements if 'name' in x["properties"]]

format_dict = []
for item in output_dict:
  new_item = dict(item)
  if "@id" in new_item:
    curr_id = new_item.pop("@id").split("/")[-1]
    new_item["elementId"] = curr_id  # Rename key and remove old one
  if "addr:postcode" in new_item:
    new_item["postal"] = new_item.pop("addr:postcode")
  format_dict.append(new_item)

clean_dict = []
for item in format_dict:
  new_item = {key: item[key] for key in ("elementId", "name", "postal") if key in item}
  clean_dict.append(new_item)

sort_dict = sorted(format_dict, key=lambda item: item["name"])

with open(OUTPUT_FILE, "w") as outputFile:
  json.dump(sort_dict, outputFile)
