import mysql.connector as c
mydb = c.connect(
  host="localhost",
  user="root",
  password="1234",
  database="cust"
)
mycursor = mydb.cursor()

name=input("Enter your name")
id = input("Enter your id")

# mycursor.execute("DROP TABLE IF EXISTS student;")
# mycursor.execute("""
# CREATE TABLE student (
#     id VARCHAR(20),
#     name VARCHAR(20)
# );
# """)
mycursor.execute("insert into student values(%s,%s)",(id,name))
mycursor.execute("SELECT * FROM student;")
students=mycursor.fetchall();

for std in students:
  print(std)
mydb.commit()

