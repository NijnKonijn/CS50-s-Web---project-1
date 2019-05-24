import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
import json

# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

"""
use this line in terminal:
export DATABASE_URL=""postgres://wwzshdaglnjdmv:8f6f6c2d1b7bb9f872e2d03f0b0cc58a7bdf88b06f6eb78d72a164246669bd8b@ec2-46-137-113-157.eu-west-1.compute.amazonaws.com:5432/d7333gmnt3hpm1""
"""

def api(isbn):
    data = db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": isbn}).fetchone()
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "iLA6lN19IlY5kRBVTjNxnw", "isbns": isbn})
    average_rating = res.json()['books'][0]['average_rating']
    work_ratings_count = res.json()['books'][0]['work_ratings_count']

    x = {
        "title": data.title,
        "author": data.author,
        "year": data.year,
        "isbn": isbn,
        "review_count": work_ratings_count,
        "average_score": average_rating
    }

#    print(x)

    api = json.dumps(x)
    return api


# api("1857231082")
# from get_api_goodreads import ap
# api("1857231082")