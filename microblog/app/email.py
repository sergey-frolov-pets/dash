from flask import render_template
from flask_mail import Message
from app import app, mail

from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))

#INFO Почитать документация Flask-Mail (https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support)

'''
Если вы хотите использовать эмулированный почтовый сервер

Чтобы настроить этот сервер, необходимо установить две переменные среды:
(venv) $ set MAIL_SERVER=localhost
(venv) $ set MAIL_PORT=8025

Запускаем в ОТДЕЛЬНОМ cmd эмулированный почтовый сервер:
(venv) $ python -m smtpd -n -c DebuggingServer localhost:8025
---------
ИЛИ по-честному отправляем через gmail
(venv) $ set MAIL_SERVER=smtp.googlemail.com
(venv) $ set MAIL_PORT=587
(venv) $ set MAIL_USE_TLS=1
(venv) $ set MAIL_USERNAME=<your-gmail-username>
(venv) $ set MAIL_PASSWORD=<your-gmail-password>

!!!Помните, что параметры безопасности вашей учетной
записи Gmail могут препятствовать приложению отправлять электронную почту через нее
https://support.google.com/accounts/answer/6010255?hl=en

Для демонстрации работы Flask-Mail, я покажу вам, как отправить электронное письмо 
из оболочки Python. Для этого запустите Python с flask shell, а затем выполните 
следующие команды:

>>> from flask_mail import Message
>>> from app import mail
>>> msg = Message('test subject', sender=app.config['ADMINS'][0],
... recipients=['your-email@example.com'])
>>> msg.body = 'text body'
>>> msg.html = '<h1>HTML body</h1>'
>>> mail.send(msg)
'''