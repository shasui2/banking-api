import boto3
import json
from database.database_helper import DBHelper

# For a Boto3 client.
ddb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')


def handler(event, context):
    amount = json.loads(event['body'])
    new_balance = DBHelper.update_balance(amount["amount"], credit=True)
    transaction = DBHelper.deposit(credit=amount["amount"], balance=new_balance)
    print("Transaction: {0}".format(transaction))

    return {"statusCode": 200, "body": json.dumps(transaction)}


