import gql
import dds_client
import json

meta_data = json.dumps(
    {
        "name": "portal-meta-name",
        "description": "This is a description for a portals metadata.",
    }
)

portal_name = "test-portal"

update_portal_mutation = gql(
    """
  updatePortal(portalname: {portal_name}, metadata: {meta_data}) {
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
  """
)

result = dds_client.execute(update_portal_mutation)

print("updated portal name: {result.portal.name}")
print("updated metadata: {result.portal.metadata}")
print("updated portal's first app name: {result.portal.apps[0].name}")
print("error: {result.error}")
