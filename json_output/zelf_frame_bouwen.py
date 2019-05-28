import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests
import json
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime



res = requests.get("http://api.paychecks.nl/booksjsontest")
res = res.text
res = json.loads(res)
res = eval(res)

x = 1
ja_mail = []
nee_mail = []

while x < len(res):
    # try:
    isbn = res[x].get("isbn")
    title = res[x].get("title")
    author = res[x].get("author")
    year = res[x].get("year")
    # print(isbn, title, author, year)

    now = datetime.now()
    datumtijd = now.replace(microsecond=0)

    alleen_datum = datetime.today().strftime('%Y-%m-%d')
    logboeknaam = (alleen_datum + " Pay-Check Logboek.csv")

    x = x +1

    temp_dict = {
        "datumtijd": datumtijd,
        "isbn": isbn,
        "title": title,
        "author": author,
        "year": year
    }




    ja_mail.append(temp_dict)


# except:
#     nee_mail.append(temp_dict)
#     print("Er is iets mis rond:", temp_dict)

    import csv
    row = [datumtijd, isbn, title, author, year]



    with open(logboeknaam, 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)


gelukt = ("Gelukt:", len(ja_mail), ja_mail)
niet_gelukt = ("Niet gelukt:", len(nee_mail), nee_mail)

print(gelukt)
print(niet_gelukt)


