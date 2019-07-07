from flask import Flask,render_template,request,url_for,redirect,session,flash
from db import *
from functools import wraps

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
global temp
temp = False
conn = connectDB()
cursor = conn.cursor(dictionary=True)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' is session:
            return f(*args, **kwargs)
        else:
            return 'cannot access'
    return decorated_function

@app.route("/")
def home():
    qs = "SELECT v.vendorId, v.serviceId, v.name vendorname, v.address, v.rating, v.lat, v.lon, s.name servicename, s.description, s.cost FROM vendors v, services s where v.serviceId=s.serviceId"
    cursor.execute(qs)
    res = cursor.fetchall()
    print(res)

    qs = "SELECT v.vendorId, v.productId, v.name vendorname, v.address, v.rating, v.lat, v.lon, p.name productname, p.description, p.cost FROM vendors v, products p where v.productId=p.productId "
    cursor.execute(qs)
    res1 = cursor.fetchall()
    print(res1)
    return render_template("index.html", users=res+res1)

@app.route("/search")
def search():
    query = request.args.get('query')
    qs = "SELECT v.vendorId, v.serviceId, v.name vendorname, v.address, v.rating, v.lat, v.lon, s.name servicename, s.description, s.cost FROM vendors v, services s where v.serviceId=s.serviceId AND v.name LIKE '%" + query + "%' OR s.name LIKE '%" + query + "%'"
    cursor.execute(qs)
    res = cursor.fetchall()
    print(res)

    qs = "SELECT v.vendorId, v.productId, v.name vendorname, v.address, v.rating, v.lat, v.lon, p.name productname, p.description, p.cost FROM vendors v, products p where v.productId=p.productId AND v.name LIKE '%" + query + "%' OR p.name LIKE '%" + query + "%'"
    print(qs)
    cursor.execute(qs)
    res1 = cursor.fetchall()
    print(res1)

    return render_template("index.html", users=res)

@app.route("/login", methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        userdetails = request.form
        userid = userdetails['email']
        passwed = userdetails['password']
        cursor.execute('select * from customers where email = %s', (userid,))
        res = cursor.fetchone()
        if(res is None):
            return 'Invalid credentials'
        elif(res['password'] == passwed):
            session['logged_in']=True
            global temp
            temp= True
            session['customerId']=int(res['customerId'])
            return redirect(url_for('home'))
    else:
        return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/vendorinfo")
def vendorinfo():
    return render_template("vendorinfo.html")

@app.route('/vendor')
def vendor():
    vendor = request.args.get('vendor')
    qs = "SELECT * FROM item i, vendors v WHERE i.vendorId=v.vendorId"
    cursor.execute(qs)
    res = cursor.fetchall()
    return render_template('vendor'+ vendor +'.html', items=res)

@app.route('/cart', methods = ["GET", "POST"])
def cart():
    if request.method == 'POST':
        inc = request.form
        # print(inc)
        items = inc.getlist('item')
        ordrs = {}
        qs = "SELECT * FROM item WHERE vendorId="+inc['venderId']
        cursor.execute(qs)
        res = cursor.fetchall()
        # print(res, items)
        for i in items:
            for j in res:
                # print(int(i), j["itemid"])
                if(int(i) == j["itemid"]):
                    ordrs[i] = [j["itemName"] ,inc['quantity'+str(i)], j["cost"]]
                    break
        # print(ordrs)
        print(session['customerId'])
        return render_template('cart.html', orders=ordrs, vendor=inc['venderId'], pay=inc['payment'], delivery=inc["delivery"])
    return redirect(url_for("home"))

@app.route("/order", methods=["GET", "POST"])
def order():
    if request.method == 'POST':
        inc = request.form
        items = inc.getlist("orders")
        quantity = inc.getlist("quantity")
        # print(items, quantity, inc, session["customerId"])
        item = ''
        for i in items:
            items += ':' + i
        quants = ''
        for i in quantity:
            quants += ':' + i
        qu = 'INSERT INTO order VALUES (null, %s, %s, %s, %s, %s, %s)'
        cursor.execute(qs, (inc['delivery'], inc['payment'], inc["vendorId"], session["customerId"], item, quants))
    return redirect(url_for("home"))
