from gql import gql
from dds import client as dds_client

link_service_mutation = gql(
    """
    mutation {
        linkService(
            serviceType: REDIS,
            serviceName: "test-service",
            appname: "test-app"
        ) {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(link_service_mutation)["linkService"]

print(f"success: {result['ok']}")
print(f"error: {result['error']}")
