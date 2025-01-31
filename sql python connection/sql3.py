import mysql.connector as c
from tabulate import tabulate

# Establish database connection
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cust"
)

# Create a cursor object
mycursor = mydb.cursor()


#mycursor.execute("DROP TABLE IF EXISTS student;")
mycursor.execute("""
CREATE TABLE student (
    Sno INT,
    Sname VARCHAR(20),
    marks INT,
    city VARCHAR(20),
    mobileNumber VARCHAR(15),
    gender VARCHAR(10)
);
""")

# Commit changes to the database
mydb.commit()


