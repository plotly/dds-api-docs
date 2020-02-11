# setResources

## Mutation

```
mutation setResources($appname: String, $resources: [ResourceInput]){
    setResources(appname: $appname, resources: $resources){
        ok
        refresh
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
appname | `String`
resources | `[ResourceInput]`

## Returns

Name | Type
---- | ----
ok | `Boolean`
refresh | `Boolean`
error | `String`
