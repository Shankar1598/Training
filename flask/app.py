# pip3 install flask
from flask import Flask, render_template
import mysql.connector

connection = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="secure_root",
  database="School"
)

cursor = connection.cursor()

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/login')
def login():
  # data
  # user_id=shankar & password=asdasda
  return render_template("login.html")

if __name__=="__main__":
  app.run(debug=True)