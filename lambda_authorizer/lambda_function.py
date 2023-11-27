import os
from base64 import b64decode

import boto3

dynamodb_client = boto3.client("dynamodb")
DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_USERS_TABLE_NAME")


def get_user(username):
    response = dynamodb_client.get_item(
        TableName=DYNAMODB_TABLE_NAME, Key={"username": {"S": username}}
    )
    return response["Item"] if "Item" in response else None


def lambda_handler(event, context):
    bearer_token = event["headers"]["authorization"][7:]
    decode_token = b64decode(bearer_token)
    username, password = decode_token.decode("utf-8").split(":")
    user = get_user(username)
    if user:
        if user["password"]["S"] != password:
            return {"isAuthorized": False}
        return {"isAuthorized": True}
    return {"isAuthorized": False}
