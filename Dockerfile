FROM python:3.6-stretch
RUN mkdir /app
EXPOSE 8080
ADD . /app
WORKDIR /app
ENV AWS_BUCKET = 
ENV AWS_ID =
ENV AWS_SECRET =
RUN pip install -r requirements.txt
# expose the port for the API
# run and start anomaly detection service.
CMD [ "python", "startService.py" ]
