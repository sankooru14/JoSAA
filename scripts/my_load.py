import sqlite3
import pandas as pd

# Step 1: Read the CSV file into a DataFrame
file_path = "./JoSAA/my_data_table/all_IITs_filtered_16_to_23.csv"
df = pd.read_csv(file_path, low_memory=False)

# Step 2: Connect to the SQLite database
connection = sqlite3.connect('db.sqlite3')

# Step 3: Drop the table if it exists (optional, if you want to replace the table)
# Note: This step is not necessary if you use 'replace' in to_sql method
cursor = connection.cursor()
cursor.execute('''
DROP TABLE IF EXISTS MainApp_data_table
''')

# Step 4: Create the table with a primary key
cursor.execute('''
CREATE TABLE IF NOT EXISTS MainApp_data_table (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    institute TEXT,
    Branch TEXT,
    Category TEXT,
    Gender TEXT,
    Opening_rank INTEGER,
    Closing_rank INTEGER,
    year INTEGER,
    round INTEGER
)
''')

# Step 5: Insert the DataFrame data into the table
df.to_sql('MainApp_data_table', connection, if_exists='replace', index=False)

# Commit the transaction
connection.commit()

# Close the connection
connection.close()
