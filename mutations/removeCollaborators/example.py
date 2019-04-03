import gql
import dds_client

teams = ["test-team-0", "test-team-1"]
users = ["test-user-0", "test-user-1"]
app_name = "test-app"

remove_collaborators_mutation = gql(
    """
    mutation {
        removeCollaborators(teams: {teams}, users: {users}, appname: {app_name}) {
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
