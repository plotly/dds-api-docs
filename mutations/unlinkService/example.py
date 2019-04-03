import gql
import dds_client

service_type = "REDIS"
service_name = "test-service"
app_name = "test-app"

unlink_service_mutation = gql(
    """
    mutation {
        unlinkService(serviceType: {service_type}, serviceName: {service_name}, appname: {app_name}) {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(unlink_service_mutation)

print(f"success: {result.ok}")
print(f"error: {result.error}")
