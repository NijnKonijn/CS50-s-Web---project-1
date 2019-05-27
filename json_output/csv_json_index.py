import csv
import json

csvfilepath = ('books.csv')
jsonfilepath = ("books_index.json")

data = {}
with open(csvfilepath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    for csvrow in csvreader:
        isbn = csvrow["isbn"]
        data[isbn] = csvrow
    print(data)

with open (jsonfilepath, "w") as jsonfile:
    jsonfile.write(json.dumps(data, indent=4))