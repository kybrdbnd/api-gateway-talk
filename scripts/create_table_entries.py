import boto3

dynamodb_client = boto3.client("dynamodb")


def create_user_table_entry():
    dynamodb_client.put_item(
        TableName="users",
        Item={
            "username": {"S": "johndoe"},
            "password": {"S": "12345"},
        },
    )

    print("User table entry created successfully!")
    return True


if __name__ == "__main__":
    create_user_table_entry()
