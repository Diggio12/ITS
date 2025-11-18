from flask import Flask, make_response, redirect, request
from pathlib import Path
from urllib.parse import unquote, urlparse, parse_qs

app = Flask(__name__)
STATIC_DIR = Path("static")

# ---------------------------
# Helper: serve file HTML
# ---------------------------
def serve_html(filename: str):
    path = STATIC_DIR / filename
    if not path.exists():
        return make_response("<h1>404 - File non trovato</h1>", 404)

    html = path.read_text(encoding="utf-8")
    resp = make_response(html, 200)
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    return resp

# ---------------------------
# 1) Pagina HTML via parametro
#    /html/home -> static/home.html
# ---------------------------
@app.route("/html/<page>")
def html_page(page):
    if page != "riservata":
        return serve_html(f"{page}.html")
    
    # Ha chiesto la pagina riservata!
    # qui gestisco eventualmente il login
    # dovrei capire se ha un token oppure se ha un cookie
    # il cookie lo chiamiamo "session"
    # Lo cerco il cookies
    cookies = request.cookies
    cookie = cookies.get("session")
    if cookie == None:
        # il cookie session non c'è, cosa faccio?
        # Cerco se nella richiesta c'è una parte query contenente token=<valore>
        token = request.args.get("token")
        if token == None:
            #devo fare una redirect al server idm
            return redirect(f"http://127.0.0.1:10000/login?http://127.0.0.1:5000/{page}", code=302)
        else:
            #fornisco il cookie
            pass
        pass
    pass

# Shortcut: home
@app.route("/")
def root():
    return serve_html("home.html")

# ---------------------------
# 2) Redirect 302 verso una pagina HTML
#    /go/errore -> 302 -> /html/errore
# ---------------------------
@app.route("/go/<target>")
def go(target):
    return redirect(f"/html/{target}", code=302)

# ---------------------------
# 3) Set cookie
#    /setcookie -> imposta cookie "sessionid"
# ---------------------------
@app.route("/setcookie")
def setcookie():
    resp = serve_html("home.html")
    # Impostiamo un cookie semplice
    resp.set_cookie("sessionid", "abc123", path="/")
    return resp

# ---------------------------
# 4) Lettura cookie
#    /showcookie -> mostra tutti i cookie ricevuti
# ---------------------------
@app.route("/showcookie", methods=["POST"])
def showcookie1():
    print("Ciao")
    return make_response("", 200)


@app.route("/showcookie", methods=["GET"])
def showcookie():
    # Tutti i cookie parsati da Flask
    cookies = request.cookies

    html = "<h1>Cookie ricevuti</h1><pre>"
    for k, v in cookies.items():
        html += f"{k} = {v}\n"
    html += "</pre><a href='/'>Torna alla home</a>"

    resp = make_response(html, 200)
    resp.headers["Content-Type"] = "text/html; charset=utf-8"
    return resp

# ---------------------------
# Avvio server
# ---------------------------
if __name__ == "__main__":
    STATIC_DIR.mkdir(exist_ok=True)
    app.run(host="10.70.1.148", port=5000, debug=True)