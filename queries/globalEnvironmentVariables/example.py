import gql
import dds_client

global_environment_variables_query = gql(
    """
    {
        globalEnvironmentVariables {
            name
            value
            readonly
        }
    }
    """
)

result = dds_client.execute(global_environment_variables_query)

print("first environment variable name: {result[0].name}")
