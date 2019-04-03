import gql
import dds_client

service_type = "REDIS"
service_name = "test-service"
app_name = "test-app"

link_service_mutation = gql(
    """
    mutation {
        linkService(serviceType: {service_type}, serviceName: {service_name}, appname: {app_name}) {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(link_service_mutation)["linkService"]

print(f"success: {result['ok']}")
print(f"error: {result['error']}")
