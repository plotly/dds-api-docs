import os
import json
import requests
from dds import DDS_ENDPOINT

logo_file_name = "logo.png"
logo_location = os.path.join(
    os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))),
    logo_file_name,
)
logo_content = open(logo_location, "rb")

mutation = """
mutation($logo: Upload!){
    uploadPortalLogo(logo: $logo, portalname: "default") {
        portal {
            logoUrl
        }
        error
    }
}
"""

variables = {"logo": logo_file_name, "portalname": "default"}

operations = json.dumps({"query": mutation, "variables": {"portalname": "default"}})

data = {
    "operations": operations,
    "map": '{"0":["variables.logo"]}',
    "0": logo_file_name,
}

files = {"0": logo_content}

result = requests.post(DDS_ENDPOINT, data=data, files=files)

result = json.loads(result.text)
result = result["data"]["uploadPortalLogo"]

print(f"new logo url: {result['portal']['logoUrl']}")
print(f"error: {result['error']}")
