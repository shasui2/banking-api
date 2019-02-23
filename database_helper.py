import sqlite3


class DbHelper:
    @staticmethod
    def query(query, date=None, credit=None, debit=None, balance=None):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute(query, (date, credit, debit, balance))
        return {"date": date, "credit": credit, "debit": debit, "balance": balance}

    @staticmethod
    def get_balance(query):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        balance = cursor.execute(query)
        print("QUERY: " + str(balance.fetchone()))
        return {"balance": balance}

    @staticmethod
    def update_balance(amount, credit=True):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        balance = cursor.execute("select balance from account")
        if credit:
            balance += amount
            cursor.execute("UPDATE account SET balance=?", balance)
            return balance
        else:
            balance -= amount
            cursor.execute("UPDATE account SET balance=?", balance)
            return balance
