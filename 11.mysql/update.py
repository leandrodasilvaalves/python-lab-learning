import helper

connection = helper.create_connection()
cursor = connection.cursor()

database = "mycompay_db"
cursor.execute(f"USE {database}")
helper.show_tables(cursor)

sql = "UPDATE customers SET name = 'João' WHERE name = 'John'"
cursor.execute(sql)

sql = "UPDATE customers SET address='av 21' WHERE address='Highway 21'"
cursor.execute(sql)
connection.commit()

print(cursor.rowcount, "Record(s) affected")
