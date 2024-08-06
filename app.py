from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("top.html")

@app.route("/tourokushityauyo")
def tourokushityauyo():
    return render_template("tourokushityauyo.html")

@app.route("/ichirannandayo")
def ichirannandayo():
    return render_template("ichirannandayo.html")

@app.route("/syuuseisurunoyo")
def syuuseisurunoyo():
    return render_template("syuuseisurunoyo.html")


app.run(debug=True)