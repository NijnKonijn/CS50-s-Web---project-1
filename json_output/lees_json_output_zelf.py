import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
import json


res = requests.get("http://api.paychecks.nl/booksjsontest")
res
x = {
    "title": res.title,
    "author": res.author,
    "year": res.year,
    "isbn": res.isbn
}

print(x)

print(res.text)