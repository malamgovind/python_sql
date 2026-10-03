import mysql.connector
conn = None
cursor = None

try: 
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MZRasbYywwRnRav7smuPeWU3LpZ0TBRU",
        database="collage"
    )
    cursor = conn.cursor()

    sql = "INSERT INTO student05 VALUES (%s,%s,%s,%s)"
    values = (55,'yo', 88, 50)

    cursor.execute(sql,values)
    conn.commit()
    print("data inserted successfully!")

except mysql.connector.Error as error:
    if conn is not None:
        conn.rollback()
    print("database error:",error)

finally:
    if cursor is not None:
        cursor.close()
    if conn is not None and conn.is_connected():
        conn.close()
    print("connection close")