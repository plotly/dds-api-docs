import gql
import dds_client

name = "test-env-var"
value = "value"
app_name = "test-app"

add_environment_variable_mutation = gql(
    """
    {
        addEnvironmentVariable(name: {name}, value: {value}, appname: {app_name}){
            ok
            error
        }
    }
    """
)

result = dds_client.execute(add_environment_variable_mutation)

print("ok: {result.ok}")
print("error: {result.error}")
