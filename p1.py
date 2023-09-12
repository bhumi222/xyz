import boto3

def get_csv_to_s3(bucket_name,s3_key,file_name):
    s3 =boto3.client('s3')

    try:
        s3.download_file(bucket_name,s3_key,file_name)
        print("file downloaded successfully to s3")
    except Exception as e:
        print(f"An error occured : {str(e)}")

bucket_name='myawsbuc3'
file_name='data.py'
s3_key='new.py'

get_csv_to_s3(bucket_name,s3_key,file_name)
