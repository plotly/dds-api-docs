# config

## Query

```
query config{
    config{
        OAUTH_CLIENT_ID
        PLOTLY_AUTH_WEBAPP_URL
        AUTH_SAML_ENABLED
        AUTH_LDAP_ENABLED
        SSL_DASH_CERT_GENERATE
        AUTH_PASSWORD
        HA_ENABLED
        DASH_APP_VIEWERS
    }
}
```

## Returns

Name | Type
---- | ----
OAUTH_CLIENT_ID | `String`
PLOTLY_AUTH_WEBAPP_URL | `String`
AUTH_SAML_ENABLED | `Boolean`
AUTH_LDAP_ENABLED | `Boolean`
SSL_DASH_CERT_GENERATE | `Boolean`
AUTH_PASSWORD | `Boolean`
HA_ENABLED | `Boolean`
DASH_APP_VIEWERS | `Int`
