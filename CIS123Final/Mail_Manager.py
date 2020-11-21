import os
import smtplib
from email.message import EmailMessage


class MailManager:
    def __init__(self, mail_address=os.environ.get('EMAIL_ADDRESS'), mail_password=os.environ.get('EMAIL_PASSWORD')):
        self.mailAddress = mail_address
        self.mailPassword = mail_password

    def send_letter(self, recipient='Me@gmail.com', title='Insert Title Here', content='', *args):
        letter = EmailMessage()
        letter['Subject'] = title
        letter['From'] = self.mailAddress
        letter['To'] = recipient
        letter.set_content(content)

        if args is not None:
            for file_path in args:
                with open(file_path, 'rb') as file:
                    letter.add_attachment(file.read(), maintype='application', subtype='plain', filename=file.name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.mailAddress, self.mailPassword)
            smtp.send_message(letter)
