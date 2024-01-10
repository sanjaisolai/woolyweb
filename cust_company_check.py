import pymysql
from en_de import*
obj12=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
cur12=obj12.cursor()
cur12.execute("select gstin,password from customer_company;")
present_users=list(cur12.fetchall())
from flask import Flask,render_template,url_for,request,redirect,session
from shared import *
import json
#app=Flask(__name__)
@app.route('/cust_company_check',methods=["POST","GET"])
def ren_cust_company_check():
    if "customer_company_customer" in session:
        return redirect('/marketplace',code=307)
    return render_template("cust_company_check.html")
x_cust_company_check=["gstin","password"]
@app.route("/submit_cust_company_check",methods=["POST","GET"])
def a_submit_cust_company_check():
    if(request.method=="POST"):
        dic={}
        for i in x_cust_company_check:
            dic[i]=request.form[i]
        return redirect(url_for("complete_cust_company_check",a=encrypt(json.dumps(dic))),code=307)
    elif(request.method=="GET"):
        return redirect('/')
r_cust_company_check=[]
@app.route("/complete_cust_company_check/<a>",methods=["POST","GET"])
def complete_cust_company_check(a):

    if (request.method=="POST"):
        r_cust_company_check.clear()
        obj12=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
        cur12=obj12.cursor()
        cur12.execute("select gstin,password from customer_company;")
    
        a=decrypt(a)
        a=json.loads(a)
        for i in x_cust_company_check:
            r_cust_company_check.append(a[i])
        for i in present_users:
            if(str(i[0])==r_cust_company_check[0] and i[1]==r_cust_company_check[1]):
                session["customer_company_customer"]=a["gstin"]
                return redirect(url_for('marketplace'),code=307)        
        return "INVALID LOGIN CREDENTIALS"
    elif(request.method=="GET"):
        return redirect('/')

'''if __name__=="__main__":
    app.run(debug=True)'''

