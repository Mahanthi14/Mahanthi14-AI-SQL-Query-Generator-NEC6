import sqlite3
import pandas as pd

conn = sqlite3.connect("employee.db")

print(pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn))
print(pd.read_sql_query("SELECT * FROM employees;", conn))

conn.close()