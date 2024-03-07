import mysql.connector as con

mydb = con.connect(
    host="localhost",
    user="root",
    password="ijse@200108",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "UPDATE student SET name=%s,age=%s WHERE sindex=%s"
val=('Chavindu',22,16965)
mycursor.execute(sql,val)
mydb.commit()
mycursor.close()
