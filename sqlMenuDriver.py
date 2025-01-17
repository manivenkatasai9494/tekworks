import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cust"
)

mycursor = mydb.cursor()
mycursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
  emp_id VARCHAR(20),
  emp_name VARCHAR(50),
  department VARCHAR(30),
  salary DECIMAL(10, 2),
  joining_date DATE
);
""")


# Function to insert employee details
def insert_employee():
    emp_name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))
    joining_date = input("Enter joining date (YYYY-MM-DD): ")

    mycursor.execute(
        "INSERT INTO employee (emp_id, emp_name, department, salary, joining_date) VALUES (%s, %s, %s, %s, %s)",
        (emp_id, emp_name, department, salary, joining_date))
    mydb.commit()
    print("Employee details inserted successfully!")


# Function to delete employee by id
def delete_employee():
    emp_id = input("Enter employee ID to delete: ")
    mycursor.execute("DELETE FROM employee WHERE emp_id = %s", (emp_id,))
    mydb.commit()
    print("Employee details deleted successfully!")


# Function to update employee details
def update_employee():
    emp_id = input("Enter employee ID to update: ")
    new_name = input("Enter new employee name: ")
    new_department = input("Enter new department: ")
    new_salary = float(input("Enter new salary: "))
    new_joining_date = input("Enter new joining date (YYYY-MM-DD): ")

    mycursor.execute(
        "UPDATE employee SET emp_name = %s, department = %s, salary = %s, joining_date = %s WHERE emp_id = %s",
        (new_name, new_department, new_salary, new_joining_date, emp_id))
    mydb.commit()
    print("Employee details updated successfully!")


# Function to display all employee details
def display_all_employees():
    mycursor.execute("SELECT * FROM employee")
    employees = mycursor.fetchall()

    if employees:
        print("\nAll Employee Details:")
        for emp in employees:
            print(emp)
    else:
        print("No employee records found.")


# Function to display employees sorted by name in ascending order
def display_employees_by_name():
    mycursor.execute("SELECT * FROM employee ORDER BY emp_name ASC")
    employees = mycursor.fetchall()

    if employees:
        print("\nEmployees Sorted by Name (Ascending):")
        for emp in employees:
            print(emp)
    else:
        print("No employee records found.")


# Function to display employees with salary between 50000 and 100000
def display_employees_by_salary_range():
    mycursor.execute("SELECT * FROM employee WHERE salary BETWEEN 50000 AND 100000")
    employees = mycursor.fetchall()

    if employees:
        print("\nEmployees with salary between 50000 and 100000:")
        for emp in employees:
            print(emp)
    else:
        print("No employees found in this salary range.")


# Function to display employees from a specific department
def display_employees_from_department():
    department = input("Enter department name: ")
    mycursor.execute("SELECT * FROM employee WHERE department = %s", (department,))
    employees = mycursor.fetchall()

    if employees:
        print(f"\nEmployees from {department} department:")
        for emp in employees:
            print(emp)
    else:
        print(f"No employees found in the {department} department.")


# Menu-Driven Program
def menu():
    while True:
        print("\nMenu:")
        print("1. Insert Employee Details")
        print("2. Delete Employee Details by Employee ID")
        print("3. Update Employee Details")
        print("4. Display All Employees")
        print("5. Display Employees Sorted by Name (Ascending)")
        print("6. Display Employees with Salary Between 50000 and 100000")
        print("7. Display Employees from a Specific Department")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            insert_employee()
        elif choice == '2':
            delete_employee()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            display_all_employees()
        elif choice == '5':
            display_employees_by_name()
        elif choice == '6':
            display_employees_by_salary_range()
        elif choice == '7':
            display_employees_from_department()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the menu-driven program
menu()
