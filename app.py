import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/datatable")
def table():
    return render_template("table.html")



if __name__ == "__main__":
    app.run()