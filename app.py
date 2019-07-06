from flask import Flask,render_template,request,url_for,redirect,session,flash
from db import *
from functools import wraps

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
global temp
temp = False
conn = connectDB()
cursor = conn.cursor(dictionary=True)

@app.route("/")
def menu():
    return render_template("home.html")

