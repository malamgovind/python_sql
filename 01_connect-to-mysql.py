import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MZRasbYywwRnRav7smuPeWU3LpZ0TBRU",
    database="collage"
)

if connection.is_connected():
    print("MySQL Connected Successfully!")

connection.close()
print("Connection Closed")