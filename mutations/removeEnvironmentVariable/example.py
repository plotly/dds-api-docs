from gql import gql
import dds_client

remove_environment_variable_mutation = gql(
    """
    mutation {
        removeEnvironmentVariable(appname: "test-env-var", name: "test-app"){
            ok
            error
        }
    }
    """
)

result = dds_client.execute(remove_environment_variable_mutation)[
    "removeEnvironmentVariable"
]

print(f"ok: {result['ok']}")
print(f"error: {result['error']}")
