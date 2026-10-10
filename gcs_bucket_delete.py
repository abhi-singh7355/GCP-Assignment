from google.cloud import storage

def delete_bucket(bucket_name):
    """Deletes a bucket from Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()
    print(f"Bucket {bucket.name} deleted.")

if __name__ == "__main__":
    # Replace with the name of the bucket you want to delete
    delete_bucket("gcp-ai-data-abhishek-12345")