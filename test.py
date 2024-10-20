import boto3
from django.conf import settings
import environ

env = environ.Env()
environ.Env.read_env()

# Create a test file to upload
with open('test.txt', 'w') as f:
    f.write('This is a test file')

# Upload using boto3
s3 = boto3.client(
    's3',
    aws_access_key_id= env('MINIO_ACCESS_KEY'),
    aws_secret_access_key=env('MINIO_SECRET_KEY'),
    endpoint_url=env('MINIO_ENDPOINT_URL')
)

s3.upload_file('test.txt', env('MINIO_BUCKET_NAME'), 'test.txt')

print('File uploaded successfully')