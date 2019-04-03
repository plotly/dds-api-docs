from gql import gql
from dds import client as dds_client

delete_service_mutation = gql(
    """
    mutation {
        deleteService(serviceType: REDIS, name: "test-service") {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(delete_service_mutation)["deleteService"]

print(f"success: {result['ok']}")
print(f"error: {result['error']}")
