from gql import gql
from dds import client as dds_client

ssh_keys_query = gql(
    """
    {
        sshKeys {
            keys
        }
    }
    """
)

result = dds_client.execute(ssh_keys_query)["sshKeys"]

print(f"ssh keys: {result['keys']}")
