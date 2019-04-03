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

print("success: {result.ok}")
print("error: {result.error}")
