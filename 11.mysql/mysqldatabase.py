import mysqlhelper as helper

connection = helper.create_connection()
cursor = connection.cursor()

helper.create_database(cursor, "first_database")
helper.show_databases(cursor)
cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

helper.show_tables(cursor)

helper.create_table(cursor)
helper.show_tables(cursor)

cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

connection.close()