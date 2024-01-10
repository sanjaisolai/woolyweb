import pymysql
from en_de import *
from flask import Flask,render_template,url_for,request,redirect,session
import json
from shared import *
obj8=pymysql.connect(host="localhost",user="root",password="abcd",database="servers")
cur8=obj8.cursor()
cur8.execute("select * from servers_list;")
servers=list(cur8.fetchall())

#app=Flask(__name__)
@app.route('/servers_login',methods=["POST","GET"])
def ren_server():
    return render_template("server.html")
x=["username","password"]
@app.route("/submit_server",methods=["POST","GET"])
def submit_server():
    
    if(request.method=="POST"):
        dic={}
        for i in x:
            dic[i]=request.form[i]
        return redirect(url_for("complete_server",a=encrypt(json.dumps(dic))),code=307)
    elif(request.method=="GET"):
        return redirect("/servers_login")
#global var
r_server=[]
@app.route("/complete_server/<a>",methods=["POST","GET"])
def complete_server(a):
    if(request.method=="POST"):
        r_server.clear()
        a=decrypt(a)
        a=json.loads(a)
        for i in x:
            r_server.append(a[i])
        for i in servers:
            if(i[0]==r_server[0] and i[1]==r_server[1]):
                return redirect(url_for('server_authentication'),code=307)#"YOUR CREDENTIALS ARE CORRECT\nLOGIN SUCCESSFUL"
            
        return "INVALID LOGIN CREDENTIALS"
    elif(request.method=="GET"):
        return redirect('/servers_login')
'''if __name__=="__main__":
    app.run(debug=True)'''

