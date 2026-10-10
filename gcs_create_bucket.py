
from google.cloud import storage


def create_bucket_class_location(bucket_name):
    """
    Create a new bucket in the US region with the Coldline storage class.
    """

    storage_client = storage.Client()
    print("Storage Client:", storage_client)

    bucket = storage_client.bucket(bucket_name)
    print("Bucket Object:", bucket)

    bucket.storage_class = "COLDLINE"

    new_bucket = storage_client.create_bucket(
        bucket,
        location="US"
    )

    print(
        f"Created bucket {new_bucket.name} in "
        f"{new_bucket.location} with storage class "
        f"{new_bucket.storage_class}"
    )

    return new_bucket


# Function call
val = create_bucket_class_location("gcp-ai-data-abhishek-12345")
print("-" * 15)
print(val)