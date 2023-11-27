from lambda_helper.helper import APIGatewayDemo


def lambda_handler(event, context):
    try:
        api_demo = APIGatewayDemo()
        repos = api_demo.get_formatted_repos()
        formatted_data = api_demo.format_data_for_dynamodb(repos)
        api_demo.write_to_dynamodb(formatted_data)
        api_demo.close_connection()
        return {"message": "successfully written to dynamodb"}
    except Exception as e:
        return {"message": "something bad happened"}
