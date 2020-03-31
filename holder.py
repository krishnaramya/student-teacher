from connectors.s3Connector import S3_connect

s3_connector = None

def setS3(aws_id, aws_sec,aws_bucket,expiration_time):
	"""
	creates the aws s3 connector object

	Parameters:
		aws_id (str): AWS Id
		aws_sec (str)" AWS Secret
		aws_bucket (str): AWS bucket name
		expiration_time (int): Expired mins
	"""
	global s3_connector
	s3_connector = S3_connect(aws_id, aws_sec, aws_bucket,expiration_time)

def getS3():
	"""
	get the aws s3 connection object

	Return:
		S3 Object: It returns aws s3 connection object
	"""
	global s3_connector
	return s3_connector

def filewrite(data):
	"""
		write content to file
	"""
	with open('student-teachers.json', 'a') as f:
		f.write(data.to_json(orient='records', lines=True))
