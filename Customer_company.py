import pymysql
from flask import Flask,render_template,url_for,request,redirect,session
import json
from shared import *
from en_de import *
obj2=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
cur2=obj2.cursor()


@app.route('/customer_company_login',methods=["POST","GET"])
def ren_customer():
    return render_template("customer company.html")
#global var
x_customer=["name","address","city","state","gstin","password"]

@app.route("/submit_customer",methods=["POST","GET"])
def submit_customer():
    if(request.method=="POST"):
        dic={}
        for i in x_customer:
            dic[i]=request.form[i]
        return redirect(url_for("complete_customer",a=encrypt(json.dumps(dic))),code=307)
    elif(request.method=="GET"):
        return redirect('/')
#global var
r_customer=[]
@app.route("/complete_customer/<a>",methods=["POST","GET"])
def complete_customer(a):
    if(request.method=="POST"):
        r_customer.clear()
        obj2=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
        cur2=obj2.cursor()
        obje=pymysql.connect(host="localhost",user="root",password="abcd",database="cust_company")
        cure=obje.cursor()
        cur=obj2.cursor()
        cur.execute("select gstin from customer_company;")
        check2=list(cur.fetchall())
        cure.execute("select * from verified_gstin;")
        check=list(cure.fetchall())
        a=decrypt(a)
        a=json.loads(a)
        for i in x_customer:
            r_customer.append(a[i])
        if((r_customer[4] in [z[0] for z in check])):
            if(r_customer[4] not in [k[0] for k in check2]):
                cur2.execute("Insert into customer_company(name,company_address,company_city,company_state,gstin,password) values"+str(tuple(r_customer))+";")
                obj2.commit()
            else:
                return "YOUR GSTIN IS ALREADY REGISTERED"
        else:
            return "YOUR GSTIN IS NOT VALID"
        return redirect('/')#after successful registration
    elif(request.method=="GET"):
        return redirect('/')

'''if __name__=="__main__":
    app.run(debug=True)'''

