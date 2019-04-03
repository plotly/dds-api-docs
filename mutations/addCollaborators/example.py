from gql import gql
import dds_client

add_collaborators_mutation = gql(
    """
    mutation {
        addCollaborators(
            teams: ["test-team-0", "test-team-1"],
            users: ["test-user-0", "test-user-1"],
            appname: "test-app"
        ) {
            app {
                collaborators {
                    users
                    teams
                }
            }
            error
        }
    }
    """
)

result = dds_client.execute(add_collaborators_mutation)["addCollaborators"]

print(f"new user collaborator: {result['app']['collaborators'][0]['users'][0]}")
print(f"error: {result['error']}")
