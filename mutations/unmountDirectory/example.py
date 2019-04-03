import gql
import dds_client

target_dir = "target"
host_dir = "host"
app_name = "test-app"

unmount_directory_mutation = gql(
    """
    mutation {
        unmountDirectory(targetDir: {target_dir}, hostDir: {host_dir}, appname: {app_name}) {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(unmount_directory_mutation)

print(f"success: {result.ok}")
print(f"error: {result.error}")
