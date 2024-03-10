import mysql.connector as con

object = con.connect(host="localhost",
                     user="root",
                     password="root123",
                     db="CompERP")

with object.cursor() as cursor:
    query = "Insert into workers values(%s,%s,%s,%s);"
    values = (142, "Jani", 22, "Matara")
cursor.execute(query, values)
object.commit()

cursor.execute("Select * from workers")
rows = cursor.fetchall()

for row in rows:
    print(row)

object.close()