import smtplib
import ssl
import os
import dotenv

dotenv.load_dotenv()


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "kusumo1920@gmail.com"
    password = os.getenv("EMAIL_APP_PASSWORD")

    receiver = "kusumo1920@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
