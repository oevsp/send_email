import smtplib
import csv
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

## Credentials for your email you want to use to send emails out to
my_email = 'myemail@mymail.com'
password = "password"

subject = "My Subject Line"

img_data = open("logo.png", 'rb').read()

with open('emails.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    for line in reader:
        text = "Dear " + line[0] + ''' \n\nLorem Ipsum is simply dummy text of the printing and typese
                                   \nindustry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley
                                   \n\nBest,
                                   \n\nBen Dover - Client Relations
                                   \n\nE: myemail@mymail.com\nwww.example.com'''
        send_email = line[1]
        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = send_email
        msg['Subject'] = subject
        msg.attach(MIMEText(text))
        image = MIMEImage(img_data, name=os.path.basename("logo.png"))
        msg.attach(image)

## Your connection settings to your SMTP server here
## Can try using port 567 for TLS or removing SSL from SMTP and adding next line start.tls()
        connection = smtplib.SMTP_SSL("smtp.logaveconsulting.com", 465, timeout=120)
        connection.login(user="Mchoncer", password=password)
        connection.sendmail(my_email,send_email,msg.as_string())
		
## Some SMTP servers limit how many emails you can mail out
        time.sleep(30.0)

        connection.close()
