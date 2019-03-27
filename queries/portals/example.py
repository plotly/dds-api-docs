import gql
import dds_client

name = "DEFAULT"

portals_name_query = gql(
    """
    {
        portals(name: $name) {
            portals {
                name
                logoUrl
            }
        }
    }
    """
)

result = dds_client.execute(portals_name_query)

print("portal name: {result.portals[0].name")
print("portal name: {result.portals[0].logoUrl")
