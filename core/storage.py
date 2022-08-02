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
            service_name=os.getenv('SERVICE_NAME'),
            aws_access_key_id=os.getenv('ACCESS_KEY'),
            aws_secret_access_key=os.getenv('ACCESS_SECRET'),
            endpoint_url=os.getenv('ENDPOINT_URL'),
            config=botocore.client.Config(signature_version='s3'),
        )

    def upload(self, file_name, object_name=None):
        if object_name is None:
            object_name = os.path.basename(file_name)
        try:
            self.s3_client.upload_file(file_name, self.bucket_name, object_name)
        except ClientError as e:
            return False
        return True
        
    def delete(self, file_name):
        if file_name is None:
            return False
        else:
            try:
                self.s3_client.delete_object(Bucket=self.bucket_name, Key=file_name)
            except ClientError as e:
                return False
            return True


    def get_file(self, file_name, object_name=None):
        if object_name is None:
            object_name = os.path.basename(file_name)
            try:
                with open(file_name, 'wb') as f:
                    self.s3_client.download_fileobj(self.bucket_name, object_name, f)
            except ClientError as e:
                return False
            return True

    def get_json(self, filename):
        return 0

    def get_blob(self, filename):
        return 0