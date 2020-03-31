import holder
import engine
import logging.config
import logging as log
import config
import os
import pathlib
from utils.Exceptions import AWSBucketEmpty, AWSIdEmpty, AWSSecretEmpty, StudentFileIsNotFound, ParquetFileIsNotFound

"""
This module is for starting the application. 
Added logging module to display the logs in proper format.
Added custom error handling messages

Raises:
    AWSBucketEmpty: If AWS bucket is empty
    AWSIdEmpty: If AWS Id is empty
    AWSSecretEmpty: IF AWS Secret is empty
    StudentFileIsNotFound: If Student file is not found
    ParquetFileIsNotFound: If parquet file is not found
"""
if __name__=="__main__":
    try:
        logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
        aws_bucket = os.getenv("AWS_BUCKET",config.aws_bucket)
        if not aws_bucket:
            raise AWSBucketEmpty
        expiration_mins = int(os.getenv("AWS_URL_EXP_MIN",config.aws_url_exp_min))
        aws_id = os.getenv("AWS_ID",config.aws_id)
        if not aws_id:
            raise AWSIdEmpty
        aws_sec = os.getenv("AWS_SECRET",config.aws_sec)
        if not aws_sec:
            raise AWSSecretEmpty
        file = pathlib.Path("data/students.csv")
        if not file.exists():
            raise StudentFileIsNotFound
        file = pathlib.Path("data/teachers.parquet")
        if not file.exists():
            raise ParquetFileIsNotFound
        holder.setS3(aws_id, aws_sec, aws_bucket,60*expiration_mins)
        engine.runme()
    except AWSBucketEmpty as E:
        log.error("----> AWS Bucket Name is Empty - Need to enter AWS_BUCKET name")
    except AWSIdEmpty as E:
        log.error("----> AWS Id is Empty - Need to enter AWS_ID name")
    except AWSSecretEmpty as E:
        log.error("----> AWS Secret is Empty - Need to enter AWS_SECRET name")
    except StudentFileIsNotFound as E:
        log.error("----> Student CSV file is not found - Need to uplaod that file")
    except ParquetFileIsNotFound as E:
        log.error("----> Parquet file is not found - Need to uplaod that file")
    except Exception as E:
        log.error("----> failed to start service with error ---->")
        log.exception(E)
