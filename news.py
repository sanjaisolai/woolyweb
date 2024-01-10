import pymysql
import json
from datetime import timedelta
from flask import Flask, render_template,request,url_for,redirect,session
from flask_session import Session
import feedparser
from flask_cors import CORS
from Farmers_personal import *
from Customer_company import*
from General_customer import *
from Servers import *
from Farmers_check import *
from general_customer_check import *
from cust_company_check import *
from server_authentication import *
from Bank_details import *
from photo_upload import *
from Product_description import *
from Marketplace import *
app.secret_key="@@wooly_web@@BY_team@@fiberflow"
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
app.config["SESSION_FILE_DIR"]="session"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)
app.config['SESSION_FILE_THRESHOLD'] = 100
Session(app)
CORS(app)
@app.route('/',methods=["POST","GET"])
def home0():
    feed = feedparser.parse('https://agritimes.co.in/feed')
    return render_template('news.html', entries=feed.entries,url='/1')
@app.route('/1',methods=["POST","GET"])
def home1():
    if(request.method=="POST"):
        feed = feedparser.parse('https://woolnews.net/feed/')
        return render_template('news.html', entries=feed.entries,url="/2")
    elif(request.method=="GET"):
        return redirect('/')
@app.route('/2',methods=["POST","GET"])
def home2():
    if(request.method=="POST"):
        feed = feedparser.parse('https://www.ibef.org/news.xml')
        return render_template('news.html', entries=feed.entries,url='/3')
    elif(request.method=="GET"):
        return redirect('/')
@app.route('/3',methods=["POST","GET"])
def home3():
    if(request.method=="POST"):
        feed = feedparser.parse('https://www.ibef.org/blog.xml')
        return render_template('news.html', entries=feed.entries,url='/re')
    elif(request.method=="GET"):
        return redirect('/')
@app.route('/re',methods=["POST","GET"])
def home4():
    if(request.method=="POST"):
        feed = feedparser.parse('https://agritimes.co.in/feed')
        return render_template('news.html', entries=feed.entries,url='/re2')
    elif(request.method=="GET"):
        return redirect('/')  
@app.route('/re2',methods=["POST","GET"])
def home5():
    if(request.method=="POST"):
        feed = feedparser.parse('https://agritimes.co.in/feed')
        return render_template('news.html', entries=feed.entries,url='/')
    elif(request.method=="GET"):
        return redirect('/') 
@app.route("/type_of_login_login",methods=["POST","GET"])
def type_of_login_login():
    return render_template("typeoflogin_login.html")
@app.route("/type_of_login",methods=["POST","GET"])
def type_of_login():
    return render_template("typeoflogin.html")
@app.route('/education',methods=["POST","GET"])
def education():
    feed = feedparser.parse('https://agritimes.co.in/feed')
    return render_template('news.html', entries='/education',url='/')
@app.route('/logout',methods=["POST","GET"])
def logout():
    session.clear()
    return redirect('/')
        
if __name__ == '__main__':
    app.run(debug=True)
