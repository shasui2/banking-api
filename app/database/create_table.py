import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS account (balance float DEFAULT (0.00) PRIMARY KEY)"
cursor.execute(create_table)

create_table = ("CREATE TABLE IF NOT EXISTS transaction_history ("
                "id INTEGER PRIMARY KEY,"
                "date date,"
                "credit text,"
                "debit text,"
                "balance float,"
                "FOREIGN KEY (balance) REFERENCES account (balance))"
                )
cursor.execute(create_table)

cursor.execute("INSERT INTO account (balance) VALUES (0.00)")

connection.commit()
connection.close()
