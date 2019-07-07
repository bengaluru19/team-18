from mysql.connector import connect

def connectDB(host='localhost',database='codeforgood',user='root',password='root',):
    return connect(host=host,database=database,user=user,password=password)