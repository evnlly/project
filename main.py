import requests
import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()
# Create a table to store the data
cursor.execute("""CREATE TABLE IF NOT EXISTS weather (id INTEGER PRIMARY KEY,city TEXT,temperature REAL)""")
# Make a request to the API
url = """https://api.openweathermap.org/data/2.5/weather?q=London&appid=260b5b182544012edb36092f71e4b1a"""
response = requests.get(url)
data = response.json()
# Extract the relevant data
city = data["name"]
temperature = data["main"]["temp"]
# Insert the data into the table
cursor.execute("INSERT INTO weather (city, temperature) VALUES (?, ?)",
               (city, temperature)
               )
# Commit the changes to the database
conn.commit()
# Close the connection to the database
conn.close()

import tracemalloc
import sys
def do_something_usefull(n):
    data = [1 for _ in range(n)]
    return data
def do_something_else_usefull(n, m, step=1):
    data = [[1 for _ in range(n)] for _ in range(0, m, step)]
    return data
def execute_and_get_memory_usage(function, *args, **kwargs):
        tracemalloc.start()
        before = tracemalloc.get_traced_memory()
        result = function(*args, **kwargs)
        data = function(*args)
        after = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"According to tracemalloc: { after[1] - before[1]} ")
        print(f"According to sys: { sys.getsizeof(data)} ")
        return result
print('1D example:')
execute_and_get_memory_usage(do_something_usefull, 10)
print('\n2D example:')
execute_and_get_memory_usage(do_something_else_usefull, 10, 10, step=2)