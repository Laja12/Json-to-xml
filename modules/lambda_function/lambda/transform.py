import json
import xml.etree.ElementTree as ET
import boto3
import uuid
import os  # <-- ADD THIS

def lambda_handler(event, context):
    data = json.loads(event['body'])

    root = ET.Element("root")
    for key, value in data.items():
        elem = ET.SubElement(root, key)
        elem.text = str(value)

    xml_string = ET.tostring(root, encoding='unicode')

    s3 = boto3.client('s3')
    key = f"{uuid.uuid4()}.xml"

    # ✅ Correct usage of env variable
    bucket_name = os.environ['BUCKET_NAME']

    s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=xml_string,
        ContentType='application/xml'
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'XML stored', 'key': key})
    }
