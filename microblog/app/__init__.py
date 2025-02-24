# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment #INFO см. https://momentjs.com/
from flask_babel import Babel,  _, lazy_gettext as _l

app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'
login.login_message = _l('Please log in to access this page.')

mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)

from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app import routes, models, db, cli
from app.models import User, Post

import os
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=3)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

@babel.localeselector
def get_locale():
    #return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'ru'

#FIXME Ошибки по Email НЕ РАБОТАЕТ!!! Исправить как в конце статьи тут: https://habr.com/ru/post/346880/
"""
from logging.handlers import SMTPHandler

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
"""