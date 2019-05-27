import csv
reader = csv.DictReader(open('books.csv'))
booksdict = []
for row in reader:
    booksdict.append(row)
    x = booksdict.append(row)
    print(x)
