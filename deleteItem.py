import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    table.delete_item(
        Key={
            "id": '0786'
            
        }
    )
    response = {
        'message': 'Item deleted'
    }
    return {
        'statuscode': 200,
        'body': response
    }