import json
from database.database_helper import DBHelper


def handler(event, context):
    return {"statusCode": 200, "body": json.dumps({'balance': DBHelper.get_balance()})}
