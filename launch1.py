#!/usr/bin/python3
import cgi
import subprocess 
import os
import cgitb
import random
import mysql.connector as mysql
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("jainhimani1999@gmail.com", "honeypagal@123gml")
message = "Registred"
s.sendmail("jainhimani1999@gmail.com", "intern3tgovernance@gmail.com", message)
s.quit()                                                                                                                                                                

ip=subprocess.getoutput("curl http://169.254.169.254/latest/meta-data/public-ipv4")
ip=ip.split('\n')[-1]
print("Content-type: text/html\r\n\r\n") 
print("<center>")
print('</br><img src="https://cssauthor.com/wp-content/uploads/2018/06/Copper-Loader.gif"  width="400" height="200" >') 
ports=[line.split(":")[-1] for line in subprocess.getoutput("netstat -tunlep | grep LISTEN | awk '{print $4}'")]
while True:
	port=random.randrange(2000,65535)
	if port not in ports:
		break
port=str(port)
webdata=cgi.FieldStorage()
name=webdata.getvalue('uname')
email=webdata.getvalue('email')
mobile=webdata.getvalue('phone')
conn=mysql.connect(user="root",password="vijay",database="data",host='localhost')
cur=conn.cursor()
cur.execute(f"""insert into datageeks VALUES (%s,%s,%s)""",(name,email,mobile))
conn.commit()
conn.close()
try:
	id=subprocess.getoutput("sudo docker run -d -p "+port+":80 datageekhindi")
	print('<iframe id="frame1" src="http://13.127.254.208/safal.html" width="100%" height="450px" frameBorder="0"></iframe>')
	print('<meta http-equiv = "refresh" content = "2; url = http://'+ip+':'+port+'/" />')
except:
	print('<iframe id="frame1" src="http://13.127.254.208/register.html" frameBorder="0" width="100%" height="450px"></iframe>')
	print('<meta http-equiv = "refresh" content = "2; url = http://'+ip+'/2.html" />')
	exit(1)
print('<meta http-equiv = "refresh" content = "2; url = http://'+ip+':'+port+'/" />')
print("</br>")	
print("</center>")
