from google.cloud import storage
import re

def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # Initialize a storage client
    storage_client = storage.Client()

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # List the blobs in the bucket
    blobs = bucket.list_blobs()

    print(f"Files in bucket {bucket_name}:")
    for blob in blobs:
        print(blob.name)



def filter_jpeg_files_direct_children(file_paths, folder_name):
    """Filters and returns paths that correspond to .jpeg files that are direct children of a specified folder."""
    # Pattern for direct children
    pattern = re.compile(rf'^{re.escape(folder_name)}/[^/]+\.jpeg$')

    filtered_paths = [path for path in file_paths if pattern.match(path)]
    return filtered_paths


def query_bigquery(query: str, big_query_client):
    query_job = big_query_client.query(query)
    return query_job.to_dataframe()


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "/local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        f"Downloaded storage object {source_blob_name} from bucket {bucket_name} to local file {destination_file_name}."
    )
