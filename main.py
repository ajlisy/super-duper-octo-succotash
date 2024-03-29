import os, time
from influxdb_client_3 import InfluxDBClient3, Point

token = os.environ.get("INFLUXDB_TOKEN")
org = "alisy@alum.mit.edu"
host = "https://us-west-2-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(host=host, token=token, org=org)
