from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

# Steps:
# 1. Design and implement a database
#   - SQLite, MySql, Maria
#   - SQLAlchemy
# 2. Connect Database to Flask
# ----------
# 3. Project Design
# 4. Add in Machine Learning
# 5. Connect Machine Learning to Flask
# 6. ???
# 7. Profit < Have a good portfolio project

# Generating a flask App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Decorator that lets flask know what url path this function requires
@app.route("/")
def index():
  return jsonify({ "message": "This is a test" }) # The returned value gets sent directly

# HTTP Methods
# Get : http://server.com/path/to/url?arg=1&arg=2
# - Most Common
# - Send Unencrypted
# - Data is in the url
#
# Post, Put, Patch, Delete
# - Used to send data to the server
# - Data is encrypted in the body
# - Method can be used to indicate desired result

@app.route("/test/<username>", methods=["GET"])
def test(username):
  return f"Your Username is {username}"

# CRUD System
#
# Create  : POST
# Read    : GET
# Update  : PUT
# Delete  : DELETE

# http://server.com/path/to/query/<id>
# query 12: "What is your favorite <value>?"
# POST   : http://server.com/path/to/query -> create a user
# GET    : http://server.com/path/to/query/12 -> view user 12
# PUT    : http://server.com/path/to/query/12 -> change values on user 12
# DELETE : http://server.com/path/to/query/12 -> remove user 12

# E.G. http://server.com/path/to/query/12?value=Movie

# API: Application Programming Interface
# - Code someone else(or yourself) wrote to do a task and you're calling it
# - Package, Module, Library, SDK (usually means tools are included)

# If we're running this code directly then 
if __name__ == "__main__":
  # Start our Flask App
  app.run()