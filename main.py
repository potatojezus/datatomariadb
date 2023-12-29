#!/usr/bin/python 
import mariadb 

conn = mariadb.connect(
    user="pcpy",
    password="*NID.M@j0wc9pInCH",
    host="192.168.1.115",
    port=3306,
    database="Test1")

cur = conn.cursor() 

    
#insert information 
try: 
    cur.execute("""INSERT INTO TestTable1 (TestCol1, TestCol2, TestCol3, TestCol4) 
                    VALUES (?, ?, ?, ?)""", ("Maria", 3, 2, 2)) 
except mariadb.Error as e: 
    print(f"Error: {e}")

conn.commit() 
print(f"Last Inserted ID: {cur.lastrowid}")
    
conn.close()