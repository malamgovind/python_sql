import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql-password",
    database="collage"
)

cursor = conn.cursor()

sql = "DELETE FROM student05 WHERE id = %s"
values = (5,)

cursor.execute(sql,values)
conn.commit()

print("data delete successfully!")
cursor.close()
conn.close()