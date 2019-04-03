from gql import gql
from dds import client as dds_client

mount_directory_mutation = gql(
    """
    mutation {
        mountDirectory(targetDir: "target", hostDir: "host", appname: "test-app") {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(mount_directory_mutation)["mountDirectory"]

print(f"success: {result['ok']}")
print(f"error: {result['error']}")
