import mysql.connector as con

mydb = con.connect(
    host="localhost",
    user="root",
    password="ijse@200108",
    database="mydatabase"
)

mycursor = mydb.cursor()
sql = "CREATE TABLE student (sindex VARCHAR (5) PRIMARY KEY ,name VARCHAR (255) NOT NULL,age INT)"
mycursor.execute(sql)
mycursor.close()

#varchar - maximum characters 5 - S0012 - S01
#char - maximum characters 5 - fixed -S0012- S01##
#int - integers
#Date - DateTime

#Constraint
#NotNull
#UNIQUE - Duplicate - (S001,S001)
#PRIMARY - NotNull+Unique
#AUTOINCREMENT - id - 1,id -2