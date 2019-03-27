import gql
import dds_client

service_type = "REDIS"
name = "test-service"

delete_service_mutation = gql(
    """
    {
        deleteService(serviceType: {service_type}, name: {name}) {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(delete_service_mutation)

print("success: {result.ok}")
print("error: {result.error}")
