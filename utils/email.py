from flask_mail import Mail, Message
from app import app

mail = Mail(app)

def send_email(recipient_email, subject, message):
    msg = Message(subject, recipients=[recipient_email])
    msg.body = message
    mail.send(msg)
