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



res = requests.get("http://api.paychecks.nl/werknemerx")
res = res.text
res = json.loads(res)
res = eval(res)

employee_id = res[1].get("employee_id")
first_name = res[1].get("first_name")
last_name = res[1].get("last_name")
email = res[1].get("email")
gender = res[1].get("gender")
city = res[1].get("city")
job_title = res[1].get("job_title")
shirt_size = res[1].get("shirt_size")