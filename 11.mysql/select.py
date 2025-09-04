import helper

connection = helper.create_connection()
cursor = connection.cursor(buffered=True)

database = "mycompay_db"

cursor.execute(f"USE {database}")
helper.show_tables(cursor)

print(''.ljust(50, '.'))
print('Fetching all records')
cursor.execute(f"SELECT * FROM customers")
for row in cursor.fetchall():
    print(row)

print(''.ljust(50, '.'))
print('Fetching one record')
cursor.execute(f"SELECT * FROM customers")
row = cursor.fetchone()
print(row)

print(''.ljust(50, '.'))
print('Prevent SQL Injection')
sql = f"SELECT * FROM customers WHERE name LIKE %s"
cursor.execute(sql, ("Le%",)) 
for row in cursor.fetchall():
    print(row)

print(''.ljust(50,'.'))
print('Limiting results 1')
sql = "SELECT * FROM customers LIMIT 3"
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)

print(''.ljust(50,'.'))
print('Limiting results 2')
sql = "SELECT * FROM customers LIMIT 2 OFFSET 2"
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)





connection.close()