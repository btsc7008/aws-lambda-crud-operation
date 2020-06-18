import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    table.put_item(
        Item={
            "id": '0786',
            "firstname": 'Pravat',
            "lastname": 'Behera'
        }
    )
    response = {
        'message': 'Item added'
    }
    return {
        'statuscode': 200,
        'body': response
    }
