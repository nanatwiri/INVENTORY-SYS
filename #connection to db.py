# connection to db
import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='inventory'
)
cursor = connection.cursor()
cursor.execute('SELECT * FROM products')
results = cursor.fetchall()
cursor.close()
connection.close()
