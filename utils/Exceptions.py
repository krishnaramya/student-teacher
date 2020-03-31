class AWSBucketEmpty(Exception):
   """Raised when the AWS Bucket is empty"""
   pass

class AWSIdEmpty(Exception):
   """Raised when the AWS Id is empty"""
   pass

class AWSSecretEmpty(Exception):
   """Raised when the AWS Secret is empty"""
   pass

class StudentFileIsNotFound(Exception):
   """Raised when the Student File is not found"""
   pass

class ParquetFileIsNotFound(Exception):
   """Raised when the Parquet File is not found"""
   pass