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


    werkgeversnaam = "Voorbeeld werkgever B.V. "
    email_onderwerp = (werkgeversnaam + alleen_datum + " Pay-Check Logboek")

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






### Email ###

text_email = """
Beste Collega,

Rapport gegenereerd uit verwerking door api, zie bijlage.

Met vriendelijke groet,

Server 0.2
"""


subject = email_onderwerp
body = text_email
sender_email = "jasperakkerman@gmail.com"
receiver_email = "loonadministratie@pay-check.nl"
password = "pbdyjaiflkgkhpkw"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = logboeknaam  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)