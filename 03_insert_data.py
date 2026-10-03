import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MZRasbYywwRnRav7smuPeWU3LpZ0TBRU",
    database="collage"
)

cursor = conn.cursor()

sql = "INSERT INTO student05 (id,name,marks,age) VALUES (%s,%s,%s,%s)"
values = (5,'my',99,10)

cursor.execute(sql,values)
conn.commit()

print("data inserted successfully!")
cursor.close()
conn.close()