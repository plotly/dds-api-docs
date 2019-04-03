import gql
import requests
from dds_client import dds_endpoint

thumbnail_file_name = "thumbnail.png"
thumbnail_content = open(thumbnail_file_name, "r")
app_name = "test-app"

mutation = gql(
    """
    mutation ($thumbnail: Upload!){
        uploadAppThumbnail(thumbnail: $thumbnail: , appname: {app_name}) {
            app {
                thumbnailUrl
            }
            error
        }
    }
    """
)
variables = {"thumbnail": "thumbnail.png"}

operations = {"query": mutation, "variables": variables}

file_map = {0: [thumbnail_file_name]}

data = {"operations": operations, "map": file_map}

files = {0: thumbnail_content}

result = request.post(dds_endpoint, files=files, data=data)["data"]

print(f"new thumbnail url: {result['app']['thumbnailUrl']}")
print(f"error: {result['error']}")
