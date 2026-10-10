from google.cloud import storage

def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""

    storage_client = storage.Client()

    blobs = storage_client.list_blobs(bucket_name)

    blob_names = []

    for blob in blobs:
        print(blob.name)
        blob_names.append(blob.name)

    return blob_names


if __name__ == '__main__':
    val = list_blobs('gcp-aiml-data-2026')
    print(val)


    
