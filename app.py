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
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    query = request.args.get('query')
    qs = "SELECT v.vendorId, v.name vendorname, v.address, v.rating, v.lat, v.lon, s.name servicename, s.description, s.cost FROM vendors v, services s where v.serviceId=s.serviceId AND v.name LIKE '%" + query + "%' OR s.name LIKE '%" + query + "%'"
    cursor.execute(qs)
    res = cursor.fetchall()
    print(res)

    qs = "SELECT v.vendorId, v.name vendorname, v.address, v.rating, v.lat, v.lon, p.name productname, p.description, p.cost FROM vendors v, products p where v.productId=p.productId AND v.name LIKE '%" + query + "%' OR p.name LIKE '%" + query + "%'"
    cursor.execute(qs)
    res1 = cursor.fetchall()
    print(res1)

    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/vendorinfo")
def vendorinfo():
    return render_template("vendorinfo.html")