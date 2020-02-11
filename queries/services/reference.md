# services

## Query

```
query services{
    services{
        name
        serviceType
        created
        status
    }
}
```

## Returns

Name | Type
---- | ----
name | `String`
serviceType | `ServiceType`
created | `DateTime`
status | `String`
