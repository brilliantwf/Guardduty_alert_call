# -*- coding: utf-8 -*-
import json
import boto3

client = boto3.client('connect')


def lambda_handler(event, context):
    info = '<speak><break time="3s"/>请注意' + event+'</speak>'
    print(event)
    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber='+861372020XXX',
        InstanceId='06d82dff-b50f-4ae8-8987-XXXX',
        ContactFlowId='131bc124-4d5b-4970-a1e2-XXXX',
        SourcePhoneNumber='+815031551XXX',
        Attributes={
            'message': info
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response)

    }
