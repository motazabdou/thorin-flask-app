import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    # "r" in the line below means json is opening the file as a read-only
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title = "About", company = data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title = "Contact Us")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title = "Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("port", "5000")),
        debug=True
    )