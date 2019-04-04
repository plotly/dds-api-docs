import json
from gql import gql
from dds import client as dds_client

metadata = json.dumps(
    {"name": "portal-meta-name", "description": "This is a description for a portal."}
)

update_portal_mutation = gql(
    """
    mutation UpdatePortal($metadata: JSONString!) {
        updatePortal(
            portalname: "default",
            metadata: $metadata
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

result = dds_client.execute(update_portal_mutation, {"metadata": metadata})[
    "updatePortal"
]

print(f"updated portal name: {result['portal']['name']}")
print(f"updated metadata: {json.loads(result['portal']['metadata'])}")
print(f"updated portal's first app name: {result['portal']['apps']['apps'][0]['name']}")
print(f"error: {result['error']}")
