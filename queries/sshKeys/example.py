import gql
import dds_client

ssh_keys_query = gql(
    """
    {
        sshKeys {
            keys
        }
    }
    """
)

result = dds_client.execute(ssh_keys_query)

print(f"ssh keys: {result.keys}")
