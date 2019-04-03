import gql
import dds_client

apps_count_query = gql(
    """
    {
        appsCount {
            username
            count
        }
    }
    """
)

result = dds_client.execute(apps_count_query)["appsCount"]

print(f"first count: {result[0]['count']}")
print(f"first username: {result[0]['username']}")
