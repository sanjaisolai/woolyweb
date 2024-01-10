import pymysql
from en_de import *
#from Farmers_personal import Countoffarmers
from flask import Flask,render_template,url_for,request,redirect,session
import json
from shared import*
obj20=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
obj201=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
cur20=obj20.cursor() 
cur201=obj201.cursor()
cur201.execute("select fid from farmers;")
lst=list(cur201.fetchall())
print(len(lst))
#app=Flask(__name__)
'''@app.route('/bank_details',methods=["POST"])
def ren_bank():
    return render_template("bank details.html")'''
#global var
x_bank=["bank name","ifsc code","acc number"]

@app.route("/submit_bank",methods=["POST","GET"])
def submit_bank():
    if(request.method=="POST"):
        dic={}
        for i in x_bank:
            dic[i]=request.form[i]
        return redirect(url_for("complete_bank",a=encrypt(json.dumps(dic))),code=307)
    elif(request.method=="GET"):
        return "<H1 style='font-family:arial;text-align:center;color:red;'>YOU CANNOT DIRECTLY ACCESS THIS PAGE</H1>";

#global var
r_bank=[]
@app.route("/complete_bank/<a>",methods=["POST","GET"])
def complete_bank(a):
    if (request.method=="POST"):
        lst=[]
        obj2012=pymysql.connect(host="localhost",user="root",database="woolyweb",password="abcd")
        cur2012=obj2012.cursor()
        cur2012.execute("Select fid from farmers;")
        lst=list(cur2012.fetchall())
        a=decrypt(a)
        a=json.loads(a)
        print(lst)
        for i in x_bank:
            r_bank.append(a[i])
        if(lst):
            r_bank.append(lst[-1][0])
        else:
            obj2012=pymysql.connect(host="localhost",user="root",database="woolyweb",password="abcd")
            cur2012=obj2012.cursor()
            cur2012.execute("Select fid from farmers;")
            r_bank.append(cur2012.fetchall()[-1][0])
        try:
            cur20.execute("Insert into account_details(bank_name,ifsc_code,account_number,fid) values"+str(tuple(r_bank))+";")
        except Exception as e:
            return "WEBSITE FAILED TO LOAD PLEASE TRY AGAIN" + e;
        obj20.commit()
        return redirect(url_for('photo_upload'),code=307)
    elif(request.method=="GET"):
        return redirect('/')

'''if __name__=="__main__":
    app.run(debug=True)'''

