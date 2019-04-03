import gql
import requests
from dds_client import dds_endpoint

logo_file_name = "logo.png"
logo_content = open(logo_file_name, "r")
portal_name = "DEFAULT"

mutation = gql(
    """
    mutation ($logo: Upload!){
        uploadPortalLogo(logo: $logo: , portalname: {portal_name}) {
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

result = request.post(dds_endpoint, files=files, data=data).data

print(f"new logo url: {result['app']['logoUrl']}")
print(f"error: {result['error']}")
