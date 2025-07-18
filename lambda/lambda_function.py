import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('resume-visitor-counter')

def lambda_handler(event, context):
    # Ignore OPTIONS (preflight) requests
    if event['requestContext']['http']['method'] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': 'https://uchennaokoronkwo.com',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'message': 'CORS preflight'})
        }

    response = table.update_item(
        Key={'id': 'visitorCount'},
        UpdateExpression='ADD #count :incr',
        ExpressionAttributeNames={'#count': 'count'},
        ExpressionAttributeValues={':incr': 1},
        ReturnValues='UPDATED_NEW'
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': 'https://uchennaokoronkwo.com',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        },
        'body': json.dumps({'count': int(response['Attributes']['count'])})
    }


