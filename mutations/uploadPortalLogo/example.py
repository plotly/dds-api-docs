import requests
from gql import gql
from dds_client import dds_endpoint

logo_file_name = "logo.png"
logo_content = open(logo_file_name, "r")

mutation = gql(
    """
    mutation ($logo: Upload!){
        uploadPortalLogo(logo: $logo: , portalname: "DEFAULT") {
            portal {
                logoUrl
            }
            error
        }
    }
    """
)
variables = {"logo": logo_file_name}

operations = {"query": mutation, "variables": variables}

file_map = {0: [logo_file_name]}

data = {"operations": operations, "map": file_map}

files = {0: logo_content}

result = requests.post(dds_endpoint, files=files, data=data).data

print(f"new logo url: {result['app']['logoUrl']}")
print(f"error: {result['error']}")
