from utils.DataProcessor import DataProcessor
from utils.FileReaders import Reader
import os
import holder

def runme():
    """
    set the students and teachers file and calls the readers for loadings each file.
    """
    student_file = os.getcwd() + '/data/students.csv'
    reader_obj = Reader()
    student_data = reader_obj.file_reader(student_file)

    par_file = os.getcwd() + '/data/teachers.parquet'
    data_process_obj = DataProcessor(student_data, par_file)
    data_process_obj.processData()
    json_file = os.getcwd() + 'student-teachers.json'

    s3_connect = holder.getS3()
    s3_connect.upload_to_aws(json_file, 'data', 'student-teachers.json')
