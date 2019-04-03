from gql import gql
import dds_client
import json

meta_data = json.dumps(
    {
        "title": "title",
        "description": "description",
        "tags": "tag1,tag2,tag3",
        "isPublic": True,
        "showInPortal": True,
        "contact": {"name": "contact-name", "email": "contact-email@test.com"},
    }
)
app_name = "test-app"

update_app_mutation = gql(
    """
    mutation {
        updateApp(metadata: {meta_data}, appname: {app_name}) {
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
