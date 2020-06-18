import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):
    response = table.get_item(
        Key={
           "id": '123456'
       }
     )
    print(response)
    return {
         'statusCode': 200,
         'body': response
     }
       

