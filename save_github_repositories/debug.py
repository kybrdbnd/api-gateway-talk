from dotenv import load_dotenv
from lambda_function import lambda_handler

load_dotenv()

result = lambda_handler(None, None)
print(result)
