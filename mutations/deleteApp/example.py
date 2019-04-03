from gql import gql
from dds import client as dds_client

delete_app_mutation = gql(
    """
    mutation {
        deleteApp(name: "test-app") {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(delete_app_mutation)["deleteApp"]

print(f"success: {result['ok']}")
print(f"error: {result['error']}")
