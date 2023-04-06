import os

import json

# This imports Flask (The capital F is important as it is a class).
# render_template allows flask to read in files inside templates folder.
from flask import Flask, render_template

# This is creating an instance of the Flask import and storing it in "app".
# __name__ is a built in python varible needs this so it knows where to look
# for templates ect
app = Flask(__name__)


# This is a python decorator, all python decorators start with @app.
# A decorator is a way of wrapping functions.
# This links my HTML pages
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    # This is opening compnay.json as read only ("r")
    # and storing it inside json_data then loading it into the data var
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    # The arguments allows to pass data in
    return render_template("about.html", page_title="About", company=data)


# Runs when ou cick on a member
@app.route("/about/<member_name>")
def about_member(member_name):
    memeber = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        # loops and gets correct member object
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# This runs the app with the following arguments.
# __main__ is the name of the default madual in python.
if __name__ == "__main__":
    app.run(
        # This gets the IP inviroment varible if exsists,
        # sets default value if not found
        host=os.environ.get("IP", "0.0.0.0"),
        # Port 5000 is Aa common port used by Flask
        port=int(os.environ.get("PORT", "5000")),
        # This will allow me to debug my code easier during devlop stage.
        # Never leave this in final code, This allows arbatrary code to run.
        # Set to False before submitting code!
        debug=True
        )