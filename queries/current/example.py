import gql
import dds_client

current_query = gql(
    """
    {
        current {
            username
            isAdmin
        }
    }
    """
)

current = dds_client.execute(current_query)

print(f"username: {current.username}")
print(f"is admin user: {current.isAdmin}")
