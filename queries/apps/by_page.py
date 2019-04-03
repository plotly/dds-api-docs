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

print("next page: {result.apps.nextPage}")
print("app url on server: {result.apps.apps[0].urlOnServer}")
print("app show in portal: {result.apps.apps[0].metadata.showInPortal}")
