import mysql.connector as con

mydb = con.connect(
    host="localhost",
    user="root",
    password="ijse@200108",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "INSERT INTO student (sindex,name,age) VALUES (%s,%s,%s)"
val=('16965','Kaveesha',21)
mycursor.execute(sql,val)
mydb.commit()
mycursor.close()

