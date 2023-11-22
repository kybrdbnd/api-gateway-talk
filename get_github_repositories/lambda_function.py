from lambda_helper.helper import APIGatewayDemo


def lambda_handler(event, context):
    api_demo = APIGatewayDemo()
    repos = api_demo.get_formatted_repos_from_db()
    return repos
