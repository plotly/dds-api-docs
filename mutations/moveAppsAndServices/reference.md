# moveAppsAndServices

## Mutation

```
mutation moveAppsAndServices($sourceUsername: String, $targetUsername: String){
    moveAppsAndServices(sourceUsername: $sourceUsername, targetUsername: $targetUsername){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
sourceUsername | `String`
targetUsername | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
