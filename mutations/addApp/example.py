import gql
import dds_client

name = "test-app"

add_app_mutation = gql(
    """
    {
        addApp(name: {name}) {
            app {
                name
                analytics {
                    resources {
                        cpuUsage
                    }
                }
                status {
                    running
                    deploying
                }
            }
            error
        }
    }
    """
)

result = dds_client.execute(add_app_mutation)

print("new app name: {result.app.name}")
print("new app cpu usage: {result.app.analytics.resources[0].cpuUsage}")
print("new app deploying: {result.app.status.deploying}")
print("error: {result.error}")
