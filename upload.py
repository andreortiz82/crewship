import os
import boto3
from botocore.exceptions import NoCredentialsError
import concurrent.futures
import mimetypes

def upload_to_s3(file_name, bucket, object_name=None):
    """
    Upload a file to an S3 bucket and return the public URL of the file.

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then use file_name
    :return: URL of the uploaded file if successful, else None
    """
    # Create an S3 client
    s3_client = boto3.client('s3')
    if object_name is None:
        object_name = file_name
   
    file_type, encoding = mimetypes.guess_type(file_name)
    if file_type is None:
        file_type = 'application/octet-stream'  # Default to binary stream if content type cannot be guessed


    try:
        # Upload the file with public-read ACL
        s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ACL': 'public-read', 'ContentType': file_type})

        # Generate the URL
        location = s3_client.get_bucket_location(Bucket=bucket)['LocationConstraint']
        if location:
            url = f"https://{bucket}.s3-{location}.amazonaws.com/{object_name}"
        else:
            url = f"https://{bucket}.s3.amazonaws.com/{object_name}"
        
        print(f"Uploaded: {url}")
        return url
    except NoCredentialsError:
        print("Credentials not available")
        return None
    except Exception as e:
        print(f"Failed to upload {object_name}: {str(e)}")
        return None

# def upload_to_s3(file_name, bucket, object_name=None):
#     """
#     Upload a file to an S3 bucket

#     :param file_name: File to upload
#     :param bucket: Bucket to upload to
#     :param object_name: S3 object name. If not specified then file_name is used
#     :return: True if file was uploaded, else False
#     """
#     # If S3 object_name was not specified, use file_name
#     if object_name is None:
#         object_name = file_name

#     # Create an S3 client
#     s3_client = boto3.client('s3')

#     try:
#         # Upload the file
#         response = s3_client.upload_file(file_name, bucket, object_name)
#     except NoCredentialsError:
#         print("Credentials not available")
#         return False
#     return True

def upload_directory_to_s3(local_directory, bucket, s3_folder):
    """
    Uploads a directory to an S3 bucket, maintaining directory structure.

    :param local_directory: Path to the local directory to upload
    :param bucket: S3 bucket name
    :param s3_folder: S3 folder path to store the files
    """
    # Create a list of all files in the directory tree
    files = []
    for root, dirs, filenames in os.walk(local_directory):
        for filename in filenames:
            local_path = os.path.join(root, filename)
            relative_path = os.path.relpath(local_path, local_directory)
            s3_path = os.path.join(s3_folder, relative_path)
            files.append((local_path, bucket, s3_path))

    # Use ThreadPoolExecutor to upload files concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(upload_to_s3, *file) for file in files]
        concurrent.futures.wait(futures)