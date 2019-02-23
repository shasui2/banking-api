from flask import Flask
from flask_restful import Api
from app.api.endpoints import Deposit, Withdraw, Account

app = Flask(__name__)
api = Api(app)

api.add_resource(Account, '/account')
api.add_resource(Deposit, '/deposit')
api.add_resource(Withdraw, '/withdraw')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
