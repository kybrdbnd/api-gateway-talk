import logging
import os

import boto3
from github import Auth, Github

logger = logging.getLogger()

GITHUB_ACCESS_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")

dynamodb_client = boto3.client("dynamodb")


class GitHubAuth:
    def __init__(self):
        auth = Auth.Token(GITHUB_ACCESS_TOKEN)
        self.g = Github(auth=auth)
        logger.info("making connection to github")

    def close_connection(self):
        self.g.close()
        logger.info("closing connection to github")


class APIGatewayDemo(GitHubAuth):
    def __init__(self):
        super().__init__()

    def get_github_repos(self):
        logger.info("getting github repositories")
        return self.g.get_user().get_repos()

    def get_formatted_repos(self) -> list[dict]:
        logger.info("formatting repositories")
        return [
            {
                "name": repo.name,
                "id": str(repo.id),
                "description": repo.description if repo.description else "",
                "archived": repo.archived,
                "created_at": str(repo.created_at),
                "stars": str(repo.stargazers_count),
                "updated_at": str(repo.updated_at),
            }
            for repo in self.get_github_repos()
        ]

    def format_data_for_dynamodb(self, repos: list[dict]) -> list[dict]:
        dynamo_db_data = []
        logger.info("preparing data for dynamoDB")
        for repo in repos:
            dynamo_db_data.append(
                {
                    "name": {"S": repo["name"]},
                    "id": {"N": repo["id"]},
                    "description": {"S": repo["description"]},
                    "archived": {"BOOL": True if repo["archived"] else False},
                    "created_at": {"S": repo["created_at"]},
                    "stars": {"N": repo["stars"]},
                    "updated_at": {"S": repo["updated_at"]},
                }
            )
        return dynamo_db_data

    def write_to_dynamodb(self, repos: list[dict]):
        for item in repos:
            try:
                logger.info(f"putting repo: {item['name']}")
                dynamodb_client.put_item(TableName=DYNAMODB_TABLE_NAME, Item=item)
            except Exception as err:
                logger.error(err)
