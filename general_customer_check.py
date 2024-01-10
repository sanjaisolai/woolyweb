import pymysql
obj11=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
cur11=obj11.cursor()
cur11.execute("select username,password from general_customer;")
farmers_list=list(cur11.fetchall())
from flask import Flask,render_template,url_for,request,redirect,session
import json
from shared import *
from en_de import *
#app=Flask(__name__)
@app.route('/generalcust_check',methods=["POST","GET"])
def ren_generalcust_check():
    if "general_customer" in session:
        return redirect('/marketplace',code=307)
    return render_template("generalcust_check.html")
x_generalcust_check=["username","password"]
@app.route("/submit_generalcust_check",methods=["POST","GET"])
def a_submit_generalcust_check():
    if(request.method=="POST"):
        dic={}
        for i in x_generalcust_check:
            dic[i]=request.form[i]
        return redirect(url_for("complete_generalcust_check",a=encrypt(json.dumps(dic))),code=307)
    elif(request.method=="GET"):
        return redirect('/generalcust_check')
    
r_generalcust_check=[]
@app.route("/complete_generalcust_check/<a>",methods=["POST","GET"])
def complete_generalcust_check(a):
    if(request.method=="POST"):
        r_generalcust_check.clear()
        obj11=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
        cur11=obj11.cursor()
        cur11.execute("select username,password from general_customer;")
        farmers_list=list(cur11.fetchall())
        a=decrypt(a)
        a=json.loads(a)
        for i in x_generalcust_check:
            r_generalcust_check.append(a[i])
        print(r_generalcust_check)
        for j in farmers_list:
            print(j)
            if(str(j[0])==r_generalcust_check[0] and j[1]==r_generalcust_check[1]):
                session["general_customer"]=a["username"]
                return redirect(url_for('marketplace'),code=307)        
        return "INVALID LOGIN CREDENTIALS"
    elif(request.method=="GET"):
        return redirect('/generalcust_check')
'''if __name__=="__main__":
    app.run(debug=True)'''

