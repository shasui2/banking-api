import sqlite3


class DbHelper:
    @staticmethod
    def query(query, date=None, credit=None, debit=None, balance=None):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute(query, (date, credit, debit, balance))
        return {"date": date, "credit": credit, "debit": debit, "balance": balance}

    @staticmethod
    def deposit(date=None, credit=None, balance=None):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO transaction_history (date, credit, balance) VALUES ({0}, {1}, {2})".format(date, credit, balance)
        cursor.execute(query)
        connection.commit()
        connection.close()

    @staticmethod
    def get_balance(query):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        balance = cursor.execute(query)
        print("QUERY: " + str(cursor.execute("SELECT balance FROM account").fetchone()))
        connection.commit()
        connection.close()
        return {"balance": balance.fetchone()}

    @staticmethod
    def update_balance(amount, credit=True):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        balance = float(cursor.execute("select balance from account").fetchone()[0])
        connection.commit()
        if credit:
            print(str(balance) + str(amount))
            balance += amount
            cursor.execute("UPDATE account SET balance={0}".format(balance))
            connection.commit()
            return balance
        else:
            balance -= amount
            cursor.execute("UPDATE account SET balance={0}".format(balance))
            connection.commit()
            return balance
