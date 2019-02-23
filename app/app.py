from flask import Flask
from flask_restful import Resource, Api, reqparse
from app.endpoints import Deposit, Withdraw, Account
import datetime

app = Flask(__name__)
api = Api(app)

transaction_history = []
balance = 0.00
accounts = [{
    'name': 'My Account',
    'current_account': [
        {
            'balance': balance
        }]
}]


api.add_resource(Account, '/account')
api.add_resource(Deposit, '/deposit')
api.add_resource(Withdraw, '/withdraw')

app.run(port=5000, debug=True)
