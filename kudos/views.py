from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/createUser")
def create_user():
    return "user has been created!"
