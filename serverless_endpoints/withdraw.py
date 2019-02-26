import json
from database.database_helper import DBHelper


def handler(event, context):
    print("Event: {0}".format(json.loads(event['body'])))
    amount = json.loads(event['body'])
    new_balance = DBHelper.update_balance(amount["amount"], credit=False)

    if not new_balance:
        return {"statusCode": 403, "body": json.dumps({'error': 'Cannot perform withdrawal. Balance would be below 0.'})}
    else:
        transaction = DBHelper.withdraw(debit=amount["amount"], balance=new_balance)
        return {"statusCode": 200, "body": json.dumps(transaction)}
