from gql import gql
from dds import client as dds_client

name = "test-app"

# Set allApps to True if you have set an admin user in dds.py and you would like to query from all apps on DDS
# and not just apps you created.
allApps = False

apps_name_query = gql(
    """
    query Apps($name: String!, $allApps: Boolean!) {
        apps(name: $name, allApps: $allApps) {
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

result = dds_client.execute(apps_name_query, {"name": name, "allApps": allApps})["apps"]

print(f"app name: {result['apps'][0]['name']}")
print(f"app status running: {result['apps'][0]['status']['running']}")
