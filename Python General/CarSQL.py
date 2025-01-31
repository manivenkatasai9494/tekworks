import mysql.connector as c

# Establishing database connection
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cust"
)

mycursor = mydb.cursor()

# Creating car_details table
# mycursor.execute("""
# CREATE TABLE IF NOT EXISTS car_details (
#     car_id VARCHAR(20) PRIMARY KEY,
#     car_name VARCHAR(50),
#     manufacturer VARCHAR(50),
#     price DECIMAL(10, 2),
#     year INT,
#     fuel_type VARCHAR(20),
#     horsepower INT,
#     features VARCHAR(500)
# );
# """)

def insert_car():
    car_id = input("Enter car ID: ")
    car_name = input("Enter car name: ")
    manufacturer = input("Enter manufacturer: ")
    price = float(input("Enter price: "))
    year = int(input("Enter year of manufacture: "))
    fuel_type = input("Enter fuel type: ")
    horsepower = int(input("Enter horsepower: "))
    features = input("Enter features: ")

    mycursor.execute(
        "INSERT INTO car_details (car_id, car_name, manufacturer, price, year, fuel_type, horsepower, features) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (car_id, car_name, manufacturer, price, year, fuel_type, horsepower, features))
    mydb.commit()
    print("Car details inserted successfully!")

def delete_car():
    car_id = input("Enter car ID to delete: ")
    mycursor.execute("DELETE FROM car_details WHERE car_id = %s", (car_id,))
    mydb.commit()
    print("Car details deleted successfully!")

def update_car():
    car_id = input("Enter car ID to update: ")
    new_name = input("Enter new car name: ")
    new_manufacturer = input("Enter new manufacturer: ")
    new_price = float(input("Enter new price: "))
    new_year = int(input("Enter new year: "))
    new_fuel_type = input("Enter new fuel type: ")
    new_horsepower = int(input("Enter new horsepower: "))
    new_features = input("Enter new features: ")

    mycursor.execute(
        "UPDATE car_details SET car_name = %s, manufacturer = %s, price = %s, year = %s, fuel_type = %s, horsepower = %s, features = %s WHERE car_id = %s",
        (new_name, new_manufacturer, new_price, new_year, new_fuel_type, new_horsepower, new_features, car_id))
    mydb.commit()
    print("Car details updated successfully!")

def display_all_cars():
    mycursor.execute("SELECT * FROM car_details")
    cars = mycursor.fetchall()

    if cars:
        print("\nAll Car Details:")
        for car in cars:
            print(car)
    else:
        print("No car records found.")

def display_cars_by_name():
    mycursor.execute("SELECT * FROM car_details ORDER BY car_name ASC")
    cars = mycursor.fetchall()

    if cars:
        print("\nCars Sorted by Name (Ascending):")
        for car in cars:
            print(car)
    else:
        print("No car records found.")


def display_cars_by_price_range():
    min_price = float(input("Enter minimum price: "))
    max_price = float(input("Enter maximum price: "))
    mycursor.execute("SELECT * FROM car_details WHERE price BETWEEN %s AND %s", (min_price, max_price))
    cars = mycursor.fetchall()

    if cars:
        print(f"\nCars within price range {min_price} and {max_price}:")
        for car in cars:
            print(car)
    else:
        print("No cars found in this price range.")
def display_cars_by_fuel_type():
    fuel_type = input("Enter fuel type: ")
    mycursor.execute("SELECT * FROM car_details WHERE fuel_type = %s", (fuel_type,))
    cars = mycursor.fetchall()

    if cars:
        print(f"\nCars with {fuel_type} fuel type:")
        for car in cars:
            print(car)
    else:
        print(f"No cars found with {fuel_type} fuel type.")
def menu():
    while True:
        print("\nMenu:")
        print("1. Insert Car Details")
        print("2. Delete Car Details by Car ID")
        print("3. Update Car Details")
        print("4. Display All Cars")
        print("5. Display Cars Sorted by Name (Ascending)")
        print("6. Display Cars Within a Specific Price Range")
        print("7. Display Cars by Fuel Type")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            insert_car()
        elif choice == '2':
            delete_car()
        elif choice == '3':
            update_car()
        elif choice == '4':
            display_all_cars()
        elif choice == '5':
            display_cars_by_name()
        elif choice == '6':
            display_cars_by_price_range()
        elif choice == '7':
            display_cars_by_fuel_type()
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
menu()