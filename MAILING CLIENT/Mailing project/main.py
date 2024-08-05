import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase



server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.ehlo()

with open('pass.txt','r') as f:
    password = f.read()

server.login('',password)
msg = MIMEMultipart()
msg['From'] = 'username'
msg['To'] = 'username'
msg['Subject'] = 'TEST'

with open('text.txt','r') as f:
    text = f.read()
    msg.attach(MIMEText(text,'plain'))



text = msg.as_string()
server.sendmail(msg['username from'],msg['username to'],text)

try:
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {str(e)}")
finally:

    server.quit()