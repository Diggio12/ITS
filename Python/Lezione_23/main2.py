from flask import Flask

app = Flask(__name__)
#app.run(debug=True, host='127.0.0.1', port=4000)

@app.route('/')
def home() -> str:
    return "<h3>Hello world<h3>"
