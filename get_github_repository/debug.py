from dotenv import load_dotenv
from lambda_function import lambda_handler

load_dotenv()

event = {
    "pathParameters": {"id": "113825403"},
}

result = lambda_handler(event, None)
print(result)
