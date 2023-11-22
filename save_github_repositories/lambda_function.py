from lambda_helper.helper import APIGatewayDemo


def lambda_handler(event, context):
    api_demo = APIGatewayDemo()
    repos = api_demo.get_formatted_repos()
    formatted_data = api_demo.format_data_for_dynamodb(repos)
    api_demo.write_to_dynamodb(formatted_data)
    api_demo.close_connection()
    return True
