from base64 import b64encode

from dotenv import load_dotenv
from lambda_function import lambda_handler

load_dotenv()

username = "johndoe"
password = "1235"

byte_string = f"{username}:{password}".encode("utf-8")

token = b64encode(byte_string).decode("utf-8")

event = {"headers": {"authorization": f"Bearer {token}"}}
result = lambda_handler(event, None)
print(result)
