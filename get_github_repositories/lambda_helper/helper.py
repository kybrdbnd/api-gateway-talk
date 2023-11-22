import os
import boto3

DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")

dynamodb_client = boto3.client("dynamodb")


class APIGatewayDemo:
    def __init__(self):
        pass

    def get_github_repos_from_db(self):
        response = dynamodb_client.scan(
            TableName=DYNAMODB_TABLE_NAME, Limit=100, Select="ALL_ATTRIBUTES"
        )
        return response

    def get_formatted_repos_from_db(self):
        return [
            {
                "id": item["id"]["N"],
                "name": item["name"]["S"],
                "description": item["description"]["S"],
                "archived": item["archived"]["BOOL"],
                "created_at": item["created_at"]["S"],
                "stars": item["stars"]["N"],
                "updated_at": item["updated_at"]["S"],
            }
            for item in self.get_github_repos_from_db()["Items"]
        ]