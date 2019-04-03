import gql
import dds_client

name = "test-app"

delete_app_mutation = gql(
    """
    mutation {
        deleteApp(name: {name}) {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(delete_app_mutation)

print(f"success: {result.ok}")
print(f"error: {result.error}")
