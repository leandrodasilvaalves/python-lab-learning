import mysql.connector

__connection = None


def create_connection():
    __connection = mysql.connector.connect(
        user="root", password="passw0rd", host="localhost"
    )
    return __connection


def create_database(cursor=None, database_name="mydatabase"):
    if cursor is None:
        cursor = __connection.cursor()
    cursor.execute(f"CREATE DATABASE {database_name}")
    cursor.execute(f"USE {database_name}")


def show_databases(cursor=None):
    if cursor is None:
        cursor = __connection.cursor()
    print("SHOW DATABASES")
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(f"database: {x}")


def drop_database(cursor=None, database_name="mydatabase"):
    if cursor is None:
        cursor = __connection.cursor()
    cursor.execute(f"DROP DATABASE {database_name}")


def create_table(cursor=None, table="employees"):
    if cursor is None:
        cursor = __connection.cursor()
    cursor.execute(
        f"CREATE TABLE {table} ("
        " id INT AUTO_INCREMENT PRIMARY KEY, "
        " name VARCHAR(255), "
        " address VARCHAR(255))"
    )


def show_tables(cursor=None):
    if cursor is None:
        cursor = __connection.cursor()
    print("SHOW TABLES")
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(f"table: {x}")
