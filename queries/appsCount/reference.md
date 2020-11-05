# appsCount

## Query

```
query appsCount{
    appsCount{
        username
        count
        user{
            username
            isDashCreator
        }
    }
}
```

## Returns

Name | Type
---- | ----
username | `String`
count | `Int`
user | `User`
