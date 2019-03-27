from gql import Client
from gql.transport.requests import RequestsHTTPTransport

DDS_ENDPOINT = "https://dds.example.com/graphql"

transport = RequestsHTTPTransport(url=DDS_ENDPOINT, use_json=True)

dds_client = Client(retries=3, transport=transport)
