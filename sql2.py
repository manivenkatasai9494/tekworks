import mysql.connector as c
from tabulate import tabulate
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cust"
)
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, city) VALUES (%s, %s)"
values = ("MANI", "HYD")
mycursor.execute(sql, values)
mydb.commit()

print("Record inserted successfully!")
