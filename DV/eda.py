import numpy as np
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

print("*" * 30)

# Query the 'user_information' table
df_user_info = pd.read_sql('SELECT * FROM user_information', engine)
print("User Information:")
print(df_user_info)
print("*" * 30)

# Query the 'workout_data' table
df_workout_data = pd.read_sql('SELECT * FROM workout_data', engine)
print("\nWorkout Data:")
print(df_workout_data)

print("*" * 30)

# Path to the CSV file for session data
csv_path = 'eda.csv'  # Make sure this is the correct path
df_session_data = pd.read_csv(csv_path)
print("\nSession Data from CSV:")
print(df_session_data)

print("*" * 30)

# Merge the 'user_information' and 'workout_data' DataFrames
merged_user_workout_df = pd.merge(df_user_info, df_workout_data, on='user_id', how='outer')
print("Merged User and Workout Data:")
print(merged_user_workout_df)

# Merge the 'session_data' (from CSV) with the merged DataFrame
final_merged_df = pd.merge(merged_user_workout_df, df_session_data, on='user_id', how='outer')

print("*" * 30)
print("Final Merged Data (User Info + Workout Data + Session Data):")
print(final_merged_df)

print("=" * 40)
print("*" * 10 + ' Memory Details ' + "*" * 10)

# Example DataFrame (replace this with your actual DataFrame)
df = pd.read_csv('eda.csv')  # or use any DataFrame you have

# Get memory usage for each column
memory_usage_per_column = df.memory_usage(deep=True)

# Print memory usage by column
print("Memory Usage by Column:")
print(memory_usage_per_column)

# Optionally, if you want the total memory usage of the entire DataFrame
total_memory_usage = df.memory_usage(deep=True).sum()
print("\nTotal Memory Usage of DataFrame: ", total_memory_usage, "bytes")
print("=" * 40)

# Converting 'session_id' column to int16 to reduce memory usage
df['session_id'] = df['session_id'].astype(np.int16)

# Verifying the conversion
print("\nData after conversion:")
print(df.dtypes)  # This will show the new data types for all columns

# Optionally, check the memory usage again after conversion
print("\nMemory Usage After Conversion:")
print(df.memory_usage(deep=True))
