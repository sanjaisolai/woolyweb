import pymysql
obj=pymysql.connect(host="localhost",user="root",password="abcd",database="woolyweb")
cur=obj.cursor()
cur.execute("select * from farmers")
print(cur.fetchall())