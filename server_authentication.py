#original
from flask import Flask, jsonify, render_template,session
import pymysql
from shared import *
import pymysql

list_min_max=[0,0]
obj13=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
cur13=obj13.cursor()
#app = Flask(__name__)
farmers=[]
@app.route('/server_authentication',methods=["POST","GET"])
def server_authentication():
    if(request.method=="POST"):
        return render_template("server_authentication2.html")
    elif(request.method=="GET"):
        return redirect('/servers_login')
@app.route('/get_data')
def get_data():
    print(list_min_max)
    farmers.clear()
    obj13=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
    cur13=obj13.cursor()
    cur13.execute("select fid,fname,age,no_of_sheeps,type_of_sheep,address,city,state from farmers where verification='n';")
    list_of_farmers_server_authentication=cur13.fetchall()
    for i in list_of_farmers_server_authentication:
        data = {'fid':i[0],'name':i[1],'age':i[2],'No_of_sheeps':i[3],'Type_of_sheep':i[4],'address':i[5],'city':i[6],'state':i[7]}
        farmers.append(data)
    return jsonify(farmers)
@app.route('/prices', methods=['POST'])
def get_price():
    list_min_max[0]=request.args.items("min-price")
    list_min_max[1]=request.args.items("max-price")
    print(list_min_max)
    return "SUCCESSFULLY UPDATED THE PRICES"
@app.route('/verify', methods=['POST'])
def verify():
    
    # Assuming you want to record the response data when the "Verify" button is clicked
    data = request.get_json()
    
    print(f"update farmers set verification='y' where fid={int(data['fid'])};")
    cur13.execute(f"update farmers set verification='y' where fid={int(data['fid'])};")
    obj13.commit()
    print("Done")
    return jsonify({"message": "Response recorded successfully"})

'''if __name__ == '__main__':
    app.run(debug=True)'''
