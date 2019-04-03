from gql import gql
from dds import client as dds_client

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

result = dds_client.execute(global_environment_variables_query)[
    "globalEnvironmentVariables"
]

print(f"first environment variable name: {result[0]['name']}")
