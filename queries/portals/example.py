from gql import gql
from dds import client as dds_client

name = "DEFAULT"

portals_name_query = gql(
    """
    query PortalQuery ($name: String!){
        portals(name: $name) {
            portals {
                name
                logoUrl
            }
        }
    }
    """
)

result = dds_client.execute(portals_name_query, {"name": name})["portals"]

print(f"portal name: {result['portals'][0]['name']}")
print(f"portal logo URL: {result['portals'][0]['logoUrl']}")
