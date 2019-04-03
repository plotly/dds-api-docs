import gql
import dds_client

name = "test-app"

apps_name_query = gql(
    """
    {
        apps(name: {name}) {
            apps {
                name
                status {
                    running
                }
            }
        }
    }
    """
)

result = dds_client.execute(apps_name_query)["apps"]

print(f"app name: {result['apps'][0]['name']}")
print(f"app status running: {result['apps'][0]['status'].running}")
