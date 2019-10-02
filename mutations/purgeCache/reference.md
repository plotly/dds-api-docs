# purgeCache

## Mutation

```
mutation purgeCache($appname: String){
    purgeCache(appname: $appname){
        ok
        error
    }
}
```

## Arguments

Name | Type
---- | ---- 
appname | `String`

## Returns

Name | Type
---- | ----
ok | `Boolean`
error | `String`
