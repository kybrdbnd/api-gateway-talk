import os

import boto3

dynamodb_client = boto3.client("dynamodb")

DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")


def get_github_repo(repo_id: int) -> dict:
    response = dynamodb_client.get_item(
        TableName=DYNAMODB_TABLE_NAME, Key={"id": {"N": repo_id}}
    )
    return response["Item"] if "Item" in response else None


def lambda_handler(event, context):
    path_params = event["pathParameters"]
    repo_id = path_params.get("id", None)
    repo = get_github_repo(repo_id)
    if repo_id is None:
        return {"message": "repo id is required"}
    if repo:
        return {
            "id": repo["id"]["N"],
            "name": repo["name"]["S"],
            "description": repo["description"]["S"],
            "archived": repo["archived"]["BOOL"],
            "created_at": repo["created_at"]["S"],
            "stars": repo["stars"]["N"],
            "updated_at": repo["updated_at"]["S"],
        }
    else:
        return {"message": "repo not found"}
