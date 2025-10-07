from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "<h3>Hello world<h3>"

@app.route('/user/<string:nome>')
def benvenuto(nome: str) -> str:
    return f"Benvenuto {nome}"