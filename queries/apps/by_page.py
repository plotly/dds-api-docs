from gql import gql
from dds import client as dds_client

apps_page_query = gql(
    """
    query AppsQuery ($page: Int!) {
        apps(page: $page) {
            apps {
                urlOnServer
                metadata {
                    showInPortal
                }
            }
            nextPage
        }
    }
    """
)

page = 2

result = dds_client.execute(apps_page_query, {"page": page})["apps"]

print(f"next page: {result['nextPage']}")
print(f"app url on server: {result['apps'][0]['urlOnServer']}")
print(f"app show in portal: {result['apps'][0]['metadata']['showInPortal']}")

nextPage = result["nextPage"]

third_page = dds_client.execute(apps_page_query, {"page": nextPage})["apps"]
