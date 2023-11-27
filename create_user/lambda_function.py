import json
import logging
import os

import boto3

dynamodb_client = boto3.client("dynamodb")
DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_USERS_TABLE_NAME")
logger = logging.getLogger()


def create_user(username, password):
    try:
        item = {
            "username": {"S": username},
            "password": {"S": password},
        }
        dynamodb_client.put_item(TableName=DYNAMODB_TABLE_NAME, Item=item)
        logger.info("User created successfully")
    except Exception as err:
        print(err)
        raise err


def lambda_handler(event, context):
    headers = event["headers"]
    auth_token = headers.get("authorization", None)
    if auth_token is None:
        return {
            "statusCode": 401,
            "body": json.dumps({"message": "Unauthorized"}),
        }
    bearer_token = auth_token[7:]
    if bearer_token == "pranavpuri":
        body = event.get("body")
        if body is None:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Bad Request"}),
            }
        else:
            body = json.loads(body)
            username = body.get("username")
            if username is None:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"message": "Bad Request"}),
                }
            password = body.get("password")
            if password is None:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"message": "Bad Request"}),
                }
            create_user(username, password)
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "user created successfully"}),
        }
    else:
        return {
            "statusCode": 401,
            "body": json.dumps({"message": "Unauthorized"}),
        }
