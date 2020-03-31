import holder
import pandas as pd
from pyarrow.parquet import ParquetFile
from utils.FileReaders import Reader

class DataProcessor():
    """
    A class is used for processing the students and teachers data frames
    and comparing the class id from students and teachers dataframes and saves individual record into a file.
    stores the file into aws s3

    Methods
    -------
    processData()
        iterate the students and sets teacher's current position

    lookup(studentsdf, teachersdf)
        iterate the students and teachers by comparing class id.
        copied the resultant data into a file.            
    """
    def __init__(self, student, par_file):
        """              
        Parameters:
            student (str): The student chunk data
            parquest_file (obj): parque object

        Returns:
            chunk (obj): The generator Object
        """
        self.student = student
        self.parquetObj = Reader.parquet_reader(par_file)

    def processData(self):
        """
        Iterate the students and sets teacher's data to current position
        """
        for students in self.student:            
            teacherData = Reader.get_parquet_data(self.parquetObj)
            for teachers in teacherData:
                self.lookup(students, teachers)

    def lookup(self, studentsdf, teachersdf):
        """
        Iterate the students and comparing class id for both student and  teacher's dataframe
        and stores in AWS S3 bucket
        """
        for studentIndex, studentRow in studentsdf.iterrows():
            cid = studentRow['cid']
            for teacherIndex , teacherRow in teachersdf.iterrows():
                if (cid == teacherRow['tcid']):
                    holder.filewrite(pd.concat([studentRow, teacherRow]).to_frame().T)
