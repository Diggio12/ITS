from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "<h3>Hello world<h3>"

@app.route("/square/<int:n>")
def quadrato(n: int) -> str:
    return str(n**2)