from flask import Flask

print("Aplicacion iniciada")

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo!"

app.run()
