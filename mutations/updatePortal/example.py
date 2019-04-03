from gql import gql
import dds_client

update_portal_mutation = gql(
    """
    mutation {
        updatePortal(
            portalname:  "test-portal",
            metadata: {
                "name": "portal-meta-name",
                "description": "This is a description for a portal."
            }
        ) {
            portal {
                name
                metadata
                apps {
                    apps {
                        name
                    }
                    nextPage
                }
            }
            error
        }
    }
  """
)

result = dds_client.execute(update_portal_mutation)["updatePortal"]

print(f"updated portal name: {result['portal']['name']}")
print(f"updated metadata: {result['portal']['metadata']}")
print(f"updated portal's first app name: {result['portal']['apps']['apps'][0]['name']}")
print(f"error: {result['error']}")
