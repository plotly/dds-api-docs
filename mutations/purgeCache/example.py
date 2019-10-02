from gql import gql
from dds import client as dds_client

purge_cache_mutation = gql(
    """
    mutation {
        purgeCache(appname: "test-app") {
            ok
            error
        }
    }
    """
)

result = dds_client.execute(purge_cache_mutation)["purgeCache"]

print(f"success: {result['ok']}")
print(f"error: {result['error']}")
