# -*- coding: utf-8 -*-
import json
import boto3

client = boto3.client('connect')


def lambda_handler(event, context):
    info = '<speak><break time="3s"/>请注意' + event+'</speak>'
    print(event)
    response = client.start_outbound_voice_contact(
        DestinationPhoneNumber='+8613720200502',
        InstanceId='06d82dff-b50f-4ae8-8987-c7d8704dfe9b',
        ContactFlowId='131bc124-4d5b-4970-a1e2-5202a3fab313',
        SourcePhoneNumber='+815031551939',
        Attributes={
            'message': info
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response)

    }
