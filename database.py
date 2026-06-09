import sqlite3
import pandas as pd

df = pd.read_csv("data/employees.csv")

conn = sqlite3.connect("employee.db")

df.to_sql(
    "employees",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("employees table created successfully in employee.db")