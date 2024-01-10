#not original
from flask import Flask, jsonify, render_template
import pymysql
from shared import *
import pymysql
list_min_max=[0,0]
obj13=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
cur13=obj13.cursor()
#app = Flask(__name__)
farmers=[]
@app.route('/server_authentication')
def server_authentication():
    return render_template("server_authentication2.html")
@app.route('/get_data')
def get_data():
    farmers.clear()
    list_min_max[0] = request.form.get('min-price') 
    list_min_max[1] = request.form.get('max-price')
    cur13.execute("select fid,fname,age,no_of_sheeps,type_of_sheep,address,city,state from farmers where verification='n';")
    list_of_farmers_server_authentication=cur13.fetchall()
    for i in list_of_farmers_server_authentication:
        data = {'fid':i[0],'name':i[1],'age':i[2],'No_of_sheeps':i[3],'Type_of_sheep':i[4],'address':i[5],'city':i[6],'state':i[7]}
        farmers.append(data)
    return jsonify(farmers)
@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    print(f"update farmers set verification='y' where fid={int(data['fid'])};")
    cur13.execute(f"update farmers set verification='y' where fid={int(data['fid'])};")
    obj13.commit()
    return jsonify({"message": "Response recorded successfully"})

'''if __name__ == '__main__':
    app.run(debug=True)'''
