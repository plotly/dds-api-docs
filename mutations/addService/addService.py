import gql
import dds_client

service_type = "REDIS"
name = "test-service"

add_service_mutation = gql(
    """
    mutation {
        addService(serviceType: {service_type}, name: {name}) {
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
