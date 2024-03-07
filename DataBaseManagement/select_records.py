import mysql.connector as con

mydb = con.connect(
    host="localhost",
    user="root",
    password="ijse@200108",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM STUDENT"
mycursor.execute(sql)
rows = mycursor.fetchall()
for row in rows :
    print(row)
mycursor.close()