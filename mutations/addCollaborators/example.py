import gql
import dds_client

teams = ["test-team-0", "test-team-1"]
users = ["test-user-0", "test-user-1"]
app_name = "test-app"

add_collaborators_mutation = gql(
    """
    mutation {
        addCollaborators(teams: {teams}, users: {users}, appname: {app_name}) {
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

result = dds_client.execute(add_collaborators_mutation)

print(f"new user collaborator: {result.app.collaborators[0].users[0]}")
print(f"error: {result.error}")
