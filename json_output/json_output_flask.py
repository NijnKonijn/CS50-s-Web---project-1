from flask import jsonify
from flask import Flask
import csv
import json

app = Flask(__name__)


csvfilepath = ('books.csv')
jsonfilepath = ("books_index.json")

data = {}
with open(csvfilepath) as csvfile:
    csvreader = csv.DictReader(csvfile)
    for csvrow in csvreader:
        isbn = csvrow["isbn"]
        data[isbn] = csvrow

with open (jsonfilepath, "w") as jsonfile:
    jsonfile.write(json.dumps(data, indent=4))



@app.route('/booksjason')
def booksjason():
    csvfilepath = ('books.csv')
    jsonfilepath = ("books_index.json")

    data = {}
    with open(csvfilepath) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for csvrow in csvreader:
            isbn = csvrow["isbn"]
            data[isbn] = csvrow

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True)
