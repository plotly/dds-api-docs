from gql import gql
from dds import client as dds_client

apps_page_query = gql(
    """
    query AppsQuery ($page: Int!, $allApps: Boolean!) {
        apps(page: $page, allApps: $allApps) {
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

# Set allApps to True if you have set an admin user in dds.py and you would like to query from all apps on DDS
# and not just apps you created.
allApps = False

result = dds_client.execute(apps_page_query, {"page": page, "allApps": allApps})["apps"]

print(f"next page: {result['nextPage']}")
print(f"app url on server: {result['apps'][0]['urlOnServer']}")
print(f"app show in portal: {result['apps'][0]['metadata']['showInPortal']}")

nextPage = result["nextPage"]

third_page = dds_client.execute(apps_page_query, {"page": nextPage, "allApps": allApps})["apps"]
