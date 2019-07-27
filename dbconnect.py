#!/usr/bin/python
import cgi
import mysql.connector as mysql
print('Content-type:text/html')
print("")

username = 'admin'
password = '128'
database_name = 'data'

webdata = cgi.FieldStorage()
name = webdata.getvalue('uname')
email = webdata.getvalue('email')
mobile = webdata.getvalue('mobile')
conn = mysql.connect(user=username,password=password,database=database_name,host='data.cpd8fs5xt95n.us-east-1.rds.amazonaws.com')
cur = conn.cursor()
cur.execute(f"insert into datageeks values({name},{email},{mobile});")
print(cur.fetchall())
conn.close
