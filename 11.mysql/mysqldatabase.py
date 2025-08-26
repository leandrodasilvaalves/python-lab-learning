import mysql.connector

def show_databases(db):
    cursor = db.cursor()
    print("SHOW DATABASES")
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(f"database: {x}")


def show_tables(db):
    cursor = db.cursor()
    print("SHOW TABLES")
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(f"table: {x}")

def remove_database(db):
    cursor = db.cursor()
    print("Removing database...")
    cursor.execute("DROP DATABASE mydatabase")
    


mydb = mysql.connector.connect(
    user="root", 
    password="passw0rd",
    host="localhost"
)

# remove_database(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")

show_databases(mydb)

mydb = mysql.connector.connect(
    user="root",
    password="passw0rd",
    host="localhost",
    database="mydatabase"
) 

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

show_tables(mydb)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE employees (" \
    " id INT AUTO_INCREMENT PRIMARY KEY, " \
    " name VARCHAR(255), " \
    " address VARCHAR(255))")

show_tables(mydb)

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")









































# remove_database(mydb)