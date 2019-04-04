import json
import requests
from dds import DDS_ENDPOINT

thumbnail_file_name = "thumbnail.png"
thumbnail_content = open(thumbnail_file_name, "rb")

mutation = """
mutation ($thumbnail: Upload!){
    uploadAppThumbnail(thumbnail: $thumbnail, appname: "test-app") {
        app {
            thumbnailUrl
        }
        error
    }
}
"""

operations = json.dumps(
    {"query": mutation, "variables": {"thumbnail": "thumbnail.png"}}
)

data = {
    "operations": operations,
    "map": '{"0":["variables.logo"]}',
    "0": thumbnail_file_name,
}

files = {"0": thumbnail_content}

result = requests.post(DDS_ENDPOINT, data=data, files=files)

result = json.loads(result.text)
result = result["data"]["uploadAppThumbnail"]

print(f"new thumbnail url: {result['app']['thumbnailUrl']}")
print(f"error: {result['error']}")
