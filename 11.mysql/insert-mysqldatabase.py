import mysqlhelper as helper

connection = helper.create_connection()
cursor = connection.cursor()

helper.create_database(cursor, "insert_class_db")
helper.create_table(cursor, "customers")
helper.show_databases(cursor)
helper.show_tables(cursor)


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
cursor.execute(sql, val)
connection.commit()
print("1 record inserted, ID:", cursor.lastrowid)

sql = "INSERT INTO customers(name, address) VALUES (%s, %s)"
val = [
    ('Leandro','Av. João Araújo, 1004'),
    ('Meirilene','Av. João Araújo, 1004'),
    ('Isabella','Av. João Araújo, 1004'),
    ('Leonardo','Av. João Araújo, 1004'),
]

cursor.executemany(sql, val)
connection.commit()
print(f"{len(val)} records inserted. Last ID: ", cursor.lastrowid)

connection.close()