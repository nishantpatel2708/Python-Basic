import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password='vinod2001',db="chirag")
mycursor=conn.cursor()
# query="sho"
mycursor.execute("SHOW databases")
# print(mycursor)
for i in mycursor:
    print(i)