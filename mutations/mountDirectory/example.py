from gql import gql
import dds_client

target_dir = "target"
host_dir = "host"
app_name = "test-app"

mount_directory_mutation = gql(
    """
    mutation {
        mountDirectory(targetDir: {target_dir}, hostDir: {host_dir}, appname: {app_name}) {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(mount_directory_mutation)["mountDirectory"]

print(f"success: {result['ok']}")
print(f"error: {result['error']}")
