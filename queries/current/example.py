import gql
import dds_client

current_query = gql(
    """
    {
        current {
            username
        }
    }
    """
)

current = dds_client.execute(current_query)

print("username: {current.username}")
