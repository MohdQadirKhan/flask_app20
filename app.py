from flask import Flask
app=Flask(__name__)
@app.route("/")
def welcome():
    return "Hello Guys  Qadir   Here!"
@app.route("/home")
def home():
    return "This is  home page!"
from controller import product_controller, user_controller,product_categories_controller

