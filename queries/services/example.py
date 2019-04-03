from gql import gql
import dds_client

services_query = gql(
    """
    {
        services {
            name
            serviceType
            created
        }
    }
    """
)

result = dds_client.execute(services_query)["services"]

print(f"first services name: {result[0]['name']}")
