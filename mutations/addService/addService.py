from gql import gql
from dds import client as dds_client

add_service_mutation = gql(
    """
    mutation {
        addService(serviceType: REDIS, name: "test-service") {
            service {
                name
                serviceType
                created
            }
            error
        }
    }
    """
)

result = dds_client.execute(add_service_mutation)["addService"]

print(f"new service name: {result['service']['name']}")
print(f"error: {result['error']}")
