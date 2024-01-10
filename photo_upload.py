from flask import Flask,request,render_template,redirect,url_for,session
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from en_de import *#my module
import os
import pymysql
from shared import *

conn21=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
conn201=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
cur21=conn21.cursor()
cu201=conn201.cursor()
cu201.execute("select fid from farmers;")
lst=list(cu201.fetchall())
temp_photo_upload=''
x_upload=['description','price']
#app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
@app.route('/photo_upload',methods=["POST","GET"])
def photo_upload():
    if(request.method=="POST"):
        return render_template('upload_page.html')
    elif(request.method=="GET"):
        return redirect('/farmer_check')
@app.route('/store', methods=['POST',"GET"])
def upload():
    if(request.method=="POST"):
        global temp_photo_upload
        if 'image' not in request.files:
            return redirect(request.url)
        image = request.files['image']
        if image.filename == '':
            return redirect(request.url)
        if image:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        # os.makedirs(os.path.dirname(filename), exist_ok=True)
            image.save(filename)
        return redirect(url_for("to_drive",f_path=encrypt(filename)),code=307)
    elif(request.method=="GET"):
        return redirect('/farmer_check')
@app.route("/to_drive/<f_path>",methods=["POST","GET"])
def to_drive(f_path):
    if(request.method=="POST"):
        global temp_photo_upload
        f_path=decrypt(f_path)
        credentials = service_account.Credentials.from_service_account_file(
        'woolyweb-7c906051fa0c.json', scopes=['https://www.googleapis.com/auth/drive'])#providing access
        try:        
            drive_service = build('drive', 'v3', credentials=credentials)#providing access
            file_name = f_path#having the file and the path name same
            file_path = f_path
            file_metadata = {
            'name': file_name
            }
            media = MediaFileUpload(file_path, resumable=True) #uploading the file
            uploaded_file = drive_service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
            ).execute()
        
            print(f'File ID: {uploaded_file["id"]}')
            file_id = uploaded_file['id']
            drive_service.permissions().create(
                    fileId=file_id,
                    body={
                        'role': 'reader',
                        'type': 'anyone',
                        }
                    ).execute()
            direct_link = f'https://drive.google.com/uc?id={file_id}'
            temp_photo_upload=f_path
            return redirect(url_for('link_upload',link=encrypt(direct_link)),code=307)
        except Exception as e:
            return f"An error occurred: {str(e)}"
    elif(request.method=="GET"):
        return redirect('/farmer_check')
    
@app.route("/link_upload/<link>",methods=["POST","GET"])
def link_upload(link):
    if(request.method=="POST"):
        link=decrypt(link)
        os.remove(temp_photo_upload)
        conn21=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
        cur21=conn21.cursor()
        conn201=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
        cur201=conn201.cursor()
        cur201.execute("select fid from farmers;")
        lst=list(cur201.fetchall())
        try:
            cur21.execute(f"INSERT INTO photos VALUES ({lst[-1][0]},%s);", (link,))
        except:
            return "IMAGE INSERTION FAILED"
        conn21.commit()
        return redirect(url_for('product_description'),code=307)
    elif(request.method=="GET"):
        return redirect('/farmer_check')

'''if __name__ == '__main__':
    app.run(debug=True)'''











