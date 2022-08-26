import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
connect_str = "DefaultEndpointsProtocol=https;AccountName=fileuploadapp;AccountKey=WS67VJmAU08o5hGW0a6WYYtuVfYGiKvIMxUwz09oCYi/pwSA4Oi1UvQi3zRLJ4Rm5OghZ84D2QtQ+AStw5oucg==;EndpointSuffix=core.windows.net"# os.getenv('AZURE_STORAGE_CONNECTION_STRING')


# Create the BlobServiceClient object which will be used to create a container client


blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Create a unique name for the container https://fileuploadapp.blob.core.windows.net/tutorial-container/sdfadfas.png
container_name = "tutorial-container"

# Create the container
# container_client = blob_service_client.create_container(container_name)
# container_client = blob_service_client.get_blob_client(container_name)
def upload_img(imgpath):
    file_name = str(uuid.uuid4())+".jpg"
    # file_name = imgpath.split("/")[-1]
    print(file_name)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + file_name)

    
    with open(imgpath, "rb") as data:
        blob_client.upload_blob(data)
    resLink = "https://fileuploadapp.blob.core.windows.net/tutorial-container/"+file_name
    return resLink

# print(upload_img("/home/sih/reading/demo.jpg"))