from gql import gql
import dds_client

apps_page_query = gql(
    """
    {
        apps(page: 2) {
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

result = dds_client.execute(apps_page_query)["apps"]

print(f"next page: {result['nextPage']}")
print(f"app url on server: {result['apps'][0]['urlOnServer']}")
print(f"app show in portal: {result['apps'][0]['metadata']['showInPortal']}")
