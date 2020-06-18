import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

id = "123456"
firstname = "Darksha"
lastname = "Parween"

def lambda_handler(event, context):
    table.update_item(
        Key={
            "id": id,
            "firstname": firstname,
            "lastname": lastname
        }
    )
    response = {
        'message': 'Item update successfully'
    }
    return {
        'statuscode': 200,
        'body': response
    }


