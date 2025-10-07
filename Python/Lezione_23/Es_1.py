from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() -> str:
    return "<h3>Hello world<h3>"


@app.route('/about')
def description() -> str:
    return "<h3>Mattia Di Giorgio is the author of this page, crazy right?<h3>"