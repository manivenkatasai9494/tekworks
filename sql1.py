import mysql.connector
from tabulate import tabulate

# Connect to MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM student;")
rows = cursor.fetchall()
headers = ["Sno", "Sname", "Marks", "City", "MobileNumber", "Gender"]

print(tabulate(rows, headers, tablefmt="grid"))


cursor.close()
connection.close()
