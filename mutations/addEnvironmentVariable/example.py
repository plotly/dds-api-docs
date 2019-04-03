from gql import gql
import dds_client

add_environment_variable_mutation = gql(
    """
    mutation {
        addEnvironmentVariable(
            name: "test-env-var",
            value: "value",
            appname: "test-app"
        ){
            ok
            error
        }
    }
    """
)

result = dds_client.execute(add_environment_variable_mutation)["addEnvironmentVariable"]

print(f"ok: {result['ok']}")
print(f"error: {result['error']}")
