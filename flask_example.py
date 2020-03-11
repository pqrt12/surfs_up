from flask import Flask

# crate a Flask instance
app = Flask(__name__)

# create a root.
@app.route('/')
def hello_world():
    return "Hello world"

