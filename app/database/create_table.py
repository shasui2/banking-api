import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS account (balance decimal DEFAULT (0.00) PRIMARY KEY)"
cursor.execute(create_table)

create_table = ("CREATE TABLE IF NOT EXISTS transaction_history ("
                "id INTEGER PRIMARY KEY,"
                "date date,"
                "credit text,"
                "debit text,"
                "balance decimal,"
                "FOREIGN KEY (balance) REFERENCES account (balance))"
                )
cursor.execute(create_table)

connection.commit()
connection.close()
