import pandas as pd
from pyarrow.parquet import ParquetFile
import os

class Reader():
    """
    A class is used for Reading the files and convert the files into DataFrames using generators

    Attributes
    ----------
    chunksize : int
         Used to return the data in chunks.

    Methods
    -------
    file_reader(filename)
        Read a csv file and convert to pandas data frame with chunks

    parquet_reader(filename)
        Read a parque file and convert to ParquetFile Object

    get_parquet_date(parquetData)
        Convert Parque object into data frame
    """

    chunksize = 10
        
    def file_reader(self, filename):
        """
        To load the data from csv file and convert into dataframe as chunks and return generator object value.
  
        Parameters:
            filename (str): The student file name

        Returns:
            chunk (obj): The generator Object
        """

        for chunk in pd.read_csv(filename, chunksize = Reader.chunksize,delimiter='_'):        
            yield chunk

    def parquet_reader(filename):
        """
        Reader interface for a single Parquet file

        Parameters:
            filename (str): The teacher parquet file name

        Returns:
            parque (obj): ParquetFile object
        """

        return ParquetFile(source = filename)

    def get_parquet_data(parquet_data):
        """
        Convert parquet file object into dataframe and returns the generator object value

        Parameters:
            parquet_data (obj): ParquetFile object

        Returns:
            res (obj): The generator Object
        """
        rows = parquet_data.num_row_groups
        cols = ['fname', 'lname', 'email', 'cid']
        for row in range(0, rows):
            row_df = parquet_data.read_row_group(row)            
            res = row_df.to_pandas()[cols];
            res.rename(columns = {'fname': 'teacherfirstname', 'lname': 'teacherlastname', 'email':'teacheremail', 'cid':'tcid'}, inplace=True)
            yield res
