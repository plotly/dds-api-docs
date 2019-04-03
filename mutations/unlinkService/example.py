from gql import gql
import dds_client

unlink_service_mutation = gql(
    """
    mutation {
        unlinkService(
            serviceType: "REDIS",
            serviceName: "test-service",
            appname: "test-app"
        ) {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(unlink_service_mutation)["unlinkService"]

print(f"success: {result['ok']}")
print(f"error: {result['error']}")
