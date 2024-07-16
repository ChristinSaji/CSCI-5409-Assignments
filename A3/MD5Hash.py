import json
import hashlib
import requests

def lambda_handler(event, context):
    value = event['value']
    banner = "B00977669"
    url = event['course_uri']
    
    value_encoded = value.encode('utf-8')
    md5_hash = hashlib.md5(value_encoded)
    hashed_value = md5_hash.hexdigest()
    
    payload = {
        'banner': banner,
        'result': hashed_value,
        'arn': context.invoked_function_arn,
        'action': 'md5',
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
