from gql import gql
from dds import client as dds_client

update_ssh_keys_mutation = gql(
    """
    mutation {
        updateSshKeys(keys: "key-0\nkey-1\nkey-2") {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(update_ssh_keys_mutation)["updateSshKeys"]

print(f"success: {result['ok']}")
print(f"error: {result['error']}")
