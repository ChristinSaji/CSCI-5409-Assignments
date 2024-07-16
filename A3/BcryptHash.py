import json
import bcrypt
import requests

def lambda_handler(event, context):
    value = event['value']
    banner = "B00977669"
    url = event['course_uri']
    
    value_encoded = value.encode('utf-8')
    bcrypt_salt = bcrypt.gensalt(12, prefix=b'2b')
    hashed_value_bytes = bcrypt.hashpw(value_encoded, bcrypt_salt)
    hashed_value = hashed_value_bytes.decode('utf-8')
    
    payload = {
        'banner': banner,
        'result': hashed_value,
        'arn': context.invoked_function_arn,
        'action': 'bcrypt',
        'value': value
    }
    
    response = requests.post(url, json=payload)
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': hashed_value,
            'response': response.text
        })
    }
