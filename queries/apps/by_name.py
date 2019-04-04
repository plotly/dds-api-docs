from gql import gql
from dds import client as dds_client

name = "test-app"

apps_name_query = gql(
    """
    query Apps($name: String!) {
        apps(name: $name) {
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

result = dds_client.execute(apps_name_query, {"name": name})["apps"]

print(f"app name: {result['apps'][0]['name']}")
print(f"app status running: {result['apps'][0]['status']['running']}")
