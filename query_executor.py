import sqlite3
import pandas as pd

def execute_query(sql):

    conn = sqlite3.connect("employee.db")

    df = pd.read_sql_query(sql, conn)

    conn.close()

    return df