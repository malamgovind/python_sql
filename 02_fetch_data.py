import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql-password",
    database="collage"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM student05")

row = cursor.fetchone()
print("fetchone():",row)

rows = cursor.fetchall()
print("fetchall():",rows)

cursor.close()
conn.close()