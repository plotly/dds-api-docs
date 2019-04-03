import gql
import dds_client

page = 2

apps_page_query = gql(
    """
    {
      apps(page: {page}) {
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

result = dds_client.execute(apps_page_query)

print(f"next page: {result.nextPage}")
print(f"app url on server: {result.apps[0].urlOnServer}")
print(f"app show in portal: {result.apps[0].metadata.showInPortal}")
