import gql
import dds_client

config_query = gql(
    """
    {
        config {
            OAUTH_CLIENT_ID
            PLOTLY_AUTH_WEBAPP_URL
            AUTH_SAML_ENABLED
            SSL_DASH_CERT_GENERATE
            AUTH_PASSWORD
        }
    }
    """
)

config = dds_client.execute(config_query)["config"]

print(f"auth password: {config['AUTH_PASSWORD']}")
