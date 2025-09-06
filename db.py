from mysql.connector import connect, Error

try:
    with connect(
        host="127.0.0.1", port=3307,user="new_dev", password="Naruto-1342-1342", database="csconer"
    )as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees")
        for row in cursor.fetchall():
            print(row)
    pass
except Error as e:
    print(e)