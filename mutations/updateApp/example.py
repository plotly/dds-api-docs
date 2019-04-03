from gql import gql
from dds import client as dds_client

update_app_mutation = gql(
    """
    mutation {
        updateApp(metadata: {
                "title": "title",
                "description": "description",
                "tags": "tag1,tag2,tag3",
                "isPublic": True,
                "showInPortal": True,
                "contact": {
                    "name": "contact-name",
                    "email": "contact-email@test.com"
                }
            },
            appname: "test-app"
        ) {
            app {
                name
                metadata {
                    title
                    description
                    tags
                    isPublic
                    showInPortal
                    contact {
                        name
                        email
                    }
                }
            }
            error
        }
    }
    """
)

result = dds_client.execute(update_app_mutation)["updateApp"]

print(f"updated app name: {result['app']['name']}")
print(
    f"updated metadata contact email: {result['app']['metadata']['contact']['email']}"
)
print(f"error: {result['error']}")
