#!/usr/bin/python3

import boto3

BUCKET = '20210308-polly-notes-web'
KEY = 'index.html'

s3 = boto3.client('s3')
presigned_url = s3.generate_presigned_url(
    ClientMethod = 'get_object',
    Params = {'Bucket' : BUCKET, 'Key' : KEY},
    ExpiresIn = 900,
    HttpMethod = 'GET'
)

print(presigned_url)

