import pymysql
from flask import Flask,render_template,url_for,request,redirect,session
import json
from shared import *
from en_de import *
obj6=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
cur6=obj6.cursor()

#app=Flask(__name__)
#@app.route('/')
@app.route('/general_customer_login',methods=["POST","GET"])
def ren_general():
    return render_template("general customer.html")
#global var
x_general=["name","gender","address","city","age","state","phone","aadhar","username","password"]

@app.route("/submit_general",methods=["POST","GET"])
def submit_general():
    if(request.method=="POST"):
        dic={}
        for i in x_general:
            dic[i]=request.form[i]
        return redirect(url_for("complete_general",a=encrypt(json.dumps(dic))),code=307)
    elif(request.method=="GET"):
        return redirect('/general_customer_login')
#global var
r_general=[]
@app.route("/complete_general/<a>",methods=["POST","GET"])
def complete_general(a):
    if(request.method=="POST"):
        a=decrypt(a)
        a=json.loads(a)
        r_general.clear()
        obj6=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
        cur6=obj6.cursor()
        cur7=obj6.cursor()
        cur7.execute("select aadhar from general_customer;")
        cur8=obj6.cursor()
        cur8.execute("select username from general_customer;")
        check3=list(cur8.fetchall())
        check2=list(cur7.fetchall())
        objz=pymysql.connect(host="localhost",user="root",password="abcd",database="aadhar")
        curz=objz.cursor()
        curz.execute("select aadhar_numbers from verified_aadhar;")
        check=list(curz.fetchall())
        for i in x_general:
            r_general.append(a[i])
        if(r_general[7] in [z[0] for z in check]):
            if(r_general[7] not in [y[0] for y in check2]):
                if(r_general[8] not in [x[0] for x in check3]):
                    cur6.execute("Insert into general_customer(cust_name,gender,cust_address,cust_city,age,cust_state,phoneno,aadhar,username,password) values"+str(tuple(r_general))+";")
                    obj6.commit()
                    return redirect('/')#"REGISTERED SUCCESSFULLY"
                else:
                    return "THIS USERNAME ALREADY EXISTS TRY SOMEOTHER"
            else:
                return "THIS AADHAR IS ALREADY REGISTERED"
        else:
            return "INVALID AADHAR"
    elif(request.method=="GET"):
        return redirect('/general_customer_login')

'''if __name__=="__main__":
    app.run(debug=True)'''

