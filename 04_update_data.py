import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql-password",
    database="collage"
)

cursor = conn.cursor()

sql = "UPDATE student05 SET name = %s WHERE id = %s"
values = ('hiros', 5)

cursor.execute(sql,values)
conn.commit()

print("data updated successfully!")

cursor.close()
conn.close()