from gql import gql
from dds import client as dds_client

unmount_directory_mutation = gql(
    """
    mutation {
        unmountDirectory(targetDir: "target", hostDir: "host", appname: "test-app") {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(unmount_directory_mutation)["unmountDirectory"]

print(f"success: {result['ok']}")
print(f"error: {result['error']}")
