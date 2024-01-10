import pymysql
obj10=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
cur10=obj10.cursor()
cur10.execute("select fid,password from farmers;")
farmers_list=list(cur10.fetchall())
from shared import *
from flask import Flask,render_template,url_for,request,redirect
import json
from en_de import *
#app=Flask(__name__)
@app.route('/farmer_check',methods=["POST","GET"])
def ren_farmer_check():
    return render_template("farmer_check.html")
x_farmer_check=["farmer username","password"]
@app.route("/submit_farmer_check",methods=["POST","GET"])
def a_submit_farmer_check():
    if(request.method=="POST"):
        dic={}
        for i in x_farmer_check:
            dic[i]=request.form[i]
        return redirect(url_for("complete_farmer_check",a=encrypt(json.dumps(dic))),code=307)
    elif(request.method=="GET"):
        return redirect('/farmer_check')
r_farmer_check=[]
@app.route("/complete_farmer_check/<a>",methods=["POST","GET"])
def complete_farmer_check(a):
    if(request.method=="POST"):
        r_farmer_check.clear()
        a=decrypt(a)
        a=json.loads(a)
        for i in x_farmer_check:
            r_farmer_check.append(a[i])
        for i in farmers_list:
            if(str(i[0])==r_farmer_check[0] and i[1]==r_farmer_check[1]):
                return "YOUR CREDENTIALS ARE CORRECT\nLOGIN SUCCESSFUL"        
        return "INVALID LOGIN CREDENTIALS"
    elif(request.method=="GET"):
        return redirect('/farmer_check')
'''if __name__=="__main__":
    app.run(debug=True)'''

