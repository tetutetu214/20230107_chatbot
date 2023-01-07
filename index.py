import boto3
import os

from dingtalk import DingTalk
from alarm import Alarm

secretArn = os.environ['SECRET_ARN']

# Get chat bot URL includes token from Secrets Manager
secret_manager_client = boto3.client('secretsmanager')
get_secret_value_response = secret_manager_client.get_secret_value(
        SecretId=secretArn
    )
secretURL = get_secret_value_response['SecretString']

# Initial DingTalk handler
dingtalk=DingTalk(secretURL)

def lambda_handler(event, context):
    msg = "【テスト】AWS CostExplorer"
    print(msg)

    dtAlarm = Alarm(

        description=msg,
    )

    dingtalk.send_text_msg(dtAlarm)

    response = {
        "statusCode": 200,
        "body": "Message Sent."
    }

    return response
