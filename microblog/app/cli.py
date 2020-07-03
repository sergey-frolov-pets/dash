import os
import click
from app import app

# Имя команды происходит от имени декорированной функции, а справочное сообщение 
# поступает из docstring. Поскольку это родительская команда, которая существует 
# только для обеспечения базы для подкоманд, самой функции ничего не нужно делать.

@app.cli.group()
def translate():
    """Translation and localization commands."""
    pass

@translate.command()
def update():
    """Update all languages."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system('pybabel update -i messages.pot -d app/translations'):
        raise RuntimeError('update command failed')
    os.remove('messages.pot')

@translate.command()
def compile():
    """Compile all languages."""
    if os.system('pybabel compile -d app/translations'):
        raise RuntimeError('compile command failed')

@translate.command()
@click.argument('lang')
def init(lang):
    """Initialize a new language."""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')
    if os.system(
            'pybabel init -i messages.pot -d app/translations -l ' + lang):
        raise RuntimeError('init command failed')
    os.remove('messages.pot')

'''
содержимое файла babel.cfg (находится в папке проекта)
[python: app/**.py]
[jinja2: app/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_

Последним шагом для включения этих команд является их импорт, чтобы команды регистрировались. 
Я решил сделать это в файле microblog.py в каталоге верхнего уровня:
from app import cli
'''