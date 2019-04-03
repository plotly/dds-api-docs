import gql
import dds_client

name = "test-env-var"
app_name = "test-app"

remove_environment_variable_mutation = gql(
    """
    mutation {
        removeEnvironmentVariable(appname: {app_name}, name: {name}){
            ok
            error
        }
    }
    """
)

result = dds_client.execute(remove_environment_variable_mutation)

print(f"ok: {result.ok}")
print(f"error: {result.error}")
