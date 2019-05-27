import csv
import json

# Open the CSV
f = open('books.csv', 'r')

# Change each fieldname to the appropriate field name. I know, so difficult.
reader = csv.DictReader(f, fieldnames=("isbn", "title", "author", "year"))

# Parse the CSV into JSON
out = json.dumps([row for row in reader], indent=4)
print("JSON parsed!")

# Save the JSON
f = open('parsed.json', 'w')
f.write(out)
print("JSON saved!")