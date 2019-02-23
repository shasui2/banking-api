from flask_restful import Resource, reqparse
import sqlite3

# Given a client makes a deposit of 1000 on 10-01-2012
# And a deposit of 2000 on 13-01-2012
# And a withdrawal of 500 on 14-01-2012
# When she prints her bank statement
# Then she would see
# date || credit || debit || balance
# 14/01/2012 || || 500.00 || 2500.00
# 13/01/2012 || 2000.00 || || 3000.00
# 10/01/2012 || 1000.00 || || 1000.00

# POST - POST is used to send data to a server to create/update a resource.
# GET  - GET is used to request data from a specified resource.

# GET  /account
# POST   /withdraw/<string:balance>
# POST   /deposit

class Deposit(Resource):
    TABLE_NAME = 'transaction_history'

    parser = reqparse.RequestParser()
    parser.add_argument('amount',
                        type=float,
                        required=True,
                        help='This field cannot be empty.')

    def post(self):
        global balance

        amount = Deposit.parse_args()

        if amount is None:
            return {'error': 'Amount is None'}, 400

        transaction_date = datetime.datetime.now().strftime('%d/%m/%Y')
        balance += amount["amount"]
        transaction_history.append({'date': transaction_date,
                                    'credit': amount,
                                    'new_balance': balance})

        return {'accounts': accounts}

    def deposit_to_db(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

class Withdraw(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('amount',
                        type=float,
                        required=True,
                        help='This field cannot be empty.')

    def post(self):
        global balance

        amount = Withdraw.parse_args()

        if amount is None:
            return {'error': 'Amount is None'}, 400

        transaction_date = datetime.datetime.now().strftime('%d/%m/%Y')
        balance += amount["amount"]
        transaction_history.append({'date': transaction_date,
                                    'debit': amount,
                                    'balance': balance})
        return {'accounts': accounts}


class Account(Resource):
    def get(self):
        return {'accounts': accounts, 'transaction_history': transaction_history}
