from email.message import EmailMessage
import ssl
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os

def notify(filename):
	email_sender = "Enter email of sender"
	password = "Don't enter your gmail password here, read the README file for better understanding"
	email_receiver = "Enter email of receiver"
	subject="야옹이지킴이"
	body="고양이가 {}에 인덕션에 다가왔어요!!".format(str(datetime.now()))

	ema = MIMEMultipart()
	ema["From"] = email_sender
	ema["To"] = email_receiver
	ema["subject"] = subject
	text = MIMEText("고양이가 인덕션에 다가왔어요!!")
	ema.attach(text)
	with open("static/warnings/" + filename, 'rb') as f:
		img_data = f.read()

	image = MIMEImage(img_data, name=os.path.basename(filename))
	ema.attach(image)
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
		smtp.login(email_sender,password)
		smtp.sendmail(email_sender,email_receiver,ema.as_string())