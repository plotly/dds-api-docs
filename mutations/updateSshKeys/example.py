from gql import gql
from dds import client as dds_client

update_ssh_keys_mutation = gql(
    """
    mutation UpdateSSHKeys ($keys: String!) {
        updateSshKeys(keys: $keys) {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(update_ssh_keys_mutation, {"keys": keys})["updateSshKeys"]

print(f"success: {result['ok']}")
print(f"error: {result['error']}")
