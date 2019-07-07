from flask import Flask,render_template,request,url_for,redirect,session,flash
from db import *
from functools import wraps

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
global temp
temp = False
conn = connectDB()
cursor = conn.cursor(dictionary=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/active')
def active():
    qs = "SELECT o.orderId,c.name, o.items, o.quantity, o.modeOfPayment, o.modeOfPayment FROM orders o, customers c where o.customerId=c.customerId AND o.vendorId=1 AND o.status='pending'"
    cursor.execute(qs)
    res = cursor.fetchall()
    fin = res
    totalitem = []
    ls = []
    totalquant = []
    for i in res:
        items = i["items"].split(':')
        # print(items)
        items = list(map(int, items))
        
        quantity = i["quantity"].split(':')
        quantity = list(map(int, quantity))
        its = []
        for i in items:
            qs = "SELECT * FROM item where itemid="+str(i)
            cursor.execute(qs)
            res = cursor.fetchone()
            its.append(res["itemName"])
        # print(its, quantity)
        totalitem.append(its)
        ls.append(len(its))
        totalquant.append(quantity)
    print(fin, totalitem, totalquant, len(fin), ls)
    return render_template('active.html', rec=fin, items=totalitem, quantity=totalquant, l=len(fin), ll=ls)

@app.route('/accept')
def accept():
    ono = request.args.get('order')
    qs = "UPDATE orders SET status='accept' where orderId="+ono
    cursor.execute(qs)
    conn.commit()
    return redirect(url_for("active"))

@app.route('/reject')
def reject():
    ono = request.args.get('order')
    qs = "UPDATE orders SET status='reject' orderId="+ono
    cursor.execute(qs)
    conn.commit()
    return redirect(url_for("active"))

@app.route('/current')
def current():
    qs = "SELECT o.orderId,c.name, o.items, o.quantity, o.modeOfPayment, o.modeOfPayment FROM orders o, customers c where o.customerId=c.customerId AND o.vendorId=1 AND o.status='accept'"
    cursor.execute(qs)
    res = cursor.fetchall()
    fin = res
    totalitem = []
    ls = []
    totalquant = []
    for i in res:
        items = i["items"].split(':')
        # print(items)
        items = list(map(int, items))
        
        quantity = i["quantity"].split(':')
        quantity = list(map(int, quantity))
        its = []
        for i in items:
            qs = "SELECT * FROM item where itemid="+str(i)
            cursor.execute(qs)
            res = cursor.fetchone()
            its.append(res["itemName"])
        # print(its, quantity)
        totalitem.append(its)
        ls.append(len(its))
        totalquant.append(quantity)
    print(fin, totalitem, totalquant, len(fin), ls)
    return render_template('current.html', rec=fin, items=totalitem, quantity=totalquant, l=len(fin), ll=ls)

@app.route('/close')
def close():
    return render_template("invoice.html")