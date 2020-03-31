import logging as log
import boto3
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError

class S3_connect:
    """
    Creates AWS S3 connection and upload the file into AWS s3 bucket

    Methods
    -------
    __create_s3_session - It creates s3 session
    upload_to_aws - Upload file into s3
    """
    def __init__(self, aws_id, aws_sec, aws_bucket, expiration_time):
        self.aws_id = aws_id
        self.aws_sec = aws_sec
        self.bucket = aws_bucket
        self.S3 = None
        self.s3client = None
        self.__create_s3_session()
        self.expiration = expiration_time

    def __create_s3_session(self):
        """
        Creates s3 session and s3 client
        """
        self.session = boto3.Session(aws_access_key_id=self.aws_id, aws_secret_access_key=self.aws_sec)
        self.s3client = self.session.client("s3")

    def upload_to_aws(self, local_file, bucket, s3_file):
        """
        Upload the file into aws s3 bucket
        """
        try:
            self.s3_client.upload_file(local_file, bucket, s3_file)
            print("Upload Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False
