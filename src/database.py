import sqlite3


connection = sqlite3.connect("healthcare.db")

print("Database connection created.")


with open("sql/create_tables.sql", "r") as file:
    sql_script = file.read()


connection.executescript(sql_script)

connection.commit()

print("Tables created successfully.")

connection.close()