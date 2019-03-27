# services

## Query

```
query services{
    services{
        name
        serviceType
        created
    }
}
```

## Returns

Name | Type
---- | ----
name | `String`
serviceType | `ServiceType`
created | `DateTime`
