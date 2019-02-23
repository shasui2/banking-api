import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = ("CREATE TABLE IF NOT EXISTS transaction_history ("
                "id INTEGER PRIMARY KEY,"
                "date text,"
                "credit text,"
                "debit text,"
                " balance float)"
                )
cursor.execute(create_table)

connection.commit()

connection.close()
