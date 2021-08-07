import boto3
from botocore.exceptions import ClientError
import time
import sys

"""
echo aws dynamodb create-table \
            --region us-east-1 \
            --table-name tf-lock-$1-$2-$site\
            --attribute-definitions \
            AttributeName=LockID,AttributeType=S \
            --key-schema AttributeName=LockID,KeyType=HASH \
            --billing-mode PAY_PER_REQUEST
"""

def create_table(aws_region=None, table_name=None):
    if aws_region and table_name:
        print(aws_region)
        print(table_name)
        try:
            client = boto3.client('dynamodb', region_name=aws_region)
            response = client.create_table(
                TableName=table_name,
                KeySchema=[
                    {
                        'AttributeName': 'LockID',
                        'KeyType': 'HASH'  # Partition key
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'LockID',
                        'AttributeType': 'S'
                    }
                ],
                BillingMode='PAY_PER_REQUEST',
                Tags=[
                {
                    'Key': 'Organization',
                    'Value': 'SRE'
                },
                {
                    'Key': 'Purpose',
                    'Value': 'tf-state'
                },
                {
                    'Key': 'Environment',
                    'Value': 'lab'
                }
            ]
            )
            print(response)
            response.wait_until_exists()
            return response
        except ClientError as e:
            sys.exc_info()
            raise(e.response)
        

# def check_table_creation(table=None):
#     if table:
#         sleep_counter = 100
#         while table["TableDescription"]["TableStatus"] != "ACTIVE":
#             if sleep_counter > 1:
#                 time.sleep(10)
#                 print(f"{sleep_counter} iteration of sleeping for 10 seconds")
#                 sleep_counter = sleep_counter - 1
#             else:
#                 print(f"sleep counter has expired. Current sleep counter is: {sleep_counter}.\n Check AWS Console for Dynamo table creation")
#             return False
#         return True


def check_table_exists(aws_region = None, table=None):
    if aws_region and table:
        try:
            client = boto3.client('dynamodb', region_name=aws_region)
            response = client.describe_table(TableName=table)
            if response:
                return True
        except:
            return False


if __name__ == '__main__':
    aws_region = 'us-east-1'
    table = 'tf-networking'
    if not check_table_exists(aws_region, table):
        out = create_table(aws_region, table)
        print(f"out: {out}")
        # if out:
        #     check_table_creation(out)
        # else:
        #     sys.exit
    else:
        print(f"{table} already exists in {aws_region}")
    
    

