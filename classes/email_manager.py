from email.message import EmailMessage
from db_manager import db_manager as db
from numpy import random
import ssl
import smtplib

class Email:

    def __init__(self):
        self.email = db().get_email()
        self.password = db().get_email_password()

    def send_email(self, to_email, subject, body):
        message = EmailMessage()
        message['From'] = self.email
        message['To'] = to_email
        message['Subject'] = subject
        message.set_content(body)

        safe = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
            smtp.login(self.email, self.password)
            smtp.sendmail(
                self.email,
                to_email,
                message.as_string()
            )

    def generate_one_time_password(self):
        one_time_password = ''
        for i in range(6):
            one_time_password += f'{random.randint(9)}'
        return one_time_password

to_email = 'matheus.pgua94@gmail.com'
subject = 'Código de acesso único'

body = f'Seu código de acesso único é: {Email().generate_one_time_password()}'

Email().send_email(to_email, subject, body)