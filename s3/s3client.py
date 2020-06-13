import boto3

# REF: https://github.com/ronaldddilley/ceph-s3-examples
# For ssl see: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html
#

#endpointurl = "overcloud.localdomain:13808"
endpoint_url = "https://10.94.73.112:13808"
secret_key="iJVRhkNovlqT5seTuVpmiaQXHoJPFxu4I32s6jBl"
access_key="RK39AL9BKJGD2H3ZAWTV"

session = boto3.session.Session()
s3_client = session.client(
    service_name='s3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    endpoint_url=endpoint_url)

print s3_client


endpoint_url = "https://overcloud.localdomain:13808"
# from https://github.com/ronaldddilley/ceph-s3-examples/blob/master/ceph-create-bucket.py
s3 = boto3.resource('s3',
                    endpoint_url=endpoint_url,
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key,
                    verify=False)  # no ssl certificates
# or verify="path/to/cert/bundle.pem"

bucket = s3.Bucket("gideon_buck2")
bucket.create()

scon = boto3.client('s3',
                    endpoint_url=endpoint_url,
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key,
                    verify=False)  # no ssl certificates
response = scon.list_buckets()
for item in response['Buckets']:
    print(item['CreationDate'], item['Name'])




