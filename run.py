import os

# This imports Flask (The capital F is important as it is a class).
from flask import Flask

# This is creating an instance of the Flask import and storing it in "app".
# __name__ is a built in python varible needs this so it knows where to look
# for templates ect
app = Flask(__name__)


# This is a python decorator, all python decorators start with @app.
# A decorator is a way of wrapping functions.
# When trying to go to the route directory the function is triggered as
# indicated by route("/").
@app.route("/")
def index():
    return "Hello, World"


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
        debug=True
        )