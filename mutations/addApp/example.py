import gql
import dds_client

name = "test-app"

add_app_mutation = gql(
    """
    mutation {
        addApp(name: {name}) {
            app {
                name
            }
            error
        }
    }
    """
)

result = dds_client.execute(add_app_mutation)

print("new app name: {result.app.name}")
print("error: {result.error}")
