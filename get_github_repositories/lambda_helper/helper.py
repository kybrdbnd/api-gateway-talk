import logging
import os

import boto3

logger = logging.getLogger()

DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")

dynamodb_client = boto3.client("dynamodb")


class APIGatewayDemo:
    def __init__(self):
        pass

    def get_github_repos_from_db(self):
        logger.info("fetching data from dynamoDB")
        response = dynamodb_client.scan(
            TableName=DYNAMODB_TABLE_NAME,
            Limit=100,
            Select="SPECIFIC_ATTRIBUTES",
            ProjectionExpression="id,#n",
            ExpressionAttributeNames={"#n": "name"}
        )
        return response

    def get_formatted_repos_from_db(self):
        logger.info("formatting data from dynamoDB")
        return [
            {"id": item["id"]["N"], "name": item["name"]["S"]}
            for item in self.get_github_repos_from_db()["Items"]
        ]
