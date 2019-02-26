from flask_restful import Resource, reqparse
from database.database_helper import DBHelper


class Account(Resource):
    def get(self):
        return {'balance': DBHelper.get_balance()}


class Transactions(Resource):
    def get(self):
        return DBHelper.get_transactions()


class Deposit(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('amount',
                        type=float,
                        required=True,
                        help='Incorrect field name, type or resource (JSON) format.')

    def post(self):
        amount = Deposit.parser.parse_args()
        new_balance = DBHelper.update_balance(amount["amount"], credit=True)
        transaction = DBHelper.deposit(credit=amount["amount"], balance=new_balance)

        return transaction


class Withdraw(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('amount',
                        type=float,
                        required=True,
                        help='Incorrect field name, type or resource (JSON) format.')

    def post(self):
        amount = Withdraw.parser.parse_args()
        new_balance = DBHelper.update_balance(amount["amount"], credit=False)

        if not new_balance:
            return {'error': 'Cannot perform withdrawal. Balance would be below 0.'}, 403
        else:
            transaction = DBHelper.withdraw(debit=amount["amount"], balance=new_balance)
            return transaction
