import pandas as pd
from sqlalchemy import create_engine

# Define database connection parameters
user = 'root'
password = '1234'
host = 'localhost'
database = 'datascience'

# Create the connection string
connection_string = f'mysql+mysqlconnector://{user}:{password}@{host}/{database}'

# Create an SQLAlchemy engine
engine = create_engine(connection_string)

print("*"*30)
# Query the 'user_information' table
df_user_info = pd.read_sql('SELECT * FROM user_information', engine)
print("User Information:")
print(df_user_info)
print("*"*30)


# Query the 'workout_data' table
df_workout_data = pd.read_sql('SELECT * FROM workout_data', engine)
print("\nWorkout Data:")
print(df_workout_data)

print("*"*30)
user_csv_path = 'eda.csv'  # Path to the CSV file for user information
df_user_info_csv = pd.read_csv(user_csv_path)
print("\nEda from CSV:")
print(df_user_info_csv)

merge_df = pd.merge(df_user_info,df_workout_data,on='user_id',how='outer')

print("*"*30)
print("merged data")
print(merge_df)