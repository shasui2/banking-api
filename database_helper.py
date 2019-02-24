import sqlite3


class DBHelper:

    @staticmethod
    def insert(query):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute(query)
        connection.commit()
        connection.close()
        return result

    @staticmethod
    def query(query):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        result = cursor.execute(query)
        return result

    @staticmethod
    def deposit(date=None, credit=None, balance=None):
        DBHelper.insert(
            "INSERT INTO transaction_history (date, credit, balance) VALUES ('{0}', {1}, {2})".format(date, credit,
                                                                                                      balance))

    @staticmethod
    def withdraw(date=None, debit=None, balance=None):
        DBHelper.insert(
            "INSERT INTO transaction_history (date, debit, balance) VALUES ('{0}', {1}, {2})".format(date, debit,
                                                                                                     balance))

    @staticmethod
    def get_balance():
        balance = DBHelper.query("select balance from account").fetchone()[0]
        return float("{0:.2f}".format(balance))

    @staticmethod
    def update_balance(amount, credit=True):
        balance = DBHelper.get_balance()
        if credit:
            balance += amount
            float("{0:.2f}".format(balance))
            DBHelper.insert("UPDATE account SET balance={0}".format(balance))
            return balance
        else:
            balance -= amount
            float("{0:.2f}".format(balance))
            DBHelper.insert("UPDATE account SET balance={0}".format(balance))
            return balance
