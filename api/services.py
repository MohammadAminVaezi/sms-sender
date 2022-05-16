import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
from kavenegar import KavenegarAPI
import os
load_dotenv()


class TextSender:
    def __init__(self):
        print("initialized text sender")
        self.from_email = os.getenv('YOUR-EMAIL')

    def send(self, email, phone_number, text):
        api = KavenegarAPI(os.getenv('API_KEY'))
        params = {
            "receptor": self.phone_number,
            "message": f'{self.text}.\n Dandelion'
        }
        api.sms_send(params)

        msg = EmailMessage()
        msg['Subject'] = 'Dandelion'
        msg['From'] = self.from_email
        msg['To'] = email
        msg.set_content(self.text)

        context = ssl.create_default_context()

        smtp = smtplib.SMTP("smtp.gmail.com", port=587, timeout=2)
        smtp.starttls(context=context)
        smtp.login(msg["From"], os.getenv('YOUR-PASSWORD'))
        smtp.send_message(msg)
        print('successfully sent the mail.')
        print('successfully sent the sms.')
