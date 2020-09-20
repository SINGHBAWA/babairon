from flask_mail import Mail, Message
import os

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USERNAME": "amansinghbawa@gmail.com",
    "MAIL_PASSWORD": "Bawa7800"
}


class EmailService:
    def __init__(self, app):
        self.app = app
        app.config.update(mail_settings)
        self.mail = Mail(app)

    def send_mail(self, recipient, message):
        msg = Message(subject=f"Query from {recipient}",
                      sender=self.app.config.get("MAIL_USERNAME"),
                      recipients=[self.app.config.get("MAIL_USERNAME"), ],  # replace with your email for testing
                      body=message)
        self.mail.send(msg)

        msg = Message(subject="Baba iron and cement store - Query submitted",
                      sender=self.app.config.get("MAIL_USERNAME"),
                      recipients=[recipient, ],  # replace with your email for testing
                      body=f"Hi,\nYour query is submitted we will contact you soon\n\nDetails:\n{message}\n\nThank you,\nBaba Iron and cement store\n")
        self.mail.send(msg)
