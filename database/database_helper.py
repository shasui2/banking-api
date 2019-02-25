import sqlite3
import datetime


class DBHelper:

    @staticmethod
    def insert(query):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        try:
            result = cursor.execute(query)
        except:
            return {'error': 'An error occurred inserting the item.'}, 500
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
    def get_transactions():
        result = DBHelper.query("select * from transaction_history")
        items = []

        for row in result:
            items.append({'id': row[0], 'date': row[1], 'credit': row[2], 'debit': row[3], 'balance': row[4]})

        return {'transactions': items}

    @staticmethod
    def get_datetime():
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def deposit(credit=None, balance=None):
        DBHelper.insert(
            "INSERT INTO transaction_history (date, credit, balance) VALUES ('{0}', {1}, {2})".format(
                DBHelper.get_datetime(),
                credit,
                balance))
        return {'new_balance': balance}

    @staticmethod
    def withdraw(debit=None, balance=None):
        DBHelper.insert(
            "INSERT INTO transaction_history (date, credit, balance) VALUES ('{0}', {1}, {2})".format(
                DBHelper.get_datetime(),
                debit,
                balance))
        return {'new_balance': balance}

    @staticmethod
    def get_balance():
        balance = DBHelper.query("select balance from account").fetchone()[0]
        return float("{0:.2f}".format(balance))

    @staticmethod
    def update_balance(amount, credit=True):
        balance = DBHelper.get_balance()
        if credit:
            balance += amount
            balance = float("{0:.2f}".format(balance))
            DBHelper.insert("UPDATE account SET balance={0}".format(balance))
            return balance
        else:
            balance -= amount
            balance = float("{0:.2f}".format(balance))
            if balance < 0:
                return False
            else:
                DBHelper.insert("UPDATE account SET balance={0}".format(balance))
                return balance
