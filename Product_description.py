from flask import Flask, render_template, request,session
import pymysql
from shared import *
#app = Flask(__name__)
obj222=pymysql.connect(host="localhost",user="root",database="woolyweb",password="abcd")
obj22=pymysql.connect(host="localhost",user="root",database="woolyweb",password="abcd")
cur22=obj22.cursor()
cur222=obj222.cursor()
cur222.execute("select fid from farmers;")
fid_list_product_description=list(cur222.fetchall())
@app.route('/product_description',methods=["POST","GET"])
def product_description():
    if(request.method=="POST"):
        return render_template('productinfo.html')
    elif(request.method=="GET"):
        return redirect('/farmer_check')

description_list=[]
@app.route('/description_cost', methods=["POST","GET"])
def description_cost():
    if request.method == "POST":
        obj222=pymysql.connect(host="localhost",user="root",database="woolyweb",password="abcd")
        cur222=obj222.cursor()
        cur222.execute("select fid from farmers;")
        fid_list_product_description=list(cur222.fetchall())
        description_list.append(fid_list_product_description[-1][0])
        description_list.append(request.form['desc_get'])
        description_list.append(request.form['cost_get'])
        cur22.execute("Insert into description values"+str(tuple(description_list))+"")
        obj22.commit()
        return redirect('/')#data entered successfully
    if(request.method=="GET"):
        return redirect('/farmer_check')


'''if __name__ == "__main__":
    app.run(debug=True)'''