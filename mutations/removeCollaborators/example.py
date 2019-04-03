from gql import gql
import dds_client

remove_collaborators_mutation = gql(
    """
    mutation {
        removeCollaborators(
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

result = dds_client.execute(remove_collaborators_mutation)["removeCollaborators"]

print(f"remaining teams: {result['app']['collaborators']['teams']}")
print(f"remaining users: {result['app']['collaborators']['users']}")
print(f"error: {result['error']}")
