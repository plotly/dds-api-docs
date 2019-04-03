import gql
import dds_client

name = "test-env-var"
value = "value"
app_name = "test-app"

add_environment_variable_mutation = gql(
    """
    mutation {
        addEnvironmentVariable(name: {name}, value: {value}, appname: {app_name}){
            ok
            error
        }
    }
    """
)

result = dds_client.execute(add_environment_variable_mutation)["addEnvironmentVariable"]

print(f"ok: {result['ok']}")
print(f"error: {result['error']}")
