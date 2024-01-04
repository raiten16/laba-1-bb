from flask import Flask, jsonify
from datetime import datetime
from lab1 import app



@app.route("/")
def hello_user():
    return f"<p>Hello!</p><a href='/healthcheck'>Check</a>"


@app.route("/healthcheck")
def healthcheck():
    resp = jsonify(date=datetime.now(), status="OK")
    resp.status_code = 200
    return resp
