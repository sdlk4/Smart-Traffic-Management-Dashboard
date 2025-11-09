import mysql.connector
from config import MYSQL

try:
    conn = mysql.connector.connect(**MYSQL)
    print("MySQL Connected Successfully!")
    conn.close()
except Exception as e:
    print("Connection Failed:", e)
