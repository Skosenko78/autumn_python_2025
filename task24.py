# todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов
from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

@app.route("/about")
def page_about():
    return "<html><p>О компании</p></html>"

@app.route("/contacts")
def page_contacts():
    return "<html><p>Контакты</p></html>"

@app.route("/postslist")
def page_postslist():
    return "<html><p>Список постов</p></html>"