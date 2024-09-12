import csv
import json
import os
from os.path import abspath, dirname

def csv_to_json_with_column_number_rename(csv_file_path, json_file_path):
    data = []
    isEnergyUseIntensity = "eui" in csv_file_path

    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)

        for row in csv_reader:
            renamed_row = {}
            for index, value in enumerate(row):
                if index == 0:
                    renamed_row["month"] = value
                else:
                    if isEnergyUseIntensity:
                        header = headers[index][:-7]
                    else:
                        header = headers[index][:-5]
                    header = header[0].lower() + header[1:]

                    if "equip" in header:
                        header = "equipment"    
                    elif "cool" in header:
                        header = "cooling"
                    elif "hReject" in header:
                        header = "heatReject"
                    elif "light" in header:
                        header = "lighting"
                    elif "heat" in header:
                        header = "heating"

                    renamed_row[header] = round(float(value), 2)

            data.append(renamed_row)

    with open(json_file_path, mode='w') as json_file:
        json.dump(data, json_file, indent=2)

    print(f"CSV file '{csv_file_path}' has been converted to JSON file '{json_file_path}' with renamed columns.")


os.chdir(dirname(abspath(__file__)))
FILE_NAME = "pioneer-house-eu"
csv_file_path = f"{FILE_NAME}.csv"
json_file_path = f"{FILE_NAME}.json"
csv_to_json_with_column_number_rename(csv_file_path, json_file_path)
