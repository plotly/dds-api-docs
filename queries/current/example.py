from gql import gql
from dds import client as dds_client

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

current = dds_client.execute(current_query)["current"]

print(f"username: {current['username']}")
print(f"is admin user: {current['isAdmin']}")
