import requests
from gql import gql
from dds import DDS_ENDPOINT

thumbnail_file_name = "thumbnail.png"
thumbnail_content = open(thumbnail_file_name, "r")

mutation = gql(
    """
    mutation ($thumbnail: Upload!){
        uploadAppThumbnail(thumbnail: $thumbnail: , appname: "test-app") {
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

result = requests.post(DDS_ENDPOINT, files=files, data=data)["data"]

print(f"new thumbnail url: {result['app']['thumbnailUrl']}")
print(f"error: {result['error']}")
