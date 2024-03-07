import mysql.connector as con

mydb = con.connect(
    host="localhost",
    user="root",
    password="ijse@200108",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "DELETE FROM student WHERE sindex=%s"
val=([16964])
mycursor.execute(sql,val)
mydb.commit()
mycursor.close()
