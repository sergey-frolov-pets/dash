from flask_mail import Message
from app import mail

#TODO Почитать документация Flask-Mail (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)