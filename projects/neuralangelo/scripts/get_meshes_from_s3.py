import boto3
import os

session = boto3.Session()

s3 = session.resource('s3')

bucket_name = 'redbuffer-quixel'
folder_key = 'RC/'

bucket = s3.Bucket(bucket_name)

for obj in bucket.objects.filter(Prefix=folder_key):
    if not os.path.exists(os.path.dirname(obj.key)):
        os.makedirs(os.path.dirname(obj.key))
    bucket.download_file(obj.key, obj.key)
