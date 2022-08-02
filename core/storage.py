import os
import boto3
import botocore
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

class S3CloudManager:

    def __init__(self, bucket):
        self.bucket_name = bucket
        boto3.set_stream_logger(name='botocore')  # this enables debug tracing
        session = boto3.session.Session()
        self.s3_client = session.client(
            service_name='s3',
            aws_access_key_id=os.getenv('ACCESS_KEY'),
            aws_secret_access_key=os.getenv('ACCESS_SECRET'),
            endpoint_url=os.getenv('ENDPOINT_URL'),
            config=botocore.client.Config(signature_version='s3'),
        )

    def upload(self, file_name, object_name=None):
        if object_name is None:
            object_name = os.path.basename(file_name)
        try:
            response = self.s3_client.upload_file(file_name, self.bucket_name, object_name)
        except ClientError as e:
            print("deu ruim")
            return False
        print("deu bom")
        return True
        
    def delete(self, filename):
        return 0
    def get_file(self, filename):
        return 0
    def get_json(self, filename):
        return 0
    def get_blob(self, filename):
        return 0