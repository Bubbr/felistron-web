from flask import Flask
from flask import render_template
import json

with open('bot.json', 'r') as f:
    data = json.load(f)

app = Flask(__name__)

class Category:
    name: str
    commands: dict

    def __init__(self, name) -> None:
        self.name = name
        self.commands = {}

class Command:
    name: str
    description: str
    nsfw: bool
    category: str
    usage: str
    aliases: list

commands = {}

for category in data["categories"]:
    commands[category] = Category(category)

for cmd_name in data["commands"]:
    cmd = data["commands"][cmd_name]

    comando = Command()
    comando.name = cmd["name"]
    comando.description = cmd["description"]
    comando.nsfw = cmd["nsfw"]

    commands[cmd["category"]].commands[cmd_name] = comando

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/help/")
def help():
    return render_template('help.html', categories=commands)

@app.route("/help/<category>/<cmd>")
def command(category, cmd):
    return render_template('cmd.html', command=commands[category].commands[cmd])