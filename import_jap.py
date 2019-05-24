import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

"""
use this line in terminal:
export DATABASE_URL=""postgres://wwzshdaglnjdmv:8f6f6c2d1b7bb9f872e2d03f0b0cc58a7bdf88b06f6eb78d72a164246669bd8b@ec2-46-137-113-157.eu-west-1.compute.amazonaws.com:5432/d7333gmnt3hpm1""
"""

# (Syntax voor TABLE): CREATE [TEMPORARY] TABLE table (field1 type [(size)] [NOT NULL] [WITH COMPRESSION | WITH COMP] [index1] [, field2 type [(size)] [NOT NULL] [index2]
# 1. table to keep track of users, 2. table to keep track of books, and 3. table to keep track of reviews.

def importeer():
    book_count = 0

    # Create tables.
    db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR NOT NULL)")
    db.execute("CREATE TABLE reviews (isbn VARCHAR NOT NULL,review VARCHAR NOT NULL, rating INTEGER NOT NULL,username VARCHAR NOT NULL)")
    db.execute("CREATE TABLE books (isbn VARCHAR PRIMARY KEY,title VARCHAR NOT NULL,author VARCHAR NOT NULL,year VARCHAR NOT NULL)")

    f=open("books.csv")
    reader =csv.reader(f)


    no_first_line = True
    for isbn,title,author,year in reader:

        print("v3")

        if no_first_line is True:
            no_first_line = False
            print("No first line")

        else:
            db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:a,:b,:c,:d)", {"a": isbn, "b": title, "c": author, "d": year})
            print(book_count)
            book_count = book_count + 1

    db.commit()


importeer()