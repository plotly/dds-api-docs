import gql
import dds_client

add_app_mutation = gql(
    """
    mutation {
        addApp(name: "test-app") {
            app {
                name
            }
            error
        }
    }
    """
)

result = dds_client.execute(add_app_mutation)["addApp"]

print(f"new app name: {result['app']['name']}")
print(f"error: {result['error']}")
