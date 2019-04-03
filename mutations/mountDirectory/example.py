from gql import gql
import dds_client

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
