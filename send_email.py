import smtplib
import ssl
import os



def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "reneesmith4949@gmail.com"
    password = os.getenv("PASSWORD")
    receiver_email = "reneesmith4949@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)

